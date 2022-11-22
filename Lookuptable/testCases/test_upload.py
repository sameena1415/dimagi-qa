from pathlib import Path

import pytest

from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from common_utilities.Excel.excel_manage import ExcelManager
from Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from common_utilities.generate_random_string import fetch_random_string
from Lookuptable.userInputs.user_inputs import UserData

""""Contains test cases related to the Data module"""

values = dict()



@pytest.mark.lookup
def test_01_upload(driver):
    data = LookUpTablePage(driver)
    print(UserData.data_upload_path)
    data.upload_1(UserData.data_upload_path,'1')


@pytest.mark.lookup
def test_02_error_upload1(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id']=data.create_download_lookuptable()
    download_path = data.error_upload1()
    print("path is " + download_path)
    excel = ExcelManager(download_path)
    col = excel.col_size(values['table_id'])
    print("table_id", values['table_id'])
    excel.write_excel_data(values['table_id'], 1, col + 1, "user 1")
    excel.upload_to_path(values['table_id'], UserData.data_list)
    data.err_upload(download_path)
    data.invalid_data_assert()

@pytest.mark.lookup
def test_03_error_upload2(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id']=data.create_download_lookuptable()
    download_path = data.error_upload1()
    print("path is " + download_path)
    excel = ExcelManager(download_path)
    col = excel.col_size(values['table_id'])
    print("table_id", values['table_id'])
    excel.write_excel_data(values['table_id'], 1, col + 1, "group 1")
    excel.upload_to_path(values['table_id'], UserData.data_list)
    data.err_upload(download_path)
    data.invalid_data_assert()

@pytest.mark.lookup
def test_04_Error_upload3(driver):
    data = LookUpTablePage(driver)
    data.err_upload(UserData.MalformedDocument_upload_path)
    data.missing_data_assert()










