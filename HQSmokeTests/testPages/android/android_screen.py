from datetime import datetime
from pathlib import Path

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

from common_utilities.generate_random_string import fetch_random_string
from common_utilities.path_settings import PathSettings
from HQSmokeTests.userInputs.user_inputs import UserData

""""Contains test page elements and functions related to the app installation and form submission on mobile"""


import os, json, subprocess

import os, requests

def bstack_upload_github_latest(bs_user: str, bs_key: str,
                                owner="dimagi", repo="commcare-android",
                                asset_name="app-commcare-release.apk",
                                custom_id: str | None = None) -> str:
    """Uploads the latest release APK from GitHub to BrowserStack and returns bs://..."""
    gh_url = f"https://github.com/{owner}/{repo}/releases/latest/download/{asset_name}"
    data = {"custom_id": custom_id} if custom_id else {}
    r = requests.post("https://api-cloud.browserstack.com/app-automate/upload",
                      auth=(bs_user, bs_key), data={**data, "url": gh_url}, timeout=180)
    # Success → prefer returned app_url
    if r.status_code in (200, 201):
        app_url = r.json().get("app_url")
        if app_url and app_url.startswith("bs://"):
            return app_url
        if custom_id:
            # some responses omit app_url when custom_id is set
            return f"bs://{custom_id}"
        raise RuntimeError(f"Upload ok but no app_url: {r.text}")
    # If the same custom_id already exists, still usable
    if r.status_code == 409 and custom_id:
        return f"bs://{custom_id}"
    raise RuntimeError(f"BrowserStack upload failed {r.status_code}: {r.text}")


class AndroidScreen:

    def __init__(self, settings):
        # This sample code uses the Appium python client v2
        # pip install Appium-Python-Client
        # Then you can paste this into a file and simply run with Python
        bs_user = settings["bs_user"]
        bs_key = settings["bs_key"]

        bs_app = bstack_upload_github_latest(
            bs_user, bs_key,
            owner="dimagi",
            repo="commcare-android",
            asset_name="app-commcare-release.apk",
            custom_id="commcare-latest"  # optional: stable alias for your caps
            )


        self.options = UiAutomator2Options().load_capabilities({
            # Specify device and os_version for testing
            "platformName": "android",
            "appium:platformVersion": "15.0",
            "appium:deviceName": "Google Pixel 9",
            "appium:automationName": "UIAutomator2",

            # Set URL of the application under test
            "appium:app": bs_app,

            "appium:autoGrantPermissions": "true",
            "appium:newCommandTimeout": 3600,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "Python Android",
                "sessionName": "first_test",
                "userName": bs_user,
                "accessKey": bs_key

            }
        })

        # Initialize the remote Webdriver using BrowserStack remote URL
        # and desired capabilities defined above
        self.driver = webdriver.Remote(
            "https://hub-cloud.browserstack.com:443/wd/hub",
            options=self.options
        )
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)

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
        self.case_list = "//android.widget.TextView[@text='" + UserData.case_list_name + "']"
        self.form = "//android.widget.TextView[@text='" + UserData.new_form_name + "']"
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
        assert self.driver.find_element(AppiumBy.XPATH,
                                        "//android.widget.TextView[@text='Add Text " + random_text + "']"
                                        ).is_displayed()
        self.driver.find_element(AppiumBy.XPATH, self.text_field).send_keys(random_text)
        self.driver.find_element(AppiumBy.XPATH, self.submit_button).click()
        time.sleep(2)
        assert self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='1 form sent to server!']"
                                        ).is_displayed()
        self.driver.find_element(AppiumBy.XPATH, self.sync_button).click()
        time.sleep(3)

    def close_android_driver(self):
        self.driver.quit()
