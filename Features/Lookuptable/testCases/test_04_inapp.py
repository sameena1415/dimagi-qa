import pytest

from HQSmokeTests.testPages.applications.app_preview import AppPreviewPage
from HQSmokeTests.testPages.home.home_page import HomePage
from Features.Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from Features.Lookuptable.userInputs.user_inputs import UserData

"""Contains test cases related to the Data module"""


@pytest.mark.lookup
@pytest.mark.inapp
def test_case_34_Lookup_table_formbuilder_6(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.open_menu(home.applications_menu_id)
    data.test_application()
    data.delete_caselist()


@pytest.mark.lookup
@pytest.mark.inapp
def test_case_30_lookup_table_form_builder1(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.open_menu(home.applications_menu_id)
    data.create_new_form()
    data.lookuptable_display_list()
    data.delete_caselist()


@pytest.mark.lookup
@pytest.mark.inapp
def test_case_29_lookup_table_form_builder1(driver, settings):  # Hover and click error.
    data = LookUpTablePage(driver)
    data.create_new_form()
    data.adding_questions()


@pytest.mark.lookup
@pytest.mark.inapp
def test_case_31_lookup_table_form_builder3(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.state, "1")
    home.open_menu(home.applications_menu_id)
    data.specific_table_upload("state")
    home.data_menu()
    data.delete_specific_lookup_table("state")
    home = HomePage(driver, settings)
    home.open_menu(home.applications_menu_id)
    data.navigation_to_application_tab()
    data.navigation_to_a_caselist("Lookup table was not found in the project")
    data.delete_caselist()


def test_case_32_lookup_table_form_builder4(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.state, "1")
    home.open_menu(home.applications_menu_id)
    data.specific_table_upload("state")
    data.formbuilder_4()
    data.delete_caselist()


def test_case_33_lookup_table_form_builder5(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.state, "1")
    home.open_menu(home.applications_menu_id)
    data.specific_table_upload("state")
    data.formbuilder_5()
    home.data_menu()
    data.edit_state()
    data.delete_caselist()


def test_case_22_filtered_lookup_table(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.Inapp, "1")
    data.specific_table_upload("Inapp")
    data.formbuilder_5()
    app_preview = AppPreviewPage(driver)
    app_preview.check_access_to_app_preview()
    data.loop_submit_form_on_registration()
    driver.switch_to.default_content()
    data.delete_caselist()


def test_case_35_languages_check(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.state, "1")
    data.specific_table_upload("state")
    data.language_check()
    AppPreview = AppPreviewPage(driver)
    AppPreview.check_access_to_app_preview()
    data.submit_form_on_registration("en", "kiran")
    data.submit_form_on_registration("hin", "kiran")
    driver.switch_to.default_content()
    data.delete_caselist()
