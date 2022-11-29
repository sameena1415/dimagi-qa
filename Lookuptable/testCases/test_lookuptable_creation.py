
import pytest

from Lookuptable.testPages.data.export_data_page import ExportDataPage
from Lookuptable.testPages.data.lookup_table_page import LookUpTablePage


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
    values['table_id'] = data.create_lookup_table()
    data.view_lookup_table(values['table_id'])
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
    export = ExportDataPage(driver)
    export.data_tab()
    data = LookUpTablePage(driver)
    values['table_id'] = data.create_download_lookuptable()
    download_path = data.error_upload1()
    print("path is " + download_path)
    data.write_data_excel(values['table_id'], download_path)
    data.upload_1(download_path, '1')


