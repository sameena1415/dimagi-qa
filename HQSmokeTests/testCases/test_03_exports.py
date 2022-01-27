from HQSmokeTests.testPages.data.export_data_page import ExportDataPage


def test_TC_21_form_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.add_form_exports()
    export.form_exports()
    export.validate_downloaded_form_exports()


def test_TC_21_case_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.add_case_exports()
    export.case_exports()
    export.validate_downloaded_case_exports()


def test_TC_22_sms_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.sms_exports()


def test_TC_24_daily_saved_exports(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.daily_saved_exports_form()
    export.daily_saved_exports_case()


def test_TC_25_excel_dashboard_integration_form(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.excel_dashboard_integration_form()


def test_TC_26_excel_dashboard_integration_case(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.excel_dashboard_integration_case()


def test_TC_28_powerBI_tableau_integration_case(driver, settings):
    username = settings["login_username"]
    password = settings["login_password"]
    export = ExportDataPage(driver)
    export.data_tab()
    export.power_bi_tableau_integration_case(username, password)


def test_TC_29_powerBI_tableau_integration_form(driver, settings):
    username = settings["login_username"]
    password = settings["login_password"]
    export = ExportDataPage(driver)
    export.data_tab()
    export.power_bi_tableau_integration_form(username, password)
    export.delete_all_bulk_exports()
