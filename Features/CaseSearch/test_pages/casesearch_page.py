from selenium.webdriver.common.by import By

from common_utilities.selenium.base_page import BasePage
from common_utilities.selenium.webapps import WebApps

""""Contains test page elements and functions related to the Homepage of Commcare"""


class CaseSearchWorkflows(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # self.dashboard_menu_id = (By.ID, "DashboardTab")

    def test(self, driver):
        print("test")

