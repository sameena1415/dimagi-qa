import pytest

from HQSmokeTests.testPages.applications.app_preview import AppPreviewPage
from HQSmokeTests.testPages.applications.application_page import ApplicationPage
from HQSmokeTests.testPages.email.email_verification import EmailVerification
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage

from HQSmokeTests.userInputs.user_inputs import UserData

@pytest.mark.report
@pytest.mark.reportCaseList
@pytest.mark.p1p2EscapeDefect
def test_case_70_case_owner_list(driver, settings):
    report = HomePage(driver, settings)
    report.reports_menu()
    load = ReportPage(driver)
    load.check_for_case_list_owner(settings['url'])


@pytest.mark.report
@pytest.mark.reportCaseList
@pytest.mark.p1p2EscapeDefect
def test_case_71_case_owner_list_explorer(driver, settings):
    report = HomePage(driver, settings)
    report.reports_menu()
    load = ReportPage(driver)
    load.check_for_case_list_explorer_owner(settings['url'])


@pytest.mark.report
@pytest.mark.p1p2EscapeDefect
def test_case_75_daily_form_activity(driver, settings):
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    report.daily_form_activity_report()
    web_data = report.export_daily_form_activity_to_excel()
    email = EmailVerification(settings)
    link = email.get_hyperlink_from_latest_email(UserData.daily_form_activity, settings['url'])
    report.compare_web_with_email(link, web_data)

@pytest.mark.report
@pytest.mark.p1p2EscapeDefect
def test_case_76_application_status(driver, settings):
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    web_data = report.export_app_status_to_excel()
    email = EmailVerification(settings)
    link = email.get_hyperlink_from_latest_email(UserData.app_status, settings['url'])
    report.compare_app_status_web_with_email(link, web_data)


@pytest.mark.application
@pytest.mark.appBuilder
@pytest.mark.p1p2EscapeDefect
def test_case_77_create_new_app(driver, settings):
    load = ApplicationPage(driver)
    app_name = load.create_application_with_verifications()
    app = AppPreviewPage(driver)
    lat, lon = app.submit_form_with_loc()
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    report.verify_form_in_submit_history(app_name, lat, lon)
    load.delete_p1p2_application(app_name)
