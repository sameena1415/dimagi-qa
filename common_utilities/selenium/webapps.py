from fixtures import TimeoutException
from selenium.webdriver.common.by import By

from common_utilities.selenium.base_page import BasePage

""""Contains common  page elements and functions related to webapps actions"""


def get_element(xpath_format, insert_value):
    element = (By.XPATH, xpath_format.format(insert_value))
    return element


class WebApps(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.app_name_format = "//*[@aria-label='{}']/div"
        self.app_header_format = "//h1[text()='{}']"
        self.menu_name_format = "//*[@aria-label='{}']"
        self.menu_name_header_format = "//*[text()='{}']"
        self.form_name_format = "//tr[@aria-label='{}']"
        self.case_name_format = "//tr[.//td[text()='{}']]"

        self.form_submit = (By.XPATH, "//button[@class='submit btn btn-primary']")
        self.form_submission_successful = (By.XPATH, "//p[contains(text(), 'Form successfully saved')]")
        self.search_all_cases_button = (By.XPATH, "//div[@class='case-list-action-button btn-group formplayer-request']")
        self.clear_case_search_page = (By.ID, "query-clear-button")
        self.submit_on_case_search_page = (By.XPATH, "//button[@type='submit' and @id='query-submit-button']")
        self.case_list = (By.XPATH, "//table[@class='table module-table module-table-case-list']")
        self.omni_search_input = (By.ID, "searchText")
        self.omni_search_button = (By.ID, "case-list-search-button")
        self.continue_button = (By.ID, "select-case")

    def open_app(self, case_search_app_name):
        self.application = get_element(self.app_name_format, case_search_app_name)
        self.application_header = get_element(self.app_header_format, case_search_app_name)
        self.wait_to_click(self.application)
        self.is_visible_and_displayed(self.application_header, timeout=200)

    def open_menu(self, menu_name):
        self.caselist_menu = get_element(self.menu_name_format, menu_name)
        self.caselist_header = get_element(self.menu_name_header_format, menu_name)
        self.wait_to_click(self.caselist_menu)
        assert self.is_visible_and_displayed(self.caselist_header)

    def open_form(self, form_name):
        self.form_name = get_element(self.form_name_format, form_name)
        self.wait_to_click(self.form_name)

    def search_all_cases(self):
        self.wait_to_click(self.search_all_cases_button)

    def search_all_cases_on_case_search_page(self):
        self.wait_to_click(self.clear_case_search_page)
        self.js_click(self.submit_on_case_search_page)
        self.is_visible_and_displayed(self.case_list)

    def omni_search(self, case_name):
        self.wait_to_clear_and_send_keys(self.omni_search_input, case_name)
        self.js_click(self.omni_search_button)
        return case_name

    def select_case(self, case_name):
        self.case = get_element(self.case_name_format, case_name)
        self.wait_to_click(self.case)
        self.js_click(self.continue_button)

    def submit_the_form(self):
        self.js_click(self.form_submit)
        self.is_visible_and_displayed(self.form_submission_successful, timeout=500)


