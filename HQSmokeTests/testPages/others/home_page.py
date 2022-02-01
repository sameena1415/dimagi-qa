from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from HQSmokeTests.userInputs.userInputsData import UserInputsData


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_menu_id = "DashboardTab"
        self.reports_menu_id = "ProjectReportsTab"
        self.view_all_link_text = "View All"
        self.data_menu_id = "ProjectDataTab"
        self.users_menu_id = "ProjectUsersTab"
        self.applications_menu_id = "ApplicationsTab"
        self.available_application = UserInputsData.application
        self.web_apps_menu_id = "CloudcareTab"
        self.show_full_menu_id = "commcare-menu-toggle"
        self.messaging_menu_id = "MessagingTab"
        self.admin_menu_id = "AdminTab"
        self.alert_button_accept = "hs-eu-confirmation-button"

    def wait_to_click(self, *locator, timeout=5):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def dashboard_menu(self):
        try:
            self.wait_to_click(By.ID, self.dashboard_menu_id)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.dashboard_menu_id)
        assert "CommCare HQ" == self.driver.title, "This is not the Dashboard page."

    def reports_menu(self):
        try:
            self.wait_to_click(By.ID, self.reports_menu_id)
            self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.reports_menu_id)
                self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        assert "My Saved Reports : Project Reports :: - CommCare HQ" in self.driver.title, "This is not the Reports menu page."

    def data_menu(self):
        try:
            self.wait_to_click(By.ID, self.data_menu_id)
            self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.data_menu_id)
                self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        assert "Export Form Data : Data :: - CommCare HQ" in self.driver.title, "This is not the Data menu page."

    def applications_menu(self):
        try:
            self.wait_to_click(By.ID, self.applications_menu_id)
            self.wait_to_click(By.LINK_TEXT, self.available_application)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.applications_menu_id)
                self.wait_to_click(By.LINK_TEXT, self.available_application)
        assert "Releases - " + UserInputsData.application + " - CommCare HQ" in self.driver.title, "This is not the Applications page."

    def users_menu(self):
        try:
            self.wait_to_click(By.ID, self.users_menu_id)
            self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.users_menu_id)
                self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        assert "Mobile Workers : Users :: - CommCare HQ" in self.driver.title, "This is not the Users menu page."

    def messaging_menu(self):
        try:
            self.wait_to_click(By.ID, self.messaging_menu_id)
            self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.messaging_menu_id)
                self.wait_to_click(By.LINK_TEXT, self.view_all_link_text)
        assert "Dashboard : Messaging :: - CommCare HQ" in self.driver.title, "This is not the Messaging menu page."

    def web_apps_menu(self):
        try:
            self.wait_to_click(By.ID, self.web_apps_menu_id)
            self.wait_to_click(By.ID, self.show_full_menu_id)
        except ElementClickInterceptedException:
            if self.driver.find_element(By.ID, self.alert_button_accept).is_displayed():
                self.driver.find_element(By.ID, self.alert_button_accept).click()
                self.wait_to_click(By.ID, self.web_apps_menu_id)
                self.wait_to_click(By.ID, self.show_full_menu_id)
        assert "Web Apps - CommCare HQ" in self.driver.title, "This is not the Webaspps menu page."
