import logging

from locust import HttpUser, SequentialTaskSet, between, events, tag, task
from locust.exception import InterruptTaskSet

from common.args import file_path
from common.utils import load_json_data
from common.web_apps import get_app_build_info
from user.models import AppDetails, HQUser, UserDetails


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--domain", help="CommCare domain", required=True, env_var="COMMCARE_DOMAIN")
    parser.add_argument("--app-id", help="CommCare app id", required=True, env_var="COMMCARE_APP_ID")
    parser.add_argument("--app-config", help="Configuration of CommCare app", required=True)
    parser.add_argument("--user-details", help="Path to user details file", required=True)


APP_CONFIG = {}
USERS_DETAILS = []


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


class WorkloadModelSteps(SequentialTaskSet):
    wait_time = between(5, 15)

    def on_start(self):
        # get domain user credential and app config info
        self.FUNC_HOME_SCREEN = APP_CONFIG['FUNC_HOME_SCREEN']
        self.FUNC_SEARCH_FOR_BEDS_MENU = APP_CONFIG['FUNC_SEARCH_FOR_BEDS_MENU']
        self.FUNC_ENTER_AGE = APP_CONFIG['FUNC_ENTER_AGE']
        self.FUNC_GENDER_IDENTITY = APP_CONFIG['FUNC_GENDER_IDENTITY']
        self.FUNC_INVOLUNTARY_CLIENT = APP_CONFIG['FUNC_INVOLUNTARY_CLIENT']
        self.FUNC_JUSTICE_INVOLVED_CLIENT = APP_CONFIG['FUNC_JUSTICE_INVOLVED_CLIENT']
        self.FUNC_CARE_TYPE = APP_CONFIG['FUNC_CARE_TYPE']
        self.FUNC_FACILITY_NAME = APP_CONFIG['FUNC_FACILITY_NAME']
        self.FUNC_RESIDENTIAL_SERVICE = APP_CONFIG['FUNC_RESIDENTIAL_SERVICE']
        self.FUNC_POPULATION_SPECIALTY = APP_CONFIG['FUNC_POPULATION_SPECIALTY']
        self.FUNC_INSURANCE_ACCEPTED = APP_CONFIG['FUNC_INSURANCE_ACCEPTED']
        self.FUNC_ACCOMMODATIONS = APP_CONFIG['FUNC_ACCOMMODATIONS']
        self.FUNC_LANGUAGE_SERVICES = APP_CONFIG['FUNC_LANGUAGE_SERVICES']
        self.FUNC_OPEN_BEDS = APP_CONFIG['FUNC_OPEN_BEDS']
        self.FUNC_PERFORM_A_SEARCH = APP_CONFIG['FUNC_PERFORM_A_SEARCH']

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
        self.user.hq_user.navigate_start(self.user, expected_title=self.FUNC_HOME_SCREEN['title'])

    @tag('search_for_beds_menu')
    @task
    def search_for_beds_menu(self):
        data = {"selections": [self.FUNC_SEARCH_FOR_BEDS_MENU['selections']]}
        self.user.hq_user.navigate(
            "Open Search for Beds Menu",
            self.user, data=data, expected_title=self.FUNC_SEARCH_FOR_BEDS_MENU['title']
        )

    @tag('perform_a_search')
    @task
    def perform_a_search(self):
        for i in range(0, 20):
            data = {
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
            }
            self.user.hq_user.navigate("Perform a Search", self.user, data=data)

    @task
    def stop(self):
        logging.info("stopping - mobile worker: " + self.user.user_detail.login_as)
        self.interrupt()

    def _formplayer_post(self, command, name, data=None, validation=None):
        return self.user.post_formplayer(
            command,
            self.client,
            self.user.app_details,
            extra_json=data,
            name=name,
            validation=validation
        )


class LoginCommCareHQWithUniqueUsers(HttpUser):
    tasks = [WorkloadModelSteps]

    def on_start(self):
        self.domain = self.environment.parsed_options.domain
        self.host = self.environment.parsed_options.host
        self.user_detail = USERS_DETAILS.pop()
        self.hq_user = HQUser(self.user_detail)
        logging.info("userinfo-->>>" + str(self.user_detail))

        self.login()
        self.app_details = AppDetails(
            domain=self.domain,
            app_id=self.environment.parsed_options.app_id,
            build_id=self._get_build_info(self.environment.parsed_options.app_id)
        )

    def login(self):
        self.hq_user.login(self.domain, self.host, self.client)

    def _get_build_info(self, app_id):
        build_id = get_app_build_info(self.client, self.domain, app_id)
        if build_id:
            logging.info("Using app build: %s", build_id)
        else:
            logging.warning("No build found for app: %s", app_id)
        return build_id
