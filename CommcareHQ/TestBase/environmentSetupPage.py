import unittest

import HtmlTestRunner
from selenium import webdriver

from SeleniumCCHQ.CommcareHQ.Pages.loginPage import LoginPage
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class EnvironmentSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=UserInputs.driver_path)
        cls.driver.maximize_window()
        cls.driver.get(UserInputs.url)
        login = LoginPage(cls.driver)
        login.enter_username(UserInputs.login_username)
        login.enter_password(UserInputs.login_password)
        login.click_submit()
        login.accept_alert()
        print("Successfully logged in")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='SeleniumCCHQ/CommcareHQ/Reports'))
