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
        self.FUNC_ENTER_GENDER = APP_CONFIG["FUNC_ENTER_GENDER"]
        self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM = APP_CONFIG["FUNC_OUTGOING_REFERRAL_DETAILS_FORM"]
        self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM_SUBMIT = APP_CONFIG["FUNC_OUTGOING_REFERRAL_DETAILS_FORM_SUBMIT"]

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
                        self.FUNC_ENTER_GENDER['input']: self.FUNC_ENTER_GENDER['inputValue']
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
            self.selected_case_id = entities[0]['id']
        except formplayer.FormplayerResponseError as e:
            logging.info(str(e) + " - mobile worker: " + self.user.user_detail.login_as)

    @tag('enter_outgoing_referral_details_form')
    @task
    def enter_create_profile_and_refer_form(self):
        logging.info("Entering form - mobile worker:" + self.user.user_detail.login_as + "; request: navigate_menu")

        validation = formplayer.ValidationCriteria(keys=["title"],
                                                key_value_pairs = {"title": self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM['title']})
        extra_json = {
                    "selections": [self.FUNC_OUTGOING_REFERRALS_MENU['selections'], self.selected_case_id, self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM['selections']],
                }
        try:
            data = self.user.HQ_user.post_formplayer("navigate_menu", self.client,  self.user.app_details,
                                                    extra_json=extra_json, name="Enter 'Outgoing Referral Details' Form",
                                                    validation=validation)
        except formplayer.FormplayerResponseError as e:
            logging.info(str(e) + " - mobile worker: " + self.user.user_detail.login_as)
        self.session_id = data['session_id']

    @tag('answer_outgoing_referral_details_form_questions')
    @task
    def answer_outgoing_referral_details_form_questions(self):
        logging.info("Answering Questions - mobile worker:" + self.user.user_detail.login_as + "; request: answer")
        for question in self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM["questions"].values():
            validation = formplayer.ValidationCriteria(keys=["title"],
                                                    key_value_pairs = {"title": self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM['title']})
            extra_json = {
                    "ix": question["ix"],
                    "answer": question["answer"],
                    "session_id": self.session_id,
                }
            try:
                data = self.user.HQ_user.post_formplayer("answer", self.client, self.user.app_details, validation=validation,
                                                extra_json=extra_json, name="Answer 'Outgoing Referral Details' Question")
            except formplayer.FormplayerResponseError as e:
                logging.info(str(e) + " - mobile worker: " + self.user.user_detail.login_as)
            rng = random.randrange(1,3)
            time.sleep(rng)

        def find_question_ix(data, result=dict()):
            nested_items = data.get('children', {})
            for children in nested_items:
                    # If the current item matches the target_ix, check if it's a question
                if children.get('type') == 'question':
                    result[children.get('ix')] = "OK"
                if 'children' in children:
                    # If the current item has children, recursively call the function on them
                    find_question_ix(children, result)
            return result

        # Question ix 10 is a count repeat group that varies depending on the case selected. So the "answer" with the appropriate
        # ix keys need to be dynamically generated to be used in submit
        for item in data["tree"]:
            if item.get('ix') == "10":
                self.attached_referral_requests_answers = find_question_ix(item)

    @tag('submit_outgoing_referral_details_form')
    @task
    def submit_outgoing_referral_details_form(self):
        logging.info("Submitting form - mobile worker:" + self.user.user_detail.login_as + "; request: submit_all")
        utc_time_tuple = time.gmtime(time.time() - 86400) #ensure we're not picking a date that would be tomorrow in local time
        formatted_date = "{:04d}-{:02d}-{:02d}".format(utc_time_tuple.tm_year, utc_time_tuple.tm_mon, utc_time_tuple.tm_mday)

        answers = {
            "2,0": 1,
            "3,1,0": 1,
            "3,1,5": formatted_date,
            "7,0": "OK",
            "8,0": "OK",
            "8,1": "OK",
            "8,2": None,
            "8,3,0": "OK",
            "8,3,1": "OK",
            "8,3,2": "OK",
            "8,3,3": "OK",
            "8,3,4": "OK",
            "8,3,5": "OK",
            "8,3,6": "OK",
            "8,3,7": "OK",
            "8,3,8": "OK",
            "8,3,9": "OK",
            "8,3,10": "OK",
            "8,3,11": "OK",
            "8,3,12": "OK",
            "8,3,13": "OK",
            "8,3,14": "OK",
            "8,3,15": "OK",
            "8,3,16": "OK",
            "8,3,17": "OK",
            "8,3,18": "OK",
            "8,3,19": "OK",
            "8,3,20": "OK",
            "8,3,21":"OK",
        }
        answers.update(self.attached_referral_requests_answers)
        input_answers= {d["ix"]: d["answer"] for d in self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM["questions"].values()}
        answers.update(input_answers)

        validation = formplayer.ValidationCriteria(keys=["submitResponseMessage"],
                                                key_value_pairs={"submitResponseMessage": self.FUNC_OUTGOING_REFERRAL_DETAILS_FORM_SUBMIT['submitResponseMessage']})
        extra_json = {
            "answers": answers,
            "prevalidated": True,
            "debuggerEnabled": True,
            "session_id": self.session_id,
        }
        self.user.HQ_user.post_formplayer("submit-all", self.client, self.user.app_details, extra_json=extra_json,
                                        name="Submit Outgoing Referral Details Form", validation=validation)


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
