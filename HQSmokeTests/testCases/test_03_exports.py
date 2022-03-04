from HQSmokeTests.testPages.data.export_data_page import ExportDataPage

""""Contains test cases related to the Exports module"""


def test_case_21_form_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.add_form_exports()
    export.form_exports()


def test_case_21_case_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.add_case_exports()
    export.case_exports()


def test_case_22_sms_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.sms_exports()


def test_case_24_daily_saved_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.cleanup_existing_dse()
    export.daily_saved_exports_form()
    export.daily_saved_exports_case()


def test_exports_cleanup(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.delete_all_bulk_exports()
