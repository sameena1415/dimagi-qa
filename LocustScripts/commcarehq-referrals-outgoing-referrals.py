import logging
import os
import time

import yaml
import random
import json

from collections import defaultdict
from locust import HttpUser, SequentialTaskSet, between, task, tag, events
from locust.exception import InterruptTaskSet
from lxml import etree
from datetime import datetime

from user.models import UserDetails, HQUser, AppDetails
from common.args import file_path
from common.utils import load_json_data

@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--domain", help="CommCare domain", required=True, env_var="COMMCARE_DOMAIN")
    parser.add_argument("--app-id", help="CommCare app id", required=True, env_var="COMMCARE_APP_ID")
    parser.add_argument("--app-config", help="Configuration of CommCare app", required=True)
    parser.add_argument("--user-details", help="Path to user details file", required=True)

APP_CONFIG = {}
USERS_DETAILS = []
class WorkloadModelSteps(SequentialTaskSet):
    wait_time = between(5, 15)

    def on_start(self):
        self.FUNC_OUTGOING_REFERRALS_MENU = APP_CONFIG["FUNC_OUTGOING_REFERRALS_MENU"]
        self.FUNC_ENTER_STATUS = APP_CONFIG["FUNC_ENTER_STATUS"]
        self.FUNC_ENTER_GENDER = APP_CONFIG["FUNC_ENTER_GENDER"]
        self.FUNC_ENTER_TYPE_OF_CARE = APP_CONFIG["FUNC_ENTER_TYPE_OF_CARE"]

    @tag('outgoing_referrals_menu')
    @task
    def outgoing_referrals_menu(self):
        try:
            logging.info("all_cases_case_list - mobile worker:" + self.user.login_as)
            data = self._formplayer_post("navigate_menu", extra_json={
                "selections": [self.FUNC_OUTGOING_REFERRALS_MENU['selections']],
            }, name="Open Outgoing Referrals Menu", checkKey="title", checkValue=self.FUNC_OUTGOING_REFERRALS_MENU['title'])
            assert "title" in data, "formplayer response does not contain title"
            assert data['title'] == self.FUNC_OUTGOING_REFERRALS_MENU['title'], "title " + data['title'] + " is incorrect"
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu")
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))

    @tag('perform_a_search')
    @task
    def perform_a_search(self):
        logging.info("Performing Search - mobile worker:" + self.user.login_as)
        try:
            data = self._formplayer_post("navigate_menu", extra_json={
                        "query_data": {
                            "search_command.m10_results": {
                                "inputs": {
                                    self.FUNC_ENTER_STATUS['input']: self.FUNC_ENTER_STATUS['inputValue'],
                                    self.FUNC_ENTER_GENDER['input']: self.FUNC_ENTER_GENDER['inputValue'],
                                    self.FUNC_ENTER_TYPE_OF_CARE['input']: self.FUNC_ENTER_TYPE_OF_CARE['inputValue']
                                },
                                "execute": True,
                                "force_manual_search": True}
                        },
                        "selections": [self.FUNC_OUTGOING_REFERRALS_MENU["selections"]],
                    }, name="Perform a Search")
            logging.info(data)
            assert 'entities' in data, "formplayer response does not contain entities"
            entities = data["entities"]
            assert len(entities) > 0, "entities is empty"
            self.selected_case = entities[0]['id']
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))


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
            if "notification" in data and data["notification"]:
                if data["notification"]["type"] == "error":
                    logging.info("ERROR::-" + data["notification"]["message"] + ": With json" + str(json))
                    response.failure("exception error--" + data["notification"]["message"])
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

@events.init.add_listener
def _(environment, **kw):
    try:
        app_config_path = file_path(environment.parsed_options.app_config)
        APP_CONFIG.update(load_json_data(app_config_path))
        logging.info("Loaded app config")
    except Exception as e:
        logging.error("Error loading app config: %s", e)
        raise InterruptTaskSet from e
    try:
        user_path = file_path(environment.parsed_options.user_details)
        user_data = load_json_data(user_path)["user"]
        USERS_DETAILS.extend([UserDetails(**user) for user in user_data])
        logging.info("Loaded %s users", len(USERS_DETAILS))
    except Exception as e:
        logging.error("Error loading users: %s", e)
        raise InterruptTaskSet from e
class LoginCommCareHQWithUniqueUsers(HttpUser):
    tasks = [WorkloadModelSteps]
    wait_time = between(5, 10)

    def on_start(self):
        self.domain = self.environment.parsed_options.domain
        self.host = self.environment.parsed_options.host
        self.user_detail = USERS_DETAILS.pop()
        self.HQ_user = HQUser( self.user_detail)
        logging.info("userinfo-->>>" + str(self.user_detail))

        self.login()
        self.app_details = AppDetails(
        domain = self.domain,
        app_id = self.environment.parsed_options.app_id,
        build_id = self._get_build_info(self.environment.parsed_options.app_id)
        )

    def login(self):
        self.HQ_user.login(self.domain, self.host, self.client)

    def _get_build_info(self, app_id):
        response = self.client.get(f'/a/{self.domain}/cloudcare/apps/v2/?option=apps', name='build info')
        assert (response.status_code == 200)
        for app in response.json():
            if app['copy_of'] == app_id:
                # get build_id
                logging.info("build_id: " + app['_id'])
                return app['_id']
