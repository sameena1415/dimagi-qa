import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from PerformanceTests.NY_CICT_App_Sprint.WorkflowActions.base.base_page import BasePage
from PerformanceTests.NY_CICT_App_Sprint.UserInputs.user_inputs import UserData

""""Contains test page elements and functions related to workflows in test"""


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.app_settings = (By.XPATH, "//div[@class='js-settings appicon appicon-settings']")
        self.break_pending_locks = (By.XPATH, "//button[contains(@class,'js-break-locks btn btn-sm btn-danger')]")
        self.lock_exists = (By.XPATH, "//div[contains(text(),'existed')]")
        self.clear_user_data = (By.XPATH, "//button[contains(@class,'js-clear-user-data btn btn-sm btn-danger')]")
        self.clear_user_data_success = (By.XPATH, "//div[text()='User data successfully cleared.'][last()]")
        self.done = (By.XPATH, "//button[contains(@class,'btn btn-primary js-done')]")
        self.sync_app = (By.XPATH, "//div[@class='js-sync-item appicon appicon-sync']")
        self.sync_success = (By.XPATH, "(//div[text()='User Data successfully synced.'])[last()]")
        self.login_as = (By.CSS_SELECTOR, ".js-restore-as-item")
        self.search_user = (By.XPATH, "//input[@class='js-user-query form-control']")
        self.search_confirm = (By.XPATH, "//button[@type ='submit' and @class= 'btn btn-default']")
        self.confirm_user_login = (By.XPATH, "//button[@id = 'js-confirmation-confirm']")
        self.all_cases_menu = (By.XPATH, "(//div[@aria-label='All Cases']/div)[1]")
        self.case_list_table = (By.XPATH, "//table[@class='table module-table module-table-case-list']")
        self.preconfig_case = (By.XPATH, "//tr[.//td[text()='" + UserData.pre_configured_case +
                               "' and @class='module-case-list-column']]")
        self.preconfig_contact = (By.XPATH, "//tr[.//td[text()='" + UserData.pre_configured_contact +
                                  "' and @class='module-case-list-column']]")
        self.case_detail_modal = (By.XPATH, "//div[@id='case-detail-modal']//div[@class='modal-content']")
        self.continue_button = (By.ID, "select-case")
        self.menu_list = (By.XPATH, "//div[@class='module-menu-container']")
        self.ci_form = (By.XPATH, "//tr[@aria-label='Case Investigation']")
        self.form_content = (By.ID, "webforms")
        self.name_of_school_dropdown = (By.XPATH, "(//*[contains(text(),'Name of university')])[1]"
                                                  "/following::span[@class='select2-selection__rendered'][1]")
        self.search_dropdown = (By.XPATH, "//span[@class='select2-search select2-search--dropdown']")
        self.school_search = random.choice(UserData.school_list)
        self.name_of_school_answer = (
        By.XPATH, "//span[@class='select2-results']//ul//li[contains(text(),'" + self.school_search + "')][1]")
        self.school_selected_displayed = (By.XPATH, "//span[contains(text(), '" + self.school_search + "')]")
        self.submit_form = (By.XPATH, "//button[@type='submit' and @class='submit btn btn-primary']")
        self.form_submission_success = (By.XPATH, "//p[text()='Form successfully saved!']")
        self.all_contacts_menu = (By.XPATH, "(//div[@aria-label='All Contacts']/div)[1]")
        self.preconfig_contact = (By.XPATH, "//tr[.//td[text()='" + UserData.pre_configured_contact +
                                  "' and @class='module-case-list-column']]")
        self.cm_form = (By.XPATH, "//tr[@aria-label='Contact Monitoring']")
        self.search_case_list = (By.ID, "searchText")
        self.search_button = (By.ID, "case-list-search-button")
        self.webapps_home = (By.XPATH, "//a[@href='/a/" + UserData.project_space + "/cloudcare/apps/v2/' and @class='navbar-brand']")
        self.use_web_user = (By.XPATH, "//a[@class='js-clear-user']")

    def break_locks_and_clear_user_data(self):
        try:
            self.wait_to_click(self.app_settings)
        except TimeoutException:
            self.wait_to_click(self.webapps_home)
            self.wait_to_click(self.app_settings)
        self.wait_to_click(self.break_pending_locks)
        if self.is_displayed(self.lock_exists):
            time.sleep(180)
        self.wait_to_click(self.clear_user_data)
        assert self.is_visible_and_displayed(self.clear_user_data_success)
        self.wait_to_click(self.done)
        self.wait_to_click(self.webapps_home)

    def login_as_ci_ct_user(self, username, url):
        self.ci_ct_user = (By.XPATH, "//b[contains(text(),'" + username + "')]")
        user_restore = url + "#restore_as/1/" + username
        self.driver.get(user_restore)
        time.sleep(3)
        self.js_click(self.ci_ct_user)
        self.wait_to_click(self.confirm_user_login)
        assert self.is_visible_and_displayed(self.ci_ct_user)

    @timer
    def sync_application(self, username, application_name):
        self.wait_to_click(self.sync_app)
        assert self.sync_successful_is_visible_and_displayed(self.sync_success)

    @timer
    def open_application(self, application_name, username):
        self.pre_application = (By.XPATH, '//div[contains(@aria-label,"' + application_name + '")]')
        self.app_name_in_breadcrumb = (By.XPATH, "//ol//li[contains(.,'" + application_name + "')]")
        self.wait_to_click(self.pre_application)
        assert self.is_visible_and_displayed(self.app_name_in_breadcrumb)

    @timer
    def all_cases_menu_load(self, application_name, username):
        self.wait_to_click(self.all_cases_menu)
        assert self.is_visible_and_displayed(self.case_list_table)

    def search_case_in_test(self, application_name, username):
        self.wait_to_clear_and_send_keys(self.search_case_list, UserData.pre_configured_case)
        self.wait_to_click(self.search_button)
        time.sleep(20)
        assert self.is_visible_and_displayed(self.preconfig_case)

    @timer
    def open_case_detail(self, application_name, username):
        self.js_click(self.preconfig_case)
        assert self.is_visible_and_displayed(self.case_detail_modal)

    @timer
    def case_menu_display(self, application_name, username):
        self.wait_to_click(self.continue_button)
        assert self.is_visible_and_displayed(self.menu_list)

    @timer
    def open_case_investigation_form(self, application_name, username):
        self.wait_to_click(self.ci_form)
        assert self.is_visible_and_displayed(self.form_content)

    @timer
    def ci_form_answer_question(self, application_name, username):
        self.scroll_to_element(self.name_of_school_dropdown)
        self.driver.execute_script("window.scrollBy(0,-80)")
        self.wait_to_click(self.name_of_school_dropdown)
        self.wait_to_click(self.name_of_school_answer)
        assert self.is_visible_and_displayed(self.school_selected_displayed)

    @timer
    def ci_form_submission(self, application_name, username):
        self.js_click(self.submit_form)
        assert self.is_visible_and_displayed(self.form_submission_success)

    def app_home_screen(self, app_in_test):
        self.app_home = (By.XPATH, "//ol//li[contains(.,'" + app_in_test + "')]")
        self.wait_to_click(self.app_home)

    @timer
    def all_contacts_menu_load(self, application_name, username):
        self.js_click(self.all_contacts_menu)
        assert self.is_visible_and_displayed(self.case_list_table)

    def search_contact_in_test(self, application_name, username):
        self.wait_to_clear_and_send_keys(self.search_case_list, UserData.pre_configured_contact)
        self.wait_to_click(self.search_button)
        time.sleep(20)
        assert self.is_visible_and_displayed(self.preconfig_contact)

    @timer
    def open_contact_detail(self, application_name, username):
        self.wait_to_click(self.preconfig_contact)
        assert self.is_visible_and_displayed(self.case_detail_modal)

    @timer
    def contact_menu_display(self, application_name, username):
        self.wait_to_click(self.continue_button)
        assert self.is_visible_and_displayed(self.menu_list)

    @timer
    def open_contact_monitoring_form(self, application_name, username):
        self.wait_to_click(self.cm_form)
        assert self.is_visible_and_displayed(self.form_content)

    @timer
    def cm_form_answer_question(self, application_name, username):
        self.scroll_to_element(self.name_of_school_dropdown)
        self.driver.execute_script("window.scrollBy(0,-80)")
        self.wait_to_click(self.name_of_school_dropdown)
        self.wait_to_click(self.name_of_school_answer)
        assert self.is_visible_and_displayed(self.school_selected_displayed)

    @timer
    def cm_form_submission(self, application_name, username):
        self.js_click(self.submit_form)
        assert self.is_visible_and_displayed(self.form_submission_success)

    def back_to_webapps_home(self):
        self.wait_to_click(self.webapps_home)
        self.wait_for_element(self.use_web_user)
        self.js_click(self.use_web_user)
        assert not self.is_displayed(self.use_web_user)
