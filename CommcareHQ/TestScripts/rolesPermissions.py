import unittest
from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.Pages.rolesPermissionsPage import RolesPermissionPage
from SeleniumCCHQ.CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup


class RolesPermissionsTests(EnvironmentSetup):

    def test_01_roles_permissions(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = RolesPermissionPage(driver)
        menu.users_menu()
        visible.click()


if __name__ == "__main__":
    unittest.main()
