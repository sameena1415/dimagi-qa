import time
import datetime
import logging
from functools import wraps

from dateutil.parser import parse
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException, UnexpectedAlertPresentException,
    StaleElementReferenceException, NoSuchElementException, JavascriptException,
    ElementNotInteractableException, WebDriverException
)

from common_utilities.path_settings import PathSettings

logger = logging.getLogger(__name__)


def retry_on_stale(retries=2, delay=0.5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except StaleElementReferenceException:
                    time.sleep(delay)
            raise
        return wrapper
    return decorator


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.alert_button_accept = (By.ID, "hs-eu-confirmation-button")
        self.error_404 = (By.XPATH, "//h1[contains(text(),'404')]")
        self.error_403 = (By.XPATH, "//h1[text()='403 Forbidden']")

    def wait_until(self, condition, timeout=10, message=None):
        return WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(condition, message=message)

    def page_404(self):
        return self.is_displayed(self.error_404)

    def page_403(self):
        return self.is_displayed(self.error_403)

    def cookie_alert(self):
        return self.is_displayed(self.alert_button_accept)

    @retry_on_stale()
    def wait_to_click(self, locator, timeout=30):
        try:
            element = self.wait_until(ec.element_to_be_clickable(locator), timeout, f"Couldn't click: {locator}")
            element.click()
        except UnexpectedAlertPresentException:
            self.driver.switch_to.alert.accept()
            self.wait_until(ec.element_to_be_clickable(locator), timeout).click()
        except TimeoutException:
            self.wait_for_element(locator)
            if self.page_403() or self.page_404():
                self.driver.back()
                self.wait_until(ec.element_to_be_clickable(locator), timeout).click()
            else:
                raise
        except Exception:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
        self.wait_after_interaction()

    def wait_for_element(self, locator, timeout=10):
        try:
            self.wait_until(ec.presence_of_element_located(locator), timeout, f"Couldn't find: {locator}")
        except (StaleElementReferenceException, TimeoutException):
            self.wait_after_interaction()
            self.wait_until(ec.presence_of_element_located(locator), timeout, f"Couldn't find: {locator}")
        self.wait_after_interaction()

    def wait_to_clear_and_send_keys(self, locator, user_input, timeout=10):
        try:
            element = self.wait_until(ec.visibility_of_element_located(locator), timeout, f"Couldn't find: {locator}")
            element.clear()
            element.send_keys(user_input)
        except Exception as e:
            logger.error(f"[wait_to_clear_and_send_keys] Failed on {locator}: {e}")
            raise

    def click(self, locator):
        try:
            self.driver.find_element(*locator).click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*locator))
        self.wait_after_interaction()
        time.sleep(1)

    def send_keys(self, locator, user_input, timeout=10):
        try:
            element = self.wait_until(ec.element_to_be_clickable(locator), timeout, f"Couldn't click: {locator}")
            element.clear()
            element.send_keys(user_input)
        except (ElementNotInteractableException, TimeoutException) as e:
            logger.warning(f"{type(e).__name__}: {e} — trying JS fallback")
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.driver.execute_script("arguments[0].value = arguments[1];", element, user_input)
            except JavascriptException as js_e:
                logger.error(f"JS fallback failed: {js_e}")
                raise
        except Exception as e:
            logger.error(f"send_keys failed: {e}")
            raise

    def is_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def wait_after_interaction(self):
        if self.driver.find_elements(By.ID, "formplayer-progress") or \
           self.driver.find_elements(By.ID, "formplayer-progress-container") or \
           self.driver.find_elements(By.CSS_SELECTOR, ".spinner"):
            logger.info("Detected progress/spinner — waiting...")
            self.wait_until(lambda d: not d.find_elements(By.ID, "formplayer-progress"), timeout=60)
            self.wait_for_ajax_and_progress()
        else:
            logger.info("No progress detected — continuing.")

    def wait_for_ajax_and_progress(self, timeout=10):
        try:
            self.wait_until(lambda d: d.execute_script("return window.jQuery ? jQuery.active == 0 : true"), timeout)
            if self.driver.find_elements(By.ID, "formplayer-progress-container"):
                self.wait_until(lambda d: d.execute_script(
                    """
                    const el = document.querySelector('#formplayer-progress-container');
                    return el && el.children.length === 0;
                    """), timeout)
        except Exception as e:
            logger.warning(f"Exception while waiting for AJAX/progress: {e}")

    def wait_until_progress_removed(self, timeout=60):
        try:
            if self.driver.find_elements(By.ID, "formplayer-progress"):
                self.wait_until(lambda d: not d.find_elements(By.ID, "formplayer-progress"), timeout)
        except Exception as e:
            logger.warning(f"Exception while waiting for progress to disappear: {e}")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def js_click(self, locator, timeout=10):
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            logger.warning(f"JS click failed: {e}, retrying...")
            element = self.wait_until(ec.element_to_be_clickable(locator), timeout)
            self.driver.execute_script("arguments[0].click();", element)

    def js_send_keys(self, locator, value, timeout=10):
        element = self.wait_until(ec.element_to_be_clickable(locator), timeout)
        self.driver.execute_script("arguments[0].value='" + value + "';", element)
        self.wait_after_interaction()

    def reload_page(self):
        self.driver.refresh()

    def back(self):
        try:
            self.driver.back()
        except WebDriverException as e:
            logger.warning(f"driver.back() failed: {e}, trying JS fallback")
            self.driver.execute_script("window.history.back();")
