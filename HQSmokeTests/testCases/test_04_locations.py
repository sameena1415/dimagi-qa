from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.org_structure_page import OrganisationStructurePage

""""Contains test cases related to the User's Locations module"""


def test_case_07_create_location(driver):

    menu = HomePage(driver)
    menu.users_menu()
    create = OrganisationStructurePage(driver)
    create.organisation_menu_open()
    print("Opened Organisation StructurePage Page")
    create.create_location()
    print("Location created")


def test_case_07_edit_existing_location(driver):

    menu = HomePage(driver)
    menu.users_menu()
    edit = OrganisationStructurePage(driver)
    edit.edit_location()
    print("Location edited")


def test_case_08_edit_location_fields(driver):

    menu = HomePage(driver)
    menu.users_menu()
    edit = OrganisationStructurePage(driver)
    edit.edit_location_fields()
    print("Location field created")
    edit.selection_location_field_for_location_created()
    print("Selected location field created, for the location")


def test_case_09_creation_organization_level(driver):

    menu = HomePage(driver)
    menu.users_menu()
    org = OrganisationStructurePage(driver)
    org.create_org_level()


def test_case_11_download_and_upload_locations(driver):

    menu = HomePage(driver)
    menu.users_menu()
    org = OrganisationStructurePage(driver)
    org.download_locations()
    org.upload_locations()


def test_cleanup_items_in_locations_menu(driver):

    menu = HomePage(driver)
    menu.users_menu()
    clean4 = OrganisationStructurePage(driver)
    clean4.cleanup_location()
    print("Deleted the location and location field")
