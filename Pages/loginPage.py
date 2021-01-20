from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "id_auth-username"
        self.password_textbox_id = "id_auth-password"
        self.submit_button_xpath = '//button[@type="submit"]'
        self.alert_button_accept = "hs-eu-confirmation-button"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    def accept_alert(self):
        try:
            self.driver.find_element_by_id(self.alert_button_accept).click()
        except NoSuchElementException:
            pass  # ignore if alert not on page
