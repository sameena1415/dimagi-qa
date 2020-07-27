import unittest
import time
import HtmlTestRunner
from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup


class MenuVisibilityTests(EnvironmentSetup):

    def test_01_reports_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.reports_menu()
        except Exception as e:
            print(e)
        finally:
            assert "My Saved Reports : Project Reports :: - CommCare HQ" in driver.title
            print("Reports Menu Visible and Click-able")
            time.sleep(2)

    def test_02_dashboard_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.dashboard_menu()
        except Exception as e:
            print(e)
        finally:
            assert "CommCare HQ" in driver.title
            print("Dashboard Menu Visible and Click-able")
            time.sleep(2)

    def test_03_application_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.applications_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Releases - Untitled Application - CommCare HQ" in driver.title
            print("Application Menu Visible and Click-able")
            time.sleep(2)

    def test_04_user_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.users_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Mobile Workers : Users :: - CommCare HQ" in driver.title
            print("Users Menu Visible and Click-able")
            time.sleep(2)

    def test_05_data_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.data_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Export Form Data : Data :: - CommCare HQ" in driver.title
            print("Data Menu Visible and Click-able")
            time.sleep(2)

    def test_06_web_apps_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.web_apps_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Web Apps - CommCare HQ" in driver.title
            print("WebApps Menu Visible and Click-able")
            time.sleep(2)

    def test_07_messaging_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.messaging_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Dashboard : Messaging :: - CommCare HQ" in driver.title
            print("Messaging Menu Visible and Click-able")
            time.sleep(2)

    def test_08_admin_menu_visibility(self):
        driver = self.driver
        visible = HomePage(driver)
        try:
            visible.admin_menu()
        except Exception as e:
            print(e)
        finally:
            assert "User List - CommCare HQ" in driver.title
            print("Admin Menu Visible and Click-able")
            time.sleep(2)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='SeleniumCCHQ/CommcareHQ/Reports'))
