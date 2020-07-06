import time

from selenium.common.exceptions import InvalidSelectorException


class MobileWorkerPage:

    def __init__(self, driver):
        self.driver = driver
        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'

    def mobile_worker_menu(self):
        bool
        users_menu_enabled = self.driver.find_element_by_id(self.users_menu_id).is_enabled()
        if users_menu_enabled:
            self.driver.find_element_by_id(self.users_menu_id).click()
            self.driver.find_element_by_link_text(self.mobile_workers_menu_link_text).click()
            time.sleep(2)

    def create_mobile_worker(self):
        self.driver.find_element_by_id(self.create_mobile_worker_id).click()
        time.sleep(2)

    def mobile_worker_enter_username(self, username):
        self.driver.find_element_by_id(self.mobile_worker_username_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_username_id).send_keys(username)
        time.sleep(2)

    def mobile_worker_enter_password(self, password):
        self.driver.find_element_by_id(self.mobile_worker_password_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_password_id).send_keys(password)
        time.sleep(2)

    def click_create(self):
        bool
        create_button_enabled = self.driver.find_element_by_id(self.create_button_xpath).is_enabled()
        if create_button_enabled:
            self.driver.find_element_by_xpath(self.create_button_xpath).click()
            time.sleep(2)
