from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:

    # self represents the instance of the class. By using the "self" keyword we can access the attributes and methods
    # of the class in python.__init__ is used when an object is created from the class and it allow the class to
    # initialize the attributes of a class.

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_menu_id = "DashboardTab"
        self.reports_menu_id = "ProjectReportsTab"
        self.reports_view_all_linkedtext = "View All"
        self.applications_menu_id = "ApplicationsTab"
        self.applications_menu_new_application = "New Application"
        self.users_menu_id = "ProjectUsersTab"


    def dashboard_menu(self):
        dashboard_menu = self.driver.find_element_by_id(self.dashboard_menu_id)
        if dashboard_menu.is_enabled():
            try:
                dashboard_menu.click()
                time.sleep(2)
            except Exception as e:
                print(e)

    def reports_menu(self):
        report_menu = self.driver.find_element_by_id(self.reports_menu_id)
        if report_menu.is_enabled():
            try:
                report_menu.click()
                time.sleep(2)
                self.driver.find_element_by_link_text (self.reports_view_all_linkedtext).click()
            except Exception as e:
                print(e)

    def applications_menu(self):
        applications_menu = self.driver.find_element_by_id(self.applications_menu_id)
        if applications_menu.is_enabled():
            try:
                applications_menu.click()
                self.driver.find_element_by_link_text(self.applications_menu_new_application).click()
                time.sleep(2)
            except Exception as e:
                print(e)

