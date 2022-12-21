import pytest

from Features.Lookuptable.testPages.data.export_data_page import ExportDataPage
from common_utilities.Excel.excel_manage import ExcelManager
from Features.Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from Features.Lookuptable.userInputs.user_inputs import UserData

""""Contains test cases related to the Data module"""

values = dict()

@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_05_download1(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id'] = data.create_download_lookuptable()
    print("Table name:", values['table_id'])
    return values['table_id']


@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_06_download_upload2(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.upload_1(UserData.hypertension_upload_path, "1")
    data.download1_specificTable()

@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_07_download_update_3(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id'] = data.create_download_lookuptable()
    download_path = data.error_upload1()
    excel = ExcelManager(download_path)
    print("table_id", values['table_id'])
    excel.write_data('types',UserData.type_data_list)
    excel.create_sheet(UserData.field_val)
    excel.write_data(UserData.field_val, UserData.type_sheet_headers)
    data.upload_1(download_path, str(excel.row_size('types')-1))

@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.excel
def test_08_download_update_4(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    values['table_id'] = data.create_download_lookuptable()
    excel = ExcelManager(driver)
    download_path = data.error_upload1()
    excel = ExcelManager(download_path)
    print("table_id", values['table_id'])
    excel.delete_sheet("types")
    data.error_upload1()


