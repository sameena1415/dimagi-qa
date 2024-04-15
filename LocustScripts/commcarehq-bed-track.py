import logging
import os
import time

import yaml
import random
import json

from collections import defaultdict
from locust import HttpUser, SequentialTaskSet, between, task, tag
from lxml import etree
from datetime import datetime


class WorkloadModelSteps(SequentialTaskSet):
    wait_time = between(5, 15)

    def on_start(self):
        # get domain user credential and app config info
        with open(self.user.app_config) as json_file:
            data = json.load(json_file)
            self.FUNC_HOME_SCREEN = data['FUNC_HOME_SCREEN']
            self.FUNC_SEARCH_FOR_BEDS_MENU = data['FUNC_SEARCH_FOR_BEDS_MENU']
            self.FUNC_ENTER_AGE = data['FUNC_ENTER_AGE']
            self.FUNC_GENDER_IDENTITY = data['FUNC_GENDER_IDENTITY']
            self.FUNC_INVOLUNTARY_CLIENT = data['FUNC_INVOLUNTARY_CLIENT']
            self.FUNC_JUSTICE_INVOLVED_CLIENT = data['FUNC_JUSTICE_INVOLVED_CLIENT']
            self.FUNC_CARE_TYPE = data['FUNC_CARE_TYPE']
            self.FUNC_FACILITY_NAME = data['FUNC_FACILITY_NAME']
            self.FUNC_RESIDENTIAL_SERVICE = data['FUNC_RESIDENTIAL_SERVICE']
            self.FUNC_POPULATION_SPECIALTY = data['FUNC_POPULATION_SPECIALTY']
            self.FUNC_INSURANCE_ACCEPTED = data['FUNC_INSURANCE_ACCEPTED']
            self.FUNC_ACCOMMODATIONS = data['FUNC_ACCOMMODATIONS']
            self.FUNC_LANGUAGE_SERVICES = data['FUNC_LANGUAGE_SERVICES']
            self.FUNC_OPEN_BEDS = data['FUNC_OPEN_BEDS']
            self.FUNC_PERFORM_A_SEARCH = data['FUNC_PERFORM_A_SEARCH']

        self._log_in()
        self._get_build_info()


    def _log_in(self):
        logging.info("_log_in - mobile worker: " + self.user.login_as)
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
        logging.info("_get_build_info - mobile worker: " + self.user.login_as)
        response = self.client.get(f'/a/{self.user.domain}/cloudcare/apps/v2/?option=apps', name='build info')
        assert (response.status_code == 200)
        for app in response.json():
            if app['copy_of'] == self.user.app_id:
                # get build_id
                self.build_id = app['_id']
        logging.info("build_id: " + self.build_id)

    # @tag('sync_app')
    # @task
    # def sync_app(self):
    #     logging.info("sync_app")
    #     data = self._formplayer_post("sync-db", name="Sync App")
    #     assert (data['status'] == "accepted")
    #
    # @task
    # def clear_user_data(self):
    #     logging.info("clear user data")
    #     data = self._formplayer_post("clear_user_data", name="Clear User Data")
    #     assert (data['type'] == "success")

    @tag('home_screen')
    @task
    def home_screen(self):
        try:
            logging.info("home_screen - mobile worker: " + self.user.login_as)
            data = self._formplayer_post("navigate_menu_start", name="Home Screen", checkKey="title",
                                         checkValue=self.FUNC_HOME_SCREEN['title'])
            assert data['title'] == self.FUNC_HOME_SCREEN['title'], "formplayer response does not contain title or title is incorrect - with mobile worker: " + self.user.login_as
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu_start")
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu_start; exception: " + str(e))

    @tag('search_for_beds_menu')
    @task
    def search_for_beds_menu(self):
        try:
            logging.info("all_cases_case_list - mobile worker:" + self.user.login_as)
            data = self._formplayer_post("navigate_menu", extra_json={
                "selections": [self.FUNC_SEARCH_FOR_BEDS_MENU['selections']],
            }, name="Open Search for Beds Menu", checkKey="title", checkValue=self.FUNC_SEARCH_FOR_BEDS_MENU['title'])
            # logging.info("===>>>>>>>>>" + str(data))
            assert data['title'] == self.FUNC_SEARCH_FOR_BEDS_MENU['title'],  "formplayer response does not contain title or title is incorrect - with mobile worker: " + self.user.login_as
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu")
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))


    @tag('perform_a_search')
    @task
    def perform_a_search(self):
        for i in range(0, 20):
            try:
                logging.info("perform_a_search_" + str(i) + " mobile worker:" + self.user.login_as)
                start_time = time.time()
                data = self._formplayer_post("navigate_menu", extra_json={
                    "query_data": {
                        "search_command.m1": {
                            "inputs": {
                                self.FUNC_ENTER_AGE['input']: self.FUNC_ENTER_AGE['inputValue'],
                                self.FUNC_GENDER_IDENTITY['input']: self.FUNC_GENDER_IDENTITY['inputValue'],
                                self.FUNC_INVOLUNTARY_CLIENT['input']: self.FUNC_INVOLUNTARY_CLIENT['inputValue'],
                                self.FUNC_JUSTICE_INVOLVED_CLIENT['input']: self.FUNC_JUSTICE_INVOLVED_CLIENT[
                                    'inputValue'],
                                self.FUNC_CARE_TYPE['input']: self.FUNC_CARE_TYPE['inputValue'],
                                self.FUNC_FACILITY_NAME['input']: self.FUNC_FACILITY_NAME['inputValue'],
                                self.FUNC_RESIDENTIAL_SERVICE['input']: self.FUNC_RESIDENTIAL_SERVICE['inputValue'],
                                self.FUNC_POPULATION_SPECIALTY['input']: self.FUNC_POPULATION_SPECIALTY['inputValue'],
                                self.FUNC_INSURANCE_ACCEPTED['input']: self.FUNC_INSURANCE_ACCEPTED['inputValue'],
                                self.FUNC_ACCOMMODATIONS['input']: self.FUNC_ACCOMMODATIONS['inputValue'],
                                self.FUNC_LANGUAGE_SERVICES['input']: self.FUNC_LANGUAGE_SERVICES['inputValue'],
                                self.FUNC_OPEN_BEDS['input']: self.FUNC_OPEN_BEDS['inputValue']
                            },
                            "execute": True}
                    },
                    "selections": ["0"],
                }, name="Perform a Search")
                assert 'entities' in data, "formplayer response does not contain entities - with mobile worker: " + self.user.login_as
                end_time = time.time()
                total_time = end_time - start_time
                rng = random.randrange(5, 15)
                logging.info(
                    "Total response time for Bed Tracking Search for user: " + self.user.username + " with mobile worker: " + self.user.login_as + " for loop " + str(
                        i) + " is " + str(total_time) + " seconds.")
                logging.info(
                    "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu")
                logging.info("mobile worker: " + self.user.login_as + " Sleeping for-->" + str(rng))
                time.sleep(rng)
            except Exception as e:
                logging.info(
                    "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))

        @task
        def stop(self):
            logging.info("stopping - mobile worker: " + self.user.login_as)
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
            # logging.info("data-->" + str(data))
            if "exception" in data:
                logging.info("ERROR::exception error--" + data['exception'])
                logging.info("ERROR::user-info::" + self.user.username + "::" + self.user.login_as)
                response.failure("exception error--" + data['exception'])
            elif checkKey and checkKey not in data:
                logging.info("error::" + checkKey + " not in data")
                response.failure("ERROR::" + checkKey + " not in data")
            # elif checkKey and checkLen:
            #     if len(data[checkKey]) != checkLen:
            #         logging.info("ERROR::len(data['" + checkKey + "']) != " + checkLen)
            #         response.failure("error::len(data['" + checkKey + "']) != " + checkLen)
            # elif checkKey and checkValue:
            #     if data[checkKey] != checkValue:
            #         logging.info("ERROR::data['" + checkKey + "'] != " + checkValue)
            #         response.failure("error::data['" + checkKey + "'] != " + checkValue)
        return response.json()


class LoginCommCareHQWithUniqueUsers(HttpUser):
    tasks = [WorkloadModelSteps]

    formplayer_host = "/formplayer"
    project = 'bha-bed-tracking-perf'  # str(os.environ.get("project"))
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
