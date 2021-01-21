from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    # self represents the instance of the class. By using the "self" keyword we can access the attributes and methods
    # of the class in python.__init__ is used when an object is created from the class and it allow the class to
    # initialize the attributes of a class.

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_menu_id = "DashboardTab"
        self.reports_menu_id = "ProjectReportsTab"
        self.view_all_link_text = "View All"
        self.data_menu_id = "ProjectDataTab"
        self.users_menu_id = "ProjectUsersTab"
        self.applications_menu_id = "ApplicationsTab"
        self.new_application_link_text = "New Application"
        self.web_apps_menu_id = "CloudcareTab"
        self.show_full_menu_id = "commcare-menu-toggle"
        self.messaging_menu_id = "MessagingTab"
        self.admin_menu_id = "AdminTab"

    def dashboard_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.dashboard_menu_id))).click()

    def reports_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.reports_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.LINK_TEXT, self.view_all_link_text))).click()

    def data_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.data_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.LINK_TEXT, self.view_all_link_text))).click()

    def applications_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.applications_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.LINK_TEXT, self.new_application_link_text))).click()

    def users_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.users_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.LINK_TEXT, self.view_all_link_text))).click()

    def web_apps_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.web_apps_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.show_full_menu_id))).click()

    def messaging_menu(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.ID, self.messaging_menu_id))).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((
            By.LINK_TEXT, self.view_all_link_text))).click()

    # def admin_menu(self):
    #     self.driver.find_element(By.ID, self.admin_menu_id).click()
    #     self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
