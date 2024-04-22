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
        self.FUNC_HOME_SCREEN = APP_CONFIG['FUNC_HOME_SCREEN']
        self.FUNC_SEARCH_FOR_BEDS_MENU = APP_CONFIG['FUNC_SEARCH_FOR_BEDS_MENU']
        self.FUNC_CREATE_PROFILE_AND_REFER_FORM = APP_CONFIG['FUNC_CREATE_PROFILE_AND_REFER_FORM']
        self.FUNC_CREATE_PROFILE_AND_REFER_FORM_QUESTIONS = {
            "FORM_QUESTION_AGE": APP_CONFIG['FORM_QUESTION_AGE'],
            "FORM_QUESTION_GENDER": APP_CONFIG['FORM_QUESTION_GENDER'],
            "FORM_QUESTION_SEEKING_CARE_REASON": APP_CONFIG['FORM_QUESTION_SEEKING_CARE_REASON'],
            "FORM_QUESTION_LEVEL_CARE_NEEDED": APP_CONFIG['FORM_QUESTION_LEVEL_CARE_NEEDED'],
            "FORM_QUESTION_SYMPTOMS": APP_CONFIG['FORM_QUESTION_SYMPTOMS'],
            "FORM_QUESTION_CONSENT": APP_CONFIG['FORM_QUESTION_CONSENT'],
        }
        self.FUNC_CREATE_PROFILE_AND_REFER_FORM_SUBMIT = APP_CONFIG['FUNC_CREATE_PROFILE_AND_REFER_FORM_SUBMIT']
        self.cases_per_page = 100

    @tag('home_screen')
    @task
    def home_screen(self):
        logging.info("home_screen - mobile worker: " + self.user.login_as + "; request: navigate_menu_start")
        validation = formplayer.ValidationCriteria(key_value_pairs = {"tile": self.FUNC_HOME_SCREEN['title']})
        try:
            data = self.user.HQ_user.post_formplayer("navigate_menu_start", self.client,
                                                        self.user.app_details, name="Home Screen",
                                                        validation=validation)
        except formplayer.FormplayerResponseError as e:
            logging.info(str(e))


    @tag('search_for_beds_menu')
    @task
    def search_for_beds_menu(self):
        try:
            logging.info("all_cases_case_list - mobile worker:" + self.user.login_as)
            data = self._formplayer_post("navigate_menu", extra_json={
                "selections": [self.FUNC_SEARCH_FOR_BEDS_MENU['selections']],
                "cases_per_page": self.cases_per_page,
            }, name="Open Search for Beds Menu", checkKey="title", checkValue=self.FUNC_SEARCH_FOR_BEDS_MENU['title'])
            assert "title" in data, "formplayer response does not contain title"
            assert data['title'] == self.FUNC_SEARCH_FOR_BEDS_MENU['title'], "title " + data['title'] + " is incorrect"
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu")
            self.page_count = data["pageCount"]
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))

    @tag('select_cases')
    @task
    def select_cases(self):
        logging.info("Selecting Random Cases - mobile worker:" + self.user.login_as)
        total_qty_cases_to_select = random.randrange(5,11)
        self.selected_case_ids = set()

        # As is, this doesn't handle if there aren't enough cases to select. Also it won't handle well
        # situations where the ratio of # cases to select: # cases available to select are too high
        # since the same random case could be chosen multiple times. But for our use case, this ratio will be very low
        max_num_iterations = total_qty_cases_to_select
        i = 0
        while len(self.selected_case_ids) < total_qty_cases_to_select:
            random_page_num = random.randrange(0, self.page_count)
            offset = random_page_num * self.cases_per_page

            random_qty_cases_to_select_per_page = random.randrange(1, total_qty_cases_to_select + 1)
            qty_cases_remaining_to_select = total_qty_cases_to_select - len(self.selected_case_ids)
            qty_to_select = min(random_qty_cases_to_select_per_page, qty_cases_remaining_to_select)
            data = self._formplayer_post("navigate_menu", extra_json={
                "selections": [self.FUNC_SEARCH_FOR_BEDS_MENU['selections']],
                "cases_per_page": self.cases_per_page,
                "offset": offset,
            }, name="Paginate for Case Selection", checkKey="title", checkValue=self.FUNC_SEARCH_FOR_BEDS_MENU['title'])

            entities = data["entities"]
            ids = [entity["id"] for entity in entities if entity["id"] not in self.selected_case_ids]
            if len(ids) < qty_to_select:
                self.selected_case_ids.update(ids)
            else:
                for _ in range(qty_to_select):
                    random_case_index = random.randrange(0, len(ids))
                    self.selected_case_ids.add(ids[random_case_index])

            # crude way to avoid looping infinitely
            i += 1
            assert i < max_num_iterations, "exceeded allowed number of iterations to select cases for mobile worker " + self.user.login_as
            rng = random.randrange(1,3)
            time.sleep(rng)
        logging.info("selected cases are " + str(self.selected_case_ids) + " for mobile worker " + self.user.login_as)


    @tag('enter_create_profile_and_refer_form')
    @task
    def enter_create_profile_and_refer_form(self):
        try:
            logging.info("Entering form - mobile worker:" + self.user.login_as)
            data = self._formplayer_post("navigate_menu", extra_json={
                        "selected_values": (list(self.selected_case_ids)),
                        "query_data": {},
                        "selections": [self.FUNC_SEARCH_FOR_BEDS_MENU['selections'], "use_selected_values"],
                    }, name="Enter 'Create Profile and Refer' Form")
            assert "title" in data, "formplayer response does not contain title"
            assert data['title'] == self.FUNC_CREATE_PROFILE_AND_REFER_FORM['title'], "title " + data['title'] + " is incorrect"
            self.session_id = data['session_id']
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: navigate_menu; exception: " + str(e))

    @tag('answer_create_profile_and_refer_form_questions')
    @task
    def answer_create_profile_and_refer_form_questions(self):
        logging.info("Answering Questions - mobile worker:" + self.user.login_as)
        try:
            for question in self.FUNC_CREATE_PROFILE_AND_REFER_FORM_QUESTIONS.values():
                    data = self._formplayer_post("answer", extra_json={
                                "ix": question["ix"],
                                "answer": question["answer"],
                                "session_id": self.session_id,
                            }, name="Answer 'Create Profile and Refer' Question")
                    rng = random.randrange(1,3)
                    time.sleep(rng)
        except Exception as e:
            logging.info(
                "user: " + self.user.username + "; mobile worker: " + self.user.login_as + "; request: answer; exception: " + str(e))

    @tag('submit_create_profile_and_refer_form')
    @task
    def submit_create_profile_and_refer_form(self):
        logging.info("Submitting form - mobile worker:" + self.user.login_as)
        current_time_seconds = time.time()
        utc_time_tuple = time.gmtime(current_time_seconds)
        year = utc_time_tuple.tm_year
        month = utc_time_tuple.tm_mon
        day = utc_time_tuple.tm_mday
        formatted_date = "{:04d}-{:02d}-{:02d}".format(year, month, day)
        answers = {
            "2": "OK",
            "4": "OK",
            "5": None,
            "7": "OK",
            "8": "OK",
            "0,1,0": "OK",
            "0,1,1": 21,
            "0,1,2": 2,
            "0,1,3": formatted_date,
            "0,1,4": "Symptoms encouraged visit",
            "0,1,5": "Inpatient",
            "0,1,6": "NOT HEADACHE",
            "0,1,7": None,
            "0,1,8": None,
            "0,1,9": None,
            "0,1,10": None,
            "0,1,11": None,
            "0,1,12": None,
            "0,1,13": None,
            "0,1,14": None,
            "0,1,15": [1],
            "3_0,2,0,0": "OK",
            "3_0,2,0,1": "OK",
            "3_0,2,0,2": "OK",
            "3_0,2,0,3": "OK",
            "3_0,2,0,4": "OK",
            "3_0,2,0,5": "OK",
            "3_0,3": None
        }
        input_answers= {d["ix"]: d["answer"] for d in self.FUNC_CREATE_PROFILE_AND_REFER_FORM_QUESTIONS.values()}
        answers.update(input_answers)

        data = self._formplayer_post("submit-all", extra_json={
            "answers": answers,
            "prevalidated": True,
            "debuggerEnabled": True,
            "session_id": self.session_id,
        }, name = "Submit Create Profile and Refer Form", checkKey="submitResponseMessage",
                                         checkValue=self.FUNC_CREATE_PROFILE_AND_REFER_FORM_SUBMIT[
                                             'submitResponseMessage'])

    def _formplayer_post(self, command, extra_json=None, name=None, checkKey=None, checkValue=None, checkLen=None):
        json = {
            "app_id": self.user.app_details.build_id,
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

    project = 'bha-referrals-perf'  # str(os.environ.get("project"))

    def on_start(self):
        self.domain = self.environment.parsed_options.domain
        self.host = self.environment.parsed_options.host
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)
        self.user_detail = USERS_DETAILS.pop()
        self.HQ_user = HQUser( self.user_detail)
        self.username = self.user_detail.username
        self.password = self.user_detail.password
        self.login_as = self.user_detail.login_as
        print("userinfo===>>" + str( self.user_detail))

        logging.info("timestamp-->>>" + str(dt_object))
        logging.info("host-->>>" + self.host)
        logging.info("login_as-->>>" + self.login_as)
        logging.info("username-->>>" + self.username)
        logging.info("domain-->>>" + self.domain)

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
