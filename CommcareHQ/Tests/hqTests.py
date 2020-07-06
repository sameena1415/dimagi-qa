from selenium import webdriver
import unittest
from SeleniumCCHQ.CommcareHQ.Pages.loginPage import LoginPage
from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.Pages.mobileWorkersPage import MobileWorkerPage
import HtmlTestRunner


class CCHQTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/dsi-user.DESKTOP-IGCBOU4/AutomationProjects/SeleniumCCHQ/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.commcarehq.org/accounts/login/")

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("automation.user.commcarehq@gmail.com")
        login.enter_password("pass@123")
        login.click_submit()
        login.accept_alert()
        print("Sucessfully logged in")

    def test_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        visible.dashboard_menu()
        print("Dashboard Menu Visible and Clickable")
        visible.reports_menu()
        print("Reports Menu Visible and Clickable")
        # visible.applications_menu()
        # print("Applications Menu Visible and Clickable")

    def test_mobileworker_creation(self):
        driver = self.driver
        visible = MobileWorkerPage(driver)
        visible.mobile_worker_menu()
        visible.create_mobile_worker()
        visible.mobile_worker_enter_username("user4")
        visible.mobile_worker_enter_password("1234")
        visible.click_create()
        print("Mobile Worker Created")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='SeleniumCCHQ/CommcareHQ/Reports'))