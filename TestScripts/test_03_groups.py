from Pages.homePage import HomePage
from Pages.groupPage import GroupPage
from TestBase.environmentSetupPage import EnvironmentSetup


class GroupsTests(EnvironmentSetup):

    def test_01_user_groups(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = GroupPage(driver)
        menu.users_menu()
        visible.click_group_menu()
        visible.add_group()
        visible.add_user_to_group()

    def test_02_edit_user_groups(self):
        driver = self.driver
        edit = GroupPage(driver)
        edit.click_group_menu()
        edit.edit_existing_group()
        edit.remove_user_from_group()
