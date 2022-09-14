from selenium.webdriver.common.by import By

from common_utilities.selenium.base_page import BasePage

""""Contains test page elements and functions related to the Case Search functionality"""


class CaseSearchWorkflows(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.rating_in_table = (By.XPATH, "//td[@class='module-case-list-column'][4]")
        self.case_name_format = "//tr[.//td[text()='{}']]"

    def check_element_claimed(self, case_name):
        self.case = self.get_element(self.case_name_format, case_name)
        assert self.is_visible_and_displayed(self.case)

    def check_default_rating_on_caselist(self, default_rating):
        ratings = self.find_elements_texts(self.rating_in_table)
        assert default_rating in ratings

