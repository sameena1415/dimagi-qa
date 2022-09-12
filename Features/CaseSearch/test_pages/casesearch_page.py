from selenium.webdriver.common.by import By

from common_utilities.selenium.base_page import BasePage

""""Contains test page elements and functions related to the Homepage of Commcare"""


class CaseSearchWorkflows(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username_in_table = (By.XPATH, "//td[@class='module-case-list-column'][last()]")
        self.case_name_format = "//tr[.//td[text()='{}']]"

    # def get_usernames_on_caselist(self, logged_in_user):
    #     usernames = self.find_elements_texts(self.username_in_table)
    #     assert logged_in_user in usernames

    def check_element_claimed(self, case_name):
        self.case = self.get_element(self.case_name_format, case_name)
        assert self.is_visible_and_displayed(self.case)


