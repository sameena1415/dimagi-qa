from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.user_inputs import UserData


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.available_application = UserData.village_application

        self.dashboard_menu = (By.ID, "DashboardTab")
        self.reports_menu = (By.ID, "ProjectReportsTab")
        self.view_all = (By.LINK_TEXT, "View All")
        self.data_menu = (By.ID, "ProjectDataTab")
        self.users_menu = (By.ID, "ProjectUsersTab")
        self.applications_menu = (By.ID, "ApplicationsTab")
        self.web_apps_menu = (By.ID, "CloudcareTab")
        self.show_full_menu = (By.ID, "commcare-menu-toggle")
        self.messaging_menu = (By.ID, "MessagingTab")
        self.admin_menu = (By.ID, "AdminTab")
        self.alert_button_accept = (By.ID, "hs-eu-confirmation-button")

    def dashboard_menu(self):
        try:
            self.wait_to_click(self.dashboard_menu)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.dashboard_menu)
        assert "CommCare HQ" == self.driver.title, "This is not the Dashboard page."

    def reports_menu(self):
        try:
            self.wait_to_click(self.reports_menu)
            self.wait_to_click(self.view_all)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.reports_menu)
                self.wait_to_click(self.view_all)
        assert "My Saved Reports : Project Reports :: - CommCare HQ" in self.driver.title, "This is not the Reports menu page."

    def data_menu(self):
        try:
            self.wait_to_click(self.data_menu)
            self.wait_to_click(self.view_all)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.data_menu)
                self.wait_to_click(self.view_all)
        assert "Export Form Data : Data :: - CommCare HQ" in self.driver.title, "This is not the Data menu page."

    def applications_menu(self):
        try:
            self.wait_to_click(self.applications_menu)
            self.wait_to_click(self.available_application)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.applications_menu)
                self.wait_to_click(self.available_application)
        assert "Releases - " + UserData.village_application + " - CommCare HQ" in self.driver.title, "This is not the Applications page."

    def users_menu(self):
        try:
            self.wait_to_click(self.users_menu)
            self.wait_to_click(self.view_all)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.users_menu)
                self.wait_to_click(self.view_all)
        assert "Mobile Workers : Users :: - CommCare HQ" in self.driver.title, "This is not the Users menu page."

    def messaging_menu(self):
        try:
            self.wait_to_click(self.messaging_menu)
            self.wait_to_click(self.view_all)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.messaging_menu)
                self.wait_to_click(self.view_all)
        assert "Dashboard : Messaging :: - CommCare HQ" in self.driver.title, "This is not the Messaging menu page."

    def web_apps_menu(self):
        try:
            self.wait_to_click(self.web_apps_menu)
            self.wait_to_click(self.show_full_menu)
        except ElementClickInterceptedException:
            if self.is_visible_and_displayed(self.alert_button_accept):
                self.click(self.alert_button_accept)
                self.wait_to_click(self.web_apps_menu)
                self.wait_to_click(self.show_full_menu)
        assert "Web Apps - CommCare HQ" in self.driver.title, "This is not the Webaspps menu page."
