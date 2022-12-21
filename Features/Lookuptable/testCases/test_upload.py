import pytest
from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from Features.Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from Features.Lookuptable.userInputs.user_inputs import UserData

""""Contains test cases related to the Data module"""

values = dict()

@pytest.mark.lookup
def test_01_upload(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.upload_1(UserData.data_upload_path,'1')

@pytest.mark.lookup
def test_02_error_upload1(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id']=data.create_download_lookuptable()
    download_path = data.latest_download_file()
    data.update_excel_user_value(values['table_id'],download_path)
    data.err_upload(download_path)
    data.invalid_data_assert()

@pytest.mark.lookup
def test_03_error_upload2(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id']=data.create_download_lookuptable()
    download_path = data.latest_download_file()
    data.update_excel_group_value(values['table_id'],download_path)
    data.err_upload(download_path)
    data.invalid_data_assert()

@pytest.mark.lookup
def test_04_Error_upload3(driver):
    data = LookUpTablePage(driver)
    data.err_upload(UserData.malformed_document_upload_path)
    data.missing_data_assert()










