from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    UnexpectedAlertPresentException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

"""This class contains all the generic methods and utilities for all workflows"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.alert_button_accept = (By.ID, "hs-eu-confirmation-button")

    def cookie_alert(self):
        try:
            self.cookie_alert_displayed = self.is_displayed(self.alert_button_accept)
        except NoSuchElementException:
            self.cookie_alert_displayed = False
        return self.cookie_alert_displayed

    def wait_to_click(self, locator, timeout=12):
        element = None
        try:
            clickable = ec.element_to_be_clickable(locator)
            element = WebDriverWait(self.driver, timeout).until(clickable,
                                                                        message="Couldn't find locator: "
                                                                                + str(locator))
            element.click()
        except ElementClickInterceptedException:
            if self.cookie_alert():
                self.click(self.alert_button_accept)
                element.click()
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert.accept()
            element.click()
        except StaleElementReferenceException:
            self.js_click(locator)

    def wait_to_clear_and_send_keys(self, locator, user_input):
        clickable = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, 5).until(clickable, message="Couldn't find locator: " + str(locator))
        element.clear()
        element.send_keys(user_input)

    def wait_for_element(self, locator, timeout=20):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable,
                                                  message="Couldn't find locator: " + str(locator))

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def js_click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            is_displayed = element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            is_displayed = False
        return bool(is_displayed)

    def is_visible_and_displayed(self, locator, timeout=120):
        try:
            visible = ec.visibility_of_element_located(locator)
            element = WebDriverWait(self.driver, timeout).until(visible, message="Element" + str(locator) + "not displayed")
            is_displayed = element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            is_displayed = False
        return bool(is_displayed)
