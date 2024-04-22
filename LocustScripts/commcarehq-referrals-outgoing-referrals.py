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

import formplayer
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
        logging.info("all_cases_case_list - mobile worker: " + self.user.user_detail.login_as + "; request: navigate_menu")
        validation = formplayer.ValidationCriteria(keys=["title"],
                                                key_value_pairs = {"title": self.FUNC_OUTGOING_REFERRALS_MENU['title']})
        extra_json = {
            "selections": [self.FUNC_OUTGOING_REFERRALS_MENU['selections']]
        }
        try:
            self.user.HQ_user.post_formplayer("navigate_menu", self.client,
                                            self.user.app_details, extra_json=extra_json,
                                            name="Home Screen", validation=validation)
        except formplayer.FormplayerResponseError as e:
            logging.info(str(e) + " - mobile worker: " + self.user.user_detail.login_as)

    @tag('perform_a_search')
    @task
    def perform_a_search(self):
        logging.info("Performing Search - mobile worker:" + self.user.user_detail.login_as + "; request: navigate_menu")
        validation = formplayer.ValidationCriteria(keys=["entities"])
        extra_json = {
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
        }
        try:
            data = self.user.HQ_user.post_formplayer("navigate_menu", self.client,
                                                     self.user.app_details, extra_json=extra_json,
                                                     validation=validation, name="Perform a Search")
            entities = data["entities"]
            assert len(entities) > 0, "entities is empty"
            self.selected_case = entities[0]['id']
        except formplayer.FormplayerResponseError as e:
            logging.info(str(e) + " - mobile worker: " + self.user.user_detail.login_as)

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
