# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time


class UsersMobileWorkersPage:

    def __init__(self, driver):
        self.driver = driver
        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'

    # def open_mobile_worker_page(self):
    #     time.sleep(2)
    #     bool
    #     users_menu_enabled = self.driver.find_element_by_id(self.users_menu_id).is_enabled()
    #     if users_menu_enabled:
    #         self.driver.find_element_by_id(self.users_menu_id).click()
    #         self.driver.find_element_by_link_text(self.mobile_workers_menu_link_text).click()
    #         time.sleep(2)

    def create_mobile_worker(self):
        self.driver.find_element_by_id(self.create_mobile_worker_id).click()

    def mobile_worker_enter_username(self, username):
        self.driver.find_element_by_id(self.mobile_worker_username_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_username_id).send_keys(username)

    def mobile_worker_enter_password(self, password):
        self.driver.find_element_by_id(self.mobile_worker_password_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_password_id).send_keys(password)

    def click_create(self):
        self.driver.find_element_by_xpath(self.create_button_xpath).click()
