from HQSmokeTests.testPages.data.data_page import DataPage
from HQSmokeTests.testPages.data.export_data_page import ExportDataPage


def test_TC_32_auto_case_update(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    data = DataPage(driver)
    data.open_auto_case_update_page()
    data.add_new_rule()
    data.remove_rule()


def test_TC_33_create_lookup_table(driver):

    data = DataPage(driver)
    data.create_lookup_table()


def test_TC_34_view_lookup_table(driver):

    data = DataPage(driver)
    data.view_lookup_table()
    data.delete_lookup_table()
