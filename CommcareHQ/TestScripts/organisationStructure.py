import unittest
from SeleniumCCHQ.CommcareHQ.Pages.homePage import HomePage
from SeleniumCCHQ.CommcareHQ.Pages.organisationStructurePage import OrganisationStructurePage
from SeleniumCCHQ.CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup


class OrganisationStructureTests(EnvironmentSetup):

    def test_01_open_organisation_page(self):
        driver = self.driver
        menu = HomePage(driver)
        visible = OrganisationStructurePage(driver)
        menu.users_menu()
        visible.organisation_menu_open()
        print("Opened Organisation StructurePage Page")

    def test_02_create_location(self):
        driver = self.driver
        create = OrganisationStructurePage(driver)
        create.create_location()
        print("Location created")

    def test_03_edit_location(self):
        driver = self.driver
        edit = OrganisationStructurePage(driver)
        edit.edit_location()
        print("Location edited")


if __name__ == "__main__":
    unittest.main()
