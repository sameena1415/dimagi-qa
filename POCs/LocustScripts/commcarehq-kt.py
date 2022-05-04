import logging
import os
import yaml
import random
import json

from collections import defaultdict
from locust import HttpUser, SequentialTaskSet, between, task, tag
from lxml import etree
from datetime import datetime

CASE_IDS = [
    "aef93695-5638-4ffa-8acd-5748339b7eaa",
    "0b5b3fec-acf5-470f-bb7b-a7e67471224a",
]


# noinspection PyShadowingNames
class WorkloadModelSteps(SequentialTaskSet):
    def on_start(self):
        # get domain user credential and app config info
        with open(self.user.app_config) as json_file:
            data = json.load(json_file)
            self.FUNC_HOME_SCREEN = data['FUNC_HOME_SCREEN']
            self.FUNC_ALL_CASES_CASE_LIST = data['FUNC_ALL_CASES_CASE_LIST']
            self.CASES_LIST_FILTER = data['CASES_LIST_FILTER']
            self.FUNC_CASE_DETAILS = data['FUNC_CASE_DETAILS']
            self.FUNC_CI_FORM = data['FUNC_CI_FORM']
            self.FUNC_PART_OF_CLUSTER = data['FUNC_PART_OF_CLUSTER']
            self.FUNC_HOSPITAL_NAME = data['FUNC_HOSPITAL_NAME']
            self.FUNC_CI_FORM_SUBMIT = data['FUNC_CI_FORM_SUBMIT']
            self.FUNC_REG_FORM = data['FUNC_REG_FORM']
            self.FUNC_ADD_CASE = data['FUNC_ADD_CASE']
            self.FUNC_REGISTRATION_FORM_SUBMIT = data['FUNC_REGISTRATION_FORM_SUBMIT']

        self._log_in()
        self._get_build_info()

    # noinspection PyUnusedLocal
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

    def _get_all_cases_ids(self):
        url = f'/a/{self.user.domain}/phone/restore/{self.user.build_id}/?skip_fixtures=true'
        if self.user.login_as:
            url += f'&as={self.user.login_as}@{self.user.domain}.commcarehq.org'
        response = self.client.get(url, name='Restore')
        assert (response.status_code == 200)

        namespaces = {None: 'http://commcarehq.org/case/transaction/v2'}
        self.case_ids = defaultdict(list)
        root = etree.fromstring(response.text)
        for case in root.findall('case', namespaces=namespaces):
            case_type = case.findall('create/case_type', namespaces=namespaces)[0].text
            self.case_ids[case_type].append(case.attrib.get('case_id'))

    def _get_case_id_patient(self, case_type):
        case_id = random.choice(self.case_ids[case_type])
        print("case_id" + case_id)
        return case_id

    @tag('home_screen')
    @task
    def home_screen(self):
        logging.info("home_screen")
        data = self._formplayer_post("navigate_menu_start", name="Home Screen", checkKey="title",
                                     checkValue=self.FUNC_HOME_SCREEN['title'])
        assert (data['title'] == self.FUNC_HOME_SCREEN['title'])

    @tag('all_cases_case_list')
    @task
    def all_cases_case_list(self):
        logging.info("all_cases_case_list")
        data = self._formplayer_post("navigate_menu", extra_json={
            "selections": [self.FUNC_ALL_CASES_CASE_LIST['selections']],
        }, name="All Cases Case List", checkKey="title", checkValue=self.FUNC_ALL_CASES_CASE_LIST['title'])
        logging.info("===>>>>>>>>>" + str(data))
        assert (data['title'] == self.FUNC_ALL_CASES_CASE_LIST['title'])
        assert (len(data['entities']))  # should return at least one case

    # noinspection PyProtectedMember
    @tag('register-case')
    @task
    # Reg Form
    class RegFormEntry(SequentialTaskSet):
        @task
        def reg_form(self):
            # Register a case
            # noinspection PyProtectedMember
            data = self.parent._formplayer_post("navigate_menu", extra_json={
                "selections": [self.parent.FUNC_REG_FORM['selections'], self.parent.FUNC_REG_FORM['subselections']],
            }, name="Registration Form Entry", checkKey="title", checkValue=self.parent.FUNC_REG_FORM['title'])
            if not ("session_id" in data):
                logging.info("no session_id")
                self.interrupt()
            self.session_id = data['session_id']
            logging.info("reg_form==reg_form::sessionId::" + self.session_id)
            assert (data['title'] == self.parent.FUNC_REG_FORM['title'])

        @task
        def user_name_register(self):
            # Add case name free text response
            data = self.parent._formplayer_post("answer", extra_json={
                "answer": self.parent.FUNC_ADD_CASE['answer'],
                "ix": self.parent.FUNC_ADD_CASE['ix'],
                "debuggerEnabled": True,
                "session_id": self.session_id
            }, name="Name for Registration Form", checkKey="title",
                                                checkValue=self.parent.FUNC_ADD_CASE['title'])
            logging.info("reg_form==reg_form::sessionId::" + self.session_id)
            logging.info("data-details===" + str(data))
            assert (data['title'] == self.parent.FUNC_ADD_CASE['title'])

        @task
        def registration_form_submit(self):
            data = self.parent._formplayer_post("submit-all", extra_json={
                "answers": {
                    self.parent.FUNC_REGISTRATION_FORM_SUBMIT['answers-key1']:
                        self.parent.FUNC_REGISTRATION_FORM_SUBMIT[
                            'answers-value1'],
                },
                "prevalidated": True,
                "debuggerEnabled": True,
                "session_id": self.session_id,
            }, name="Registration Form Submit", checkKey="submitResponseMessage",
                                                checkValue=self.parent.FUNC_REGISTRATION_FORM_SUBMIT[
                                                    'submitResponseMessage'])
            logging.info("data-details===" + str(data))
            assert (data['submitResponseMessage'] == self.parent.FUNC_REGISTRATION_FORM_SUBMIT['submitResponseMessage'])

        @task
        def stop(self):
            self.interrupt()

    # noinspection PyProtectedMember
    @tag('form entry')
    @task
    # Follow Up Form
    class CIFormEntry(SequentialTaskSet):
        @task
        def case_details(self):
            # select All Cases, then a case
            self.local_case_id = random.choice(CASE_IDS)
            logging.info("ci-form==case_details::case_id::" + self.local_case_id)
            data = self.parent._formplayer_post("get_details", extra_json={
                "selections": [self.parent.FUNC_CASE_DETAILS['selections'], self.local_case_id],
            }, name="Case Detail for Followup Form", checkKey=self.parent.FUNC_CASE_DETAILS['checkKey'],
                                                checkLen=self.parent.FUNC_CASE_DETAILS['checkLen'])
            logging.info("data-details===" + str(data))
            assert (len(data['details']) == self.parent.FUNC_CASE_DETAILS['checkLen'])

        @task
        def ci_form(self):
            # Select All Cases, then a case, then Case Investiation form
            self.local_case_id = random.choice(CASE_IDS)
            logging.info("ci-form==ci_form::case_id::" + self.local_case_id)
            data = self.parent._formplayer_post("navigate_menu", extra_json={
                "selections": [self.parent.FUNC_CI_FORM['selections'], self.local_case_id,
                               self.parent.FUNC_CI_FORM['subselections']],
            }, name="Followup Form Entry", checkKey="title", checkValue=self.parent.FUNC_CI_FORM['title'])
            if not ("session_id" in data):
                logging.info("case not found -- no session_id")
                self.interrupt()
            self.session_id = data['session_id']
            logging.info("ci_form==ci_form::sessionId::" + self.session_id)
            assert (data['title'] == self.parent.FUNC_CI_FORM['title'])
            assert ('instanceXml' in data)

        @task
        def part_of_cluster(self):
            # Is this case part of a cluster? --> select No
            logging.info("ci-form==part_of_cluster::case_id::" + self.local_case_id)
            data = self.parent._formplayer_post("answer", extra_json={
                "answer": self.parent.FUNC_PART_OF_CLUSTER['answer'],
                "ix": self.parent.FUNC_PART_OF_CLUSTER['ix'],
                "debuggerEnabled": True,
                "session_id": self.session_id
            }, name="Part of Cluster for Followup Form", checkKey="title",
                                                checkValue=self.parent.FUNC_PART_OF_CLUSTER['title'])
            logging.info("data-details===" + str(data))
            assert (data['title'] == self.parent.FUNC_PART_OF_CLUSTER['title'])

        @task
        def hospital_name(self):
            # hospital name free text response
            logging.info("ci-form==hospital_name::case_id::"+self.local_case_id)
            data = self.parent._formplayer_post("answer", extra_json={
                "answer": self.parent.FUNC_HOSPITAL_NAME['answer'],
                "ix": self.parent.FUNC_HOSPITAL_NAME['ix'],
                "debuggerEnabled": True,
                "session_id": self.session_id
            }, name="Hospital Name for Followup Form", checkKey="title",
                                                checkValue=self.parent.FUNC_HOSPITAL_NAME['title'])
            logging.info("data-details===" + str(data))
            assert(data['title'] == self.parent.FUNC_HOSPITAL_NAME['title'])

        @task
        def ci_form_submit(self):
            logging.info("ci-form==ci_form_submit::case_id::" + self.local_case_id)
            data = self.parent._formplayer_post("submit-all", extra_json={
                "answers": {
                    self.parent.FUNC_CI_FORM_SUBMIT['answers-key1']: self.parent.FUNC_CI_FORM_SUBMIT['answers-value1'],
                    self.parent.FUNC_CI_FORM_SUBMIT['answers-key2']: self.parent.FUNC_CI_FORM_SUBMIT['answers-value2'],
                },
                "prevalidated": True,
                "debuggerEnabled": True,
                "session_id": self.session_id,
            }, name="Followup Form Submit", checkKey="submitResponseMessage",
                                                checkValue=self.parent.FUNC_CI_FORM_SUBMIT['submitResponseMessage'])
            logging.info("data-details===" + str(data))
            assert (data['submitResponseMessage'] == self.parent.FUNC_CI_FORM_SUBMIT['submitResponseMessage'])

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
            response = self.client.get(f"{self.parent.formplayer_host}/serverup")
            response.raise_for_status()

        xsrf_token = self.client.cookies['XSRF-TOKEN']
        headers = {'X-XSRF-TOKEN': xsrf_token}
        self.client.headers.update(headers)

        with self.client.post(f"{self.user.formplayer_host}/{command}/", json=json, name=name,
                              catch_response=True) as response:
            data = response.json()
            logging.info("data-->"+str(data))
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
    project = str(os.environ.get("project"))
    domain_user_credential_force = str(os.environ.get("user_credential"))
    app_config_force = str(os.environ.get("app_config"))
    wait_time_force = "test"

    if wait_time_force == "test":
        wait_time = between(5, 10)

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
        print("userinfo===>>" + str(user_info))

        logging.info("timestamp-->>>" + str(dt_object))
        logging.info("host-->>>" + self.host)
        logging.info("login_as-->>>" + self.login_as)
        logging.info("username-->>>" + self.username)
        logging.info("domain-->>>" + self.domain)
        logging.info("domain_user_credential-->>>" + self.domain_user_credential)
        logging.info("app_config-->>>" + self.app_config)
