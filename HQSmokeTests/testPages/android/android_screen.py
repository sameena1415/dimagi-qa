from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from HQSmokeTests.userInputs.user_inputs import UserData
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import time

""""Contains test page elements and functions related to the app installation and form submission on mobile"""


class AndroidScreen:

    def __init__(self, settings):
        self.options = UiAutomator2Options().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "android",
            "platformVersion": "10.0",
            "deviceName": "Google Pixel 4 XL",
            "automationName": "Appium",

            # Set URL of the application under test
            "app": "bs://4ba00b3041a98c264aa875c944c8748dd47df7fe",

            "autoGrantPermissions": "true",
            "newCommandTimeout": 200,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "Python Android",
                "sessionName": "first_test",

                # Set your access credentials
                "userName": settings["bs_user"],
                "accessKey": settings["bs_key"]

            }
        })

        # Initialize the remote Webdriver using BrowserStack remote URL
        # and desired capabilities defined above
        self.driver = webdriver.Remote(
            "http://hub-cloud.browserstack.com/wd/hub",
            options=self.options
        )
        self.driver.implicitly_wait(15)

        # Locator
        self.enter_code = "//android.widget.TextView[@text='Enter Code']"
        self.profile_code = "org.commcare.dalvik:id/edit_profile_location"
        self.start_install = "org.commcare.dalvik:id/start_install"
        self.install = "//android.widget.TextView[@text='Start Install']"
        self.username = "org.commcare.dalvik:id/edit_username"
        self.password = "org.commcare.dalvik:id/edit_password"
        self.login = "org.commcare.dalvik:id/login_button"
        self.start_button = "//android.widget.TextView[@text='Start']"
        self.sync_button = "//android.widget.TextView[@text='Sync with Server']"
        self.case_list = "//android.widget.TextView[@text='"+UserData.case_list_name+"']"
        self.form = "//android.widget.TextView[@text='"+UserData.new_form_name+"']"
        self.text_field = "//android.widget.EditText"
        self.submit_button = "//android.widget.TextView[@text='FINISH']"

    def click_xpath(self, locator):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        element.click()

    def click_id(self, locator):
        element = self.driver.find_element(AppiumBy.ID, locator)
        element.click()

    def send_text_xpath(self, locator, user_input):
        element = self.driver.find_element(AppiumBy.XPATH, locator)
        element.send_keys(user_input)

    def send_text_id(self, locator, user_input):
        element = self.driver.find_element(AppiumBy.ID, locator)
        element.send_keys(user_input)

    def install_app_and_submit_form(self, code, random_text):
        self.driver.find_element(AppiumBy.XPATH, self.enter_code).click()
        self.driver.find_element(AppiumBy.ID, self.profile_code).send_keys(code)
        self.driver.find_element(AppiumBy.ID, self.start_install).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, self.install).click()
        time.sleep(15)
        self.driver.find_element(AppiumBy.ID, self.username).send_keys(UserData.app_login)
        self.driver.find_element(AppiumBy.ID, self.password).send_keys(UserData.app_password)
        self.driver.find_element(AppiumBy.ID, self.login).click()
        time.sleep(50)
        self.driver.find_element(AppiumBy.XPATH, self.start_button).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, self.case_list).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, self.form).click()
        time.sleep(3)
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Add Text "+random_text+"']").is_displayed()
        self.driver.find_element(AppiumBy.XPATH, self.text_field).send_keys(random_text)
        self.driver.find_element(AppiumBy.XPATH, self.submit_button).click()
        time.sleep(10)
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='1 form sent to server!']").is_displayed()
        self.driver.find_element(AppiumBy.XPATH, self.sync_button).click()
        time.sleep(3)

    def close_android_driver(self):
        self.driver.quit()
