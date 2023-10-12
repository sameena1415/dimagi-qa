import pytest

from HQSmokeTests.testPages.applications.app_preview import AppPreviewPage
from HQSmokeTests.testPages.home.home_page import HomePage
from Features.Lookuptable.userInputs.user_inputs import UserData
from Features.Lookuptable.testPages.data.lookup_table_page import LookUpTablePage

""""Contains test cases related to the Data module"""

@pytest.mark.data
@pytest.mark.managetables
def test_case_19_create_lookup_table(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.create_lookup_table()


@pytest.mark.data
@pytest.mark.viewtables
def test_case_28_view_lookup_table(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    value = data.create_lookup_table()
    data.view_lookup_table(value)
    data.delete_lookup_table()


@pytest.mark.data
@pytest.mark.managetables
def test_case_36_select_deselect(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    data.selects_deselects()


@pytest.mark.data
@pytest.mark.managetables
def test_case_37_edit_table(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.edit_table()


@pytest.mark.data
@pytest.mark.managetables
def test_case_38_create_dummy_id(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.create_dummyid()


@pytest.mark.data
@pytest.mark.managetables
def test_case_39_edit_dummy_data(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.edit_dummy_data()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.lookupexcel
def test_case_21_error_upload_3(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    data.write_data_excel(value, download_path)
    data.upload_1(download_path, '1')


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.lookupexcel
def test_case_20_creation2(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.download_update_8(download_path, value)
    data.replace_existing_table(download_path)
    home = HomePage(driver, settings)
    home.open_menu(home.applications_menu_id)
    data.create_new_form()
    data.navigation_to_a_caselist(value)
    data.formbuilder_5()
    app_preview = AppPreviewPage(driver)
    app_preview.check_access_to_app_preview()
    data.submit_form_on_registration(UserData.languages[0], UserData.user_ids_list[0])
    driver.switch_to.default_content()
    data.delete_caselist()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.lookupexcel
def test_case_40_multiple_groups(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.multiple_groups(download_path, value)
    data.view_lookup_table(value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.lookupexcel
def test_case_41_user_restore(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.multiple_groups(download_path, value)
    driver.get(settings["url"]+UserData.restore_url)
    data.restore_attribute_1()


@pytest.mark.data
@pytest.mark.managetables
def test_case_42_delete_test_tables(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    data.download_bulk_tables()
    download_path = data.latest_download_file()
    data.compare_and_delete(download_path)
