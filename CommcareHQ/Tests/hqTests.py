import unittest

import HtmlTestRunner
from selenium import webdriver

from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.Pages.loginPage import LoginPage
from SeleniumCCHQ.CommcareHQ.Pages.mobileWorkersPage import MobileWorkerPage
from SeleniumCCHQ.CommcareHQ.Pages.groupPage import GroupPage
from SeleniumCCHQ.CommcareHQ.Pages.rolesPermissionsPage import RolesPermissionPage
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class CCHQTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=UserInputs.driver_path)
        cls.driver.maximize_window()
        cls.driver.get(UserInputs.url)

    def test_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(UserInputs.login_username)
        login.enter_password(UserInputs.login_password)
        login.click_submit()
        login.accept_alert()
        print("Successfully logged in")

    # def test_menu_visibility(self):
    #     driver = self.driver
    #     visible = HomePage(driver)
    #     visible.dashboard_menu()
    #     print("Dashboard Menu Visible and Click-able")
    #     visible.reports_menu()
    #     print("Reports Menu Visible and Click-able")
    #     # visible.applications_menu()
    #     # print("Applications Menu Visible and Click-able")
    #
    def test_mobileworker_creation(self):
        driver = self.driver
        visible = MobileWorkerPage(driver)
        visible.mobile_worker_menu()
    #     visible.create_mobile_worker()
    #     visible.mobile_worker_enter_username(UserInputs.mobile_worker_username)
    #     visible.mobile_worker_enter_password(UserInputs.mobile_worker_password)
    #     visible.click_create()
    #     print("Mobile Worker Created")
    #
    # def test_userfield_creation(self):
    #     driver = self.driver
    #     visible = MobileWorkerPage(driver)
    #     visible.mobile_worker_menu()
    #     visible.edit_user_field()
    #     visible.add_field()
    #     visible.add_user_property(UserInputs.user_property)
    #     visible.add_label(UserInputs.label)
    #     visible.add_choice(UserInputs.choice)
    #     visible.save_field()
    #     print("User Field Added")
    #
    # def test_userfield_visible(self):
    #     driver = self.driver
    #     visible = MobileWorkerPage(driver)
    #     visible.go_back_to_mobile_workers()
    #     visible.select_mobile_worker_created()
    #     print("Clicked on user")
    #     visible.enter_value_for_created_userfield()
    #     print("Selected User Field")
    #     visible.update_information()
    #     print("Info Updated")

    # def test_roles_permissions(self):
    #     driver = self.driver
    #     visible = RolesPermissionPage(driver)
    #     visible.click()

    def test_user_groups(self):
        driver = self.driver
        visible = GroupPage(driver)
        visible.click_group_menu()
        print("Group menu clicked")
        visible.enter_group_name(UserInputs.group_name)
        print("Group name entered")
        visible.add_group()
        print("Group Added")
        visible.click_on_users_dropdown()
        visible.add_user_to_group()
        visible.update_group()
        print ("User Added to Group")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='SeleniumCCHQ/CommcareHQ/Reports'))
