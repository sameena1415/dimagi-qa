import time

from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.user_inputs import UserData
from selenium.common.exceptions im
""""Contains test page elements and functions related to the Manage Forms module"""


class ManageFormsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.manage_forms_link = (By.XPATH, '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a')
        self.select_app_dropdown = (By.ID, 'report_filter_form_app_id')
        self.basic_tests_app = (By.XPATH, "//option[text()='Basic Tests']")
        self.apply_button = (By.XPATH, '//*[@id="apply-btn"]')
        self.select_all_checkbox = (By.XPATH, "//input[@name='select_all']")
        self.first_form_checkbox = (By.XPATH, "(//input[@type='checkbox' and @name='xform_ids'])[1]")
        self.checkbox1 = (By.XPATH, "//*[@id='form_options']//*[@type='checkbox']")
        self.archive_button = (By.XPATH, '//*[@id="submitForms"]')
        self.success_message = (By.XPATH, "//div[@class='alert alert-success']")
        self.view_form_link = (By.XPATH, "//a[@class='ajax_dialog']")
        self.archived_restored_dropdown = (By.XPATH, '//*[@id="select2-report_filter_archive_or_restore-container"]')
        self.archived_forms_option = (By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
        self.manage_forms_return = (By.XPATH, '//span[contains(text(),"Return to")]/a[.="Manage Forms"]')
        self.apply = (By.XPATH, "//button[@class='applyBtn btn btn-sm btn-primary']")
        self.date_range_manage_forms = (By.ID, "filter_range")
        self.village_app = (By.XPATH, "//option[text()='Village Health']")

    def get_normal_forms(self):
        self.wait_and_sleep_to_click(self.manage_forms_link)
        self.wait_and_sleep_to_click(self.select_app_dropdown)
        self.wait_and_sleep_to_click(self.basic_tests_app)
        # Date Filter
        self.wait_and_sleep_to_click(self.date_range_manage_forms)
        self.clear(self.date_range_manage_forms)
        self.send_keys(self.date_range_manage_forms, UserData.date_having_submissions)
        self.wait_and_sleep_to_click(self.apply)
        # Report Apply
        self.wait_and_sleep_to_click(self.apply_button)
        time.sleep(5)

    def view_normal_form(self):
        self.wait_and_sleep_to_click(self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("normal_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    def achieve_forms(self):
        self.wait_and_sleep_to_click(self.first_form_checkbox)
        self.wait_and_sleep_to_click(self.archive_button)
        assert self.is_present_and_displayed(self.success_message)
        print("Forms archival successful!!")
        time.sleep(3)

    def get_archieved_forms(self):
        self.wait_and_sleep_to_click(self.manage_forms_link)
        self.wait_and_sleep_to_click(self.select_app_dropdown)
        self.wait_and_sleep_to_click(self.basic_tests_app)
        self.wait_and_sleep_to_click(self.archived_restored_dropdown)
        self.wait_and_sleep_to_click(self.archived_forms_option)
        self.wait_and_sleep_to_click(self.apply_button)
        self.driver.refresh()

    def view_archieved_forms(self):
        self.wait_and_sleep_to_click(self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("archived_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    def restore_forms(self):
        self.wait_and_sleep_to_click(self.first_form_checkbox)
        self.wait_and_sleep_to_click(self.archive_button)
        assert self.is_present_and_displayed(self.success_message)
        print("Forms Restoration successful!!")
        try:

        except IndexError: