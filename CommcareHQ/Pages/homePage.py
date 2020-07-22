from selenium.webdriver.common.by import By
import time


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
        self.driver.find_element(By.ID, self.dashboard_menu_id).click()
        time.sleep(2)

    def reports_menu(self):
        self.driver.find_element(By.ID, self.reports_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)

    def data_menu(self):
        self.driver.find_element(By.ID, self.data_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)

    def applications_menu(self):
        self.driver.find_element(By.ID, self.applications_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.new_application_link_text).click()
        time.sleep(2)

    def users_menu(self):
        self.driver.find_element(By.ID, self.users_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)

    def web_apps_menu(self):
        self.driver.find_element(By.ID, self.web_apps_menu_id).click()
        time.sleep (2)
        self.driver.find_element(By.ID, self.show_full_menu_id).click()
        time.sleep (2)


        time.sleep(2)

    def messaging_menu(self):
        self.driver.find_element(By.ID, self.messaging_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)

    def admin_menu(self):
        self.driver.find_element(By.ID, self.admin_menu_id).click()
        self.driver.find_element(By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)
