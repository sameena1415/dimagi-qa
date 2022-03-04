from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from HQSmokeTests.testPages.webapps.web_apps_page import WebAppsPage

""""Contains test cases related to the Export module"""


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


def test_case_25_excel_dashboard_integration_form(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.excel_dashboard_integration_form()


def test_case_26_excel_dashboard_integration_case(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.excel_dashboard_integration_case()


def test_case_27_powerbi_tableau_integration_case(driver, settings):
    username = settings["login_username"]
    password = settings["login_password"]
    export = ExportDataPage(driver)
    export.data_tab()
    export.power_bi_tableau_integration_case(username, password)


def test_case_28_powerbi_tableau_integration_form(driver, settings):
    username = settings["login_username"]
    password = settings["login_password"]
    export = ExportDataPage(driver)
    export.data_tab()
    export.power_bi_tableau_integration_form(username, password)


def test_exports_cleanup(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    export.delete_all_bulk_exports()


def test_case_55_update_case_verify_change_in_export_data(driver, settings):
    case = HomePage(driver)
    case.web_apps_menu()
    webapps = WebAppsPage(driver)
    case_name = webapps.submit_case_change_register_form()
    value = webapps.submit_case_update_form(case_name)
    webapps.click_case_link()
    load = ReportPage(driver)
    case_id = load.verify_updated_data_in_case_list(case_name,value)
    export = ExportDataPage(driver)
    export.data_tab()
    export.add_updated_case_exports(settings['login_username'])
    export.verify_export_has_updated_case_data(case_id, case_name, value)
    export.data_tab()
    export.clean_up_case_data()