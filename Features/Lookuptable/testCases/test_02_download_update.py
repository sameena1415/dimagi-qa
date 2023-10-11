import pytest
from HQSmokeTests.testPages.home.home_page import HomePage
from common_utilities.Excel.excel_manage import ExcelManager
from Features.Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from Features.Lookuptable.userInputs.user_inputs import UserData

""""Contains test cases related to the Data module"""


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_05_download1(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    data.create_download_lookuptable()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_06_download_upload2(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.upload_1(UserData.hypertension_upload_path, "1")
    data.download1_specificTable()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_07_download_update_3(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    data.create_download_lookuptable()
    download_path = data.latest_download_file()
    excel = ExcelManager(download_path)
    excel.write_data('types', UserData.type_data_list)
    excel.create_sheet(UserData.field_val)
    excel.write_data(UserData.field_val, UserData.type_sheet_headers)
    data.upload_1(download_path, str(excel.row_size('types') - 1))


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_08_download_update_4(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    data.create_download_lookuptable()
    download_path = data.latest_download_file()
    excel = ExcelManager(download_path)
    excel.delete_sheet("types")
    home.data_menu()
    data.err_upload(download_path)
    data.missing_data_assert()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_09_download_update_5(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.update_delete_field(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_11_download_update_7(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    d1, d2 = data.download_update_7(value, download_path)
    data.compare_excel(d1, d2, 0)


# user1 is displayed twice
@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_12_download_update_8(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    d1, d2 = data.download_update_8(download_path, value)
    data.compare_excel(d1, d2, 1)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_13_download_update_9(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.test_13(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_14_download_update_10(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.delete_row_from_table(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_15_download_update_11(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    home.data_menu()
    data.test_15(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_16_Attributes_1(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    download_path = data.latest_download_file()
    print("path is ", download_path)
    value = data.create_download_lookup_table_without_field()
    home.data_menu()
    data.attribute_2(download_path, value)
    driver.get(settings["url"]+UserData.url+settings['login_username'])
    data.restore_attribute_1()


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_17_Attributes_2(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    download_path = data.latest_download_file()
    value = data.create_download_lookup_table_without_field()
    home.data_menu()
    data.attribute_2(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_case_18_Attributes_3(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    download_path = data.latest_download_file()
    print("path is ", download_path)
    value = data.create_download_lookup_table_without_field()
    home.data_menu()
    data.attribute_2(download_path, value)
    home.data_menu()
    data.delete_field_columns(download_path, value)


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_24_bulkupload_1(driver, settings):
    data = LookUpTablePage(driver)
    home = HomePage(driver, settings)
    home.data_menu()
    tableid1 = data.create_lookup_table()
    tableid2 = data.create_new_lookuptable()
    tablenames = tableid1 + ":" + tableid2
    print("tables", tablenames)
    data.select_multiple_tables_download(tablenames, 2)
    download_path = data.latest_download_file()
    excel = ExcelManager(download_path)
    excel.write_data(tableid1, UserData.data_list1)
    excel.write_data(tableid2, UserData.data_list1)
    home.data_menu()
    data.bulkupload_1(tablenames, 2, download_path)


def test_25_bulkupload_2(driver, settings):
    home = HomePage(driver, settings)
    home.data_menu()
    data = LookUpTablePage(driver)
    value = data.create_download_lookuptable()
    download_path = data.latest_download_file()
    excel = ExcelManager(download_path)
    excel.write_data(value, UserData.duplicate_values)
    home.data_menu()
    data.err_upload(download_path)
    data.download1()
    data.view_lookup_table(value)
    data.rowCount_table(value)
    row_value = data.rowCount_table(value)
    assert row_value == str((excel.row_size(value) - 1))
