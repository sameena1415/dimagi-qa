import time

from selenium.webdriver.common.by import By
from common_utilities.selenium.base_page import BasePage
from Features.CaseSearch.constants import *

""""Contains test page elements and functions related to the CO BHA App"""


class BhaWorkflows(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.admit_new_client_on_caselist = (By.XPATH, "//button[text()='Admit New Client']")
        self.radio_option_value = "//input[contains(@value,'{}')]"
        self.case_search_properties = (By.XPATH, "//label[@class='control-label']")
        self.continue_button = "//span[@id='multi-select-btn-text' and text()='{}']"
        self.client_info = " (//h2[contains(text(), 'Client Information')]/following::strong[contains(text(),'{}')]//ancestor::li[1])[1]"
        self.combobox_select_clinic = (By.XPATH, "//select[@class='form-control select2-hidden-accessible']")
        self.answer_option_label = "//p[text()='{}']"
        self.question_label = "//span[text()='{}']"
        self.clinic_close_button = "//button[@aria-label='Remove item' and contains(@aria-describedby , '{}')]"
        self.case_list_display_properties = "(//tr[.//th[contains(text(),'{}')]])[1]"
        self.case_prop_value = "//th[@title='{}']/following::td[contains(text(),'{}')]"

    def click_on_admit_new_client(self):
        self.js_click(self.admit_new_client_on_caselist)

    def replace_one_char(self, original_string):
        index = 2
        new_character = "a"
        return original_string[:index] + new_character + original_string[index + 1:]

    def select_radio(self, value):
        radio_value = self.get_element(self.radio_option_value, value)
        self.js_click(radio_value)

    def check_search_properties_present(self, properties):
        properties_labels = self.find_elements_texts(self.case_search_properties)
        for search_property in properties:
            assert search_property in properties_labels

    def expected_count_on_continue_button(self, number):
        count_on_continue = self.get_element(self.continue_button, number)
        assert self.is_displayed(count_on_continue)

    def check_client_info_on_form(self, search_property, search_value):
        value_on_form_xpath = self.get_element(self.client_info, search_property)
        value_on_form = self.get_text(value_on_form_xpath)
        assert search_value in value_on_form

    def select_clinic(self, clinic_name):
        if self.is_displayed(self.combobox_select_clinic):
            self.select_by_text(self.combobox_select_clinic, clinic_name)

    def remove_clinic(self, clinic_name):
        close_xpath = self.get_element(self.clinic_close_button, clinic_name)
        self.js_click(close_xpath)

    def check_answer_options(self, label, displayed=None):
        answer_label = self.get_element(self.answer_option_label, label)
        if displayed == YES:
            assert self.is_displayed(answer_label)
        elif displayed == NO:
            assert not self.is_displayed(answer_label)

    def check_question_label(self, label, displayed=None):
        question_label = self.get_element(self.question_label, label)
        if displayed == YES:
            assert self.is_displayed(question_label)
        elif displayed == NO:
            assert not self.is_displayed(question_label)

    def check_headers_on_case_list(self, display_properties):
        for prop in display_properties:
            header = self.get_element(self.case_list_display_properties, prop)
            assert self.is_displayed(header)

    def check_property_on_case_list_report(self, case_link, case_property, case_property_value):
        self.driver.get(case_link)
        self.locator = (By.XPATH, self.case_prop_value.format(case_property, case_property_value))
        assert self.is_present(self.locator)
