import unittest
from SeleniumCCHQ.CommcareHQ.Pages.mobileWorkersPage import MobileWorkerPage
from SeleniumCCHQ.CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


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
        worker.mobile_worker_enter_username(UserInputs.mobile_worker_username)
        worker.mobile_worker_enter_password(UserInputs.mobile_worker_password)
        worker.click_create()
        print("Mobile Worker Created")

    def test_03_user_field_creation(self):
        driver = self.driver
        create = MobileWorkerPage(driver)
        create.mobile_worker_menu()
        create.edit_user_field()
        create.add_field()
        create.add_user_property(UserInputs.user_property)
        create.add_label(UserInputs.label)
        create.add_choice(UserInputs.choice)
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


if __name__ == "__main__":
    unittest.main()
