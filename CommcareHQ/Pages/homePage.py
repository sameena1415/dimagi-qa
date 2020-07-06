from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_menu_id = "DashboardTab"
        self.reports_menu_id = "ProjectReportsTab"
        self.reports_view_all_linkedtext = "View All"
        self.applications_menu_id = "ApplicationsTab"
        self.applications_menu_new_application = "New Application"

        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'


    def dashboard_menu(self):
        bool
        dashboard_menu_enabled = self.driver.find_element_by_id(self.dashboard_menu_id).is_enabled()
        if dashboard_menu_enabled:
            self.driver.find_element_by_id(self.dashboard_menu_id).click()

    def reports_menu(self):
        bool
        reports_menu_enabled = self.driver.find_element_by_id(self.reports_menu_id).is_enabled()
        if reports_menu_enabled:
            self.driver.find_element_by_id(self.reports_menu_id).click()
            self.driver.find_element_by_link_text(self.reports_view_all_linkedtext).click()
            time.sleep(2)

    def applications_menu(self):
        bool
        applications_menu_enabled = self.driver.find_element_by_id(self.applications_menu_id).is_enabled()
        if applications_menu_enabled:
            self.driver.find_element_by_id(self.applications_menu_id).click()
            self.driver.find_element_by_link_text(self.applications_menu_new_application).click()
            time.sleep(2)


