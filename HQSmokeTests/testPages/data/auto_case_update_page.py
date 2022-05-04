from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.testPages.base.base_page import BasePage

""""Contains test page elements and functions related to automatic case update module"""


class AutoCaseUpdatePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.rule_name = "rule " + str(fetch_random_string())
        self.rule_created = "//a/strong[text()='" + self.rule_name + "']"

        self.auto_case_update_link = (By.LINK_TEXT, 'Automatically Update Cases')
        self.add_rule_button = (By.ID, 'add-new')
        self.add_rule_name = (By.ID, "id_rule-name")
        self.case_type = (By.ID, "id_criteria-case_type")
        self.case_type_option_value = (By.XPATH, "//option[@value='pregnancy']")
        self.rule_save = (By.XPATH, "//button[@class='btn btn-primary' and text()='Save']")
        self.add_action = (By.XPATH, "(//button[@ data-toggle='dropdown'])[3]")
        self.close_case = (By.XPATH, "//li[@data-bind=\"click: function() { addAction('close-case-action'); }\"]")
        self.rule_created_path = (By.XPATH, self.rule_created)
        self.delete_rule = (By.XPATH, self.rule_created + "//following::button[@class='btn btn-danger'][1]")
        self.delete_confirm = (By.XPATH, self.rule_created + "//following::button[@class='btn btn-danger delete-item-confirm'][1]")

    def open_auto_case_update_page(self):
        self.wait_to_click(self.auto_case_update_link)

    def add_new_rule(self):
        self.wait_to_click(self.add_rule_button)
        self.send_keys(self.add_rule_name, self.rule_name)
        self.wait_to_click(self.case_type)
        self.wait_to_click(self.case_type_option_value)
        self.wait_to_click(self.add_action)
        self.wait_to_click(self.close_case)
        self.wait_to_click(self.rule_save)
        assert self.is_present_and_displayed(self.rule_created_path)
        print("New Rule to Update Cases created successfully!")

    def remove_rule(self):
        self.open_auto_case_update_page()
        self.wait_to_click(self.delete_rule)
        self.wait_to_click(self.delete_confirm)
        self.driver.refresh()
        try:
            isPresent = self.is_visible_and_displayed(self.rule_created_path)
        except (TimeoutException, NoSuchElementException):
            isPresent = False
        assert not isPresent
        print("Rule removed successfully!")
