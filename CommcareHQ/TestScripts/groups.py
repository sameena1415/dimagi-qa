import unittest
from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.Pages.groupPage import GroupPage
from SeleniumCCHQ.CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class GroupsTests(EnvironmentSetup):

    def test_01_user_groups(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = GroupPage(driver)
        menu.users_menu()
        visible.click_group_menu()
        print("Group menu clicked")
        visible.enter_group_name(UserInputs.group_name)
        print("Group name entered")
        visible.add_group()
        print("Group Added")
        visible.click_on_users_drop_down()
        visible.add_user_to_group()
        visible.update_group()
        print("User Added to Group")

    def test_02_edit_user_groups(self):
        driver = self.driver
        edit = GroupPage(driver)
        edit.click_group_menu()
        print("Clicked on the Group to be Edited")
        edit.edit_existing_group()
        print("Clicked on Edit Settings for Group")
        edit.rename_existing_group()
        print("Renamed a group")
        edit.remove_user_from_group()
        print("Removed added user from group")


if __name__ == "__main__":
    unittest.main()
