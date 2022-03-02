from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from HQSmokeTests.testPages.webapps.web_apps_page import WebAppsPage
from HQSmokeTests.testPages.data.export_data_page import ExportDataPage

def test_case_14_report_loading(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.worker_activity_report()
    load.daily_form_activity_report()
    load.submissions_by_form_report()
    load.form_completion_report()
    load.case_activity_report()
    load.completion_vs_submission_report()
    load.worker_activity_times_report()
    load.project_performance_report()
    load.submit_history_report()
    load.case_list_report()
    load.sms_usage_report()
    load.messaging_history_report()
    load.message_log_report()
    load.sms_opt_out_report()
    load.scheduled_messaging_report()


def test_case_15_16_submit_form_verify_formdata_casedata(driver):
    home = HomePage(driver)
    driver.refresh()
    home.web_apps_menu()
    webapps = WebAppsPage(driver)
    webapps.verify_apps_presence()
    case_name = webapps.submit_case_form()
    home.reports_menu()
    load = ReportPage(driver)
    load.verify_form_data_submit_history(case_name)
    load.verify_form_data_case_list(case_name)


def test_case_17_create_form_report(driver):

    report = HomePage(driver)
    driver.refresh()
    report.reports_menu()
    load = ReportPage(driver)
    load.create_report_builder_form_report()


def test_case_18_create_case_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.create_report_builder_case_report()


def test_case_19_saved_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.saved_report()


def test_case_20_scheduled_report(driver):

    report = HomePage(driver)
    report.reports_menu()
    load = ReportPage(driver)
    load.scheduled_report()
    load.delete_scheduled_and_saved_reports()

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







