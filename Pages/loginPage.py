from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "id_auth-username"
        self.password_textbox_id = "id_auth-password"
        self.submit_button_xpath = '//button[@type="submit"]'
        self.alert_button_accept = "hs-eu-confirmation-button"
        self.continue_button_xpath = '//button[@class="btn btn-primary btn-lg" and @type ="button"]'

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def click_continue(self):
        try:
            self.driver.find_element_by_xpath(self.continue_button_xpath).click()
        except (NoSuchElementException, ElementNotInteractableException):
            print("Non SSO workflow")

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((
                By.ID, self.alert_button_accept))).click()
        except TimeoutException:
            pass  # ignore if alert not on page
