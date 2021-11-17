import json
import logging
import os
from datetime import datetime

import yaml
from locust import HttpUser, TaskSet, between, task, tag


class WorkloadModelSteps(TaskSet):
    def on_start(self, x=0):
        # get domain user credential and app config info
        with open(self.user.app_config) as json_file:
            data = json.load(json_file)
            self.FUNC_HOME_SCREEN = data['FUNC_HOME_SCREEN']
            self.FUNC_ALL_CASES_CASE_LIST = data['FUNC_ALL_CASES_CASE_LIST']
        self._log_in()
        self._get_build_info()

    def _log_in(self):
        logging.info("_log_in")
        login_url = f'/a/{self.user.domain}/login/'
        response = self.client.get(login_url)
        response = self.client.post(
            login_url,
            {
                "auth-username": self.user.username,
                "auth-password": self.user.password,
                "cloud_care_login_view-current_step": ['auth'],  # fake out two_factor ManagementForm
            },
            headers={
                "X-CSRFToken": self.client.cookies.get('csrftoken'),
                "REFERER": f'{self.user.host}{login_url}',  # csrf requires this for secure requests
            },
        )
        assert (response.status_code == 200)
        assert ('Sign In' not in response.text)  # make sure we weren't just redirected back to login

    def _get_build_info(self):
        logging.info("_get_build_info")
        response = self.client.get(f'/a/{self.user.domain}/cloudcare/apps/v2/?option=apps', name='build info')
        assert (response.status_code == 200)
        for app in response.json():
            if app['copy_of'] == self.user.app_id:
                # get build_id
                self.build_id = app['_id']
        logging.info("build_id: " + self.build_id)

    @tag('all', 'home_screen')
    @task()
    def home_screen(self):
        logging.info("home_screen")
        data = self._formplayer_post("navigate_menu_start", name="Home Screen", checkKey="title", checkValue=self.FUNC_HOME_SCREEN['title'])
        assert (self.FUNC_HOME_SCREEN['title'] == data['title'])
        # assert(len(data['commands']) == 41)

        # @tag('all', 'all_cases_case_list')
        # @task(6)
        # def all_cases_case_list(self):
        #     logging.info("all_cases_case_list")
        #     data = self._formplayer_post("navigate_menu",extra_json={
        #        "selections" : [self.FUNC_ALL_CASES_CASE_LIST['selections']],
        #     }, name="All Cases Case List", checkKey="title", checkValue=self.FUNC_ALL_CASES_CASE_LIST['title'])
        #     #data = self._navigate_menu([5], name="All Cases case list")
        #     ##logging.info("===>>>>>>>>>"+str(data))
        #     assert(data['title'] == self.FUNC_ALL_CASES_CASE_LIST['title'])
        #     assert(len(data['entities']))       # should return at least one case
        #
        #     @task
        #     def ci_form(self):
        #         # Select All Cases, then a case, then Case Investiation form
        #         logging.info("ci-form==ci_form::case_id::"+self.local_case_id)
        #         data = self.parent._formplayer_post("navigate_menu", extra_json={
        #             "selections": [self.parent.FUNC_CI_FORM['selections'], self.local_case_id, self.parent.FUNC_CI_FORM['subselections']],
        #         }, name="CI Form", checkKey="title", checkValue=self.parent.FUNC_CI_FORM['title'])
        #         if not ("session_id" in data):
        #             logging.info("case not found -- no session_id")
        #             self.interrupt()
        #         self.session_id=data['session_id']
        #         logging.info("ci_form==ci_form::sessionId::"+self.session_id)
        #         assert(data['title'] == self.parent.FUNC_CI_FORM['title'])
        #         assert('instanceXml' in data)

        @task
        def stop(self):
            self.interrupt()

    def _formplayer_post(self, command, extra_json=None, name=None, checkKey=None, checkValue=None, checkLen=None):
        json = {
            "app_id": self.build_id,
            "domain": self.user.domain,
            "locale": "en",
            "restoreAs": self.user.login_as,
            "username": self.user.username,
        }
        if extra_json:
            json.update(extra_json)
        name = name or command

        if 'XSRF-TOKEN' not in self.client.cookies:
            response = self.client.get(f"{self.user.formplayer_host}/serverup")
            response.raise_for_status()

            xsrf_token = self.client.cookies['XSRF-TOKEN']
            headers = {'X-XSRF-TOKEN': xsrf_token}
            self.client.headers.update(headers)

        with self.client.post(f"{self.user.formplayer_host}/{command}/", json=json, name=name,
                              catch_response=True) as response:
            data = response.json()
            print(data)
            if "exception" in data:
                logging.info("ERROR::exception error--" + data['exception'])
                logging.info("ERROR::user-info::" + self.user.username + "::" + self.user.login_as)
                response.failure("exception error--" + data['exception'])
            elif checkKey and checkKey not in data:
                logging.info("error::" + checkKey + " not in data")
                response.failure("ERROR::" + checkKey + " not in data")
            elif checkKey and checkLen:
                if len(data[checkKey]) != checkLen:
                    logging.info("ERROR::len(data['" + checkKey + "']) != " + checkLen)
                    response.failure("error::len(data['" + checkKey + "']) != " + checkLen)
            elif checkKey and checkValue:
                if data[checkKey] != checkValue:
                    logging.info("ERROR::data['" + checkKey + "'] != " + checkValue)
                    response.failure("error::data['" + checkKey + "'] != " + checkValue)
        return response.json()


class LoginCommCareHQWithUniqueUsers(HttpUser):
    tasks = [WorkloadModelSteps]


    formplayer_host = "/formplayer"
    project = "syria-support"
    domain_user_credential_force = str(os.environ.get("user_credential"))
    app_config_force = str(os.environ.get("app_config"))
    wait_time_force = str(os.environ.get("wait_time"))


    if wait_time_force == "test":
        wait_time = between(2, 4)
    else:
        wait_time = between(45, 90)

    with open("project-config/" + project + "/config.yaml") as f:
        config = yaml.safe_load(f)
        host = config['host']
        domain = config['domain']
        app_id = config['app_id']
        if domain_user_credential_force != "None":
            domain_user_credential = "project-config/" + project + "/" + domain_user_credential_force
        else:
            domain_user_credential = config['domain_user_credential']
        if app_config_force != "None":
            app_config = "project-config/" + project + "/" + app_config_force
        else:
            app_config = config['app_config']
        owner_id = config['owner_id']
        case_type = config['case_type']


    # get domain user credential and app config info
    with open(domain_user_credential) as json_file:
        data = json.load(json_file)
        data_user = data['user']

    def on_start(self):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)
        user_info = self.data_user.pop()
        self.username = user_info['username']
        self.password = user_info['password']
        self.login_as = user_info['login_as']
        print("userinfo===>>"+str(user_info))

        logging.info("timestamp-->>>" + str(dt_object))
        logging.info("host-->>>" + self.host)
        logging.info("login_as-->>>" + self.login_as)
        logging.info("username-->>>" + self.username)
        logging.info("domain-->>>" + self.domain)
        logging.info("domain_user_credential-->>>" + self.domain_user_credential)
        logging.info("app_config-->>>" + self.app_config)
