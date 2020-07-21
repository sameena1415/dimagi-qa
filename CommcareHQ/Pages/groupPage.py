import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs
from selenium.webdriver.support import expected_conditions as EC


class GroupPage:

    def __init__(self, driver):
        self.driver = driver
        self.group_name_id = "id_group_name"
        self.add_group_button = "//button[@type='submit' and @class='btn btn-primary']"
        self.group_menu_xpath = "//a[@data-title='Groups']"
        self.users_drop_down_xpath = "//span[@class='selection']"
        self.select_user_xpath = "//li[text()='"+UserInputs.mobile_worker_username+"']"
        self.update_button_id = "submit-id -submit"

    def click_group_menu(self):
        self.driver.find_element_by_xpath(self.group_menu_xpath).click()
        time.sleep(2)

    def enter_group_name(self, groupname):
        time.sleep(2)
        self.driver.find_element_by_id(self.group_name_id).send_keys(groupname)
        time.sleep(2)

    def add_group(self):
        time.sleep (2)
        self.driver.find_element_by_xpath(self.add_group_button).click()
        time.sleep(2)

    def click_on_users_dropdown(self):
        self.driver.find_element_by_xpath(self.users_drop_down_xpath).click()
        time.sleep(2)

    def add_user_to_group(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.select_user_xpath).click()
        time.sleep(2)

    def update_group(self):
        self.driver.find_element_by_id(self.update_button_id).click()
        time.sleep(2)

    def edit_existing_group(self):
        self.click_group_menu()
        self.driver.find_element_by_link_text(UserInputs.group_name).click()








