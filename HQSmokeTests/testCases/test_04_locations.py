import pytest

from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.org_structure_page import OrganisationStructurePage

""""Contains test cases related to the User's Locations module"""

@pytest.mark.smoke
@pytest.mark.location
def test_case_07_create_location(driver):

    menu = HomePage(driver)
    menu.users_menu()
    create = OrganisationStructurePage(driver)
    create.organisation_menu_open()
    print("Opened Organisation StructurePage Page")
    create.create_location()
    print("Location created")


@pytest.mark.smoke
@pytest.mark.location
def test_case_07_edit_existing_location(driver):

    menu = HomePage(driver)
    menu.users_menu()
    edit = OrganisationStructurePage(driver)
    edit.edit_location()
    print("Location edited")

@pytest.mark.smoke
@pytest.mark.location
def test_case_56_archive_unarchive_location(driver):

    menu = HomePage(driver)
    menu.users_menu()
    location = OrganisationStructurePage(driver)
    location.archive_location()
    print("Location successfully Archived")
    location.unarchive_location()
    print("Location successfully Unarchived")


@pytest.mark.smoke
@pytest.mark.location
def test_case_08_edit_location_fields(driver):

    menu = HomePage(driver)
    menu.users_menu()
    edit = OrganisationStructurePage(driver)
    edit.edit_location_fields()
    print("Location field created")
    edit.selection_location_field_for_location_created()
    print("Selected location field created, for the location")

@pytest.mark.smoke
@pytest.mark.location
def test_case_09_creation_organization_level(driver, settings):
    if 'staging' in settings['url']:
        pytest.xfail("failing due to QA-4374")
    menu = HomePage(driver)
    menu.users_menu()
    org = OrganisationStructurePage(driver)
    org.create_org_level()

@pytest.mark.smoke
@pytest.mark.location
def test_case_11_download_and_upload_locations(driver):

    menu = HomePage(driver)
    menu.users_menu()
    org = OrganisationStructurePage(driver)
    org.download_locations()
    org.upload_locations()

@pytest.mark.smoke
@pytest.mark.location
def test_cleanup_items_in_locations_menu(driver, settings):
    if 'staging' in settings['url']:
        pytest.xfail("failing due to QA-4374")
    menu = HomePage(driver)
    menu.users_menu()
    clean4 = OrganisationStructurePage(driver)
    clean4.cleanup_location()
    print("Deleted the location and location field")
