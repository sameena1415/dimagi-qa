import unittest
from Pages.mobileWorkersPage import MobileWorkerPage
from TestBase.environmentSetupPage import EnvironmentSetup
from UserInputs.generateUserInputs import fetch_random_string


class MobileWorkerTests(EnvironmentSetup):

    def test_01_click_mobile_worker_menu(self):
        driver = self.driver
        worker = MobileWorkerPage(driver)
        try:
            worker.mobile_worker_menu()
        except Exception as e:
            print(e)
        finally:
            assert "Mobile Workers : Users :: - CommCare HQ" in driver.title
            print("Mobile Workers Menu Visible and Click-able")

    def test_02_create_mobile_worker(self):
        driver = self.driver
        worker = MobileWorkerPage(driver)
        worker.create_mobile_worker()
        worker.mobile_worker_enter_username("username_" + fetch_random_string())
        worker.mobile_worker_enter_password(fetch_random_string())
        worker.click_create()
        print("Mobile Worker Created")

    def test_03_user_field_creation(self):
        driver = self.driver
        create = MobileWorkerPage(driver)
        create.mobile_worker_menu()
        create.edit_user_field()
        create.add_field()
        create.add_user_property("user_field_" + fetch_random_string())
        create.add_label("user_field_" + fetch_random_string())
        create.add_choice("user_field_" + fetch_random_string())
        create.save_field()
        print("User Field Added")

    def test_04_user_field_visible(self):
        driver = self.driver
        visible = MobileWorkerPage(driver)
        visible.go_back_to_mobile_workers()
        visible.select_mobile_worker_created()
        print("Clicked on user")
        visible.enter_value_for_created_user_field()
        print("Selected User Field")
        visible.update_information()
        print("User Field Visible and Added for User")

    def test_05_deactivate_user(self):
        driver = self.driver
        user = MobileWorkerPage(driver)
        user.deactivate_user()
        user.verify_deactivation()
        user.verify_deactivation_via_login()

    def test_06_reactivate_user(self):
        driver = self.driver
        user = MobileWorkerPage(driver)
        user.reactivate_user()
        user.verify_reactivation()
        user.verify_reactivation_via_login()

    def test_07_download_workers(self):
        driver = self.driver
        user = MobileWorkerPage(driver)
        user.download_mobile_worker()

    def test_08_upload_workers(self):
        driver = self.driver
        user = MobileWorkerPage(driver)
        user.upload_mobile_worker()


if __name__ == "__main__":
    unittest.main()
