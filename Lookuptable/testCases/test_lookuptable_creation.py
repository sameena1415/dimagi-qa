from pathlib import Path

import pytest

from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from common_utilities.Excel.excel_manage import ExcelManager
from Lookuptable.testPages.data.lookup_table_page import LookUpTablePage
from common_utilities.generate_random_string import fetch_random_string
from Lookuptable.userInputs.user_inputs import UserData

""""Contains test cases related to the Data module"""

values = dict()

@pytest.mark.data
@pytest.mark.managetables
def test_19_create_lookup_table(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.create_lookup_table()

@pytest.mark.data
@pytest.mark.viewtables
def test_29_view_lookup_table(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.create_lookup_table()
    data.view_lookup_table()
    data.delete_lookup_table()


@pytest.mark.data
@pytest.mark.managetables
def test_37_select_deselect(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    data.selects_deselects()

@pytest.mark.data
@pytest.mark.managetables
def test_38_edit_table(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.edit_table()

@pytest.mark.data
@pytest.mark.managetables
def test_39_create_dummy_id(driver):
        data = LookUpTablePage(driver)
        export = ExportDataPage(driver)
        export.data_tab()
        data.create_dummyid()

@pytest.mark.data
@pytest.mark.managetables
def test_40_edit_dummy_data(driver):
        data = LookUpTablePage(driver)
        export = ExportDataPage(driver)
        export.data_tab()
        data.edit_dummy_data()

@pytest.mark.data
@pytest.mark.managetables
@pytest.mark.lookupexcel
def test_21_Error_upload3(driver):
    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    values['table_id'] = data.create_download_lookuptable()
    excel = ExcelManager(driver)
    Download_path = data.error_upload1()
    print("path is " + Download_path)
    excel = ExcelManager(Download_path)
    for x in UserData.Col_headers:
        for i in range(1,2):
            col = excel.col_size(values['table_id'])
            excel.write_excel_data(values['table_id'],1,col+i,x)
    for y in range(1,3):
            excel.write_data(values['table_id'], UserData.data_list1)
    data = LookUpTablePage(driver)
    data.upload_1(Download_path, '1')


