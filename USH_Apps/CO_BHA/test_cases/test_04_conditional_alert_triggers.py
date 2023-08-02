from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from USH_Apps.CO_BHA.test_pages.bha_app_pages import BhaWorkflows
from datetime import datetime

from USH_Apps.CO_BHA.user_inputs.bha_user_inputs import BhaUserInput
from common_utilities.selenium.base_page import BasePage


def test_messaging_history_triggers(driver, settings):
    """use case: Check if conditional alerts have been triggred for all workflows"""
    report = HomePage(driver, settings)
    load = ReportPage(driver)
    app = BhaWorkflows(driver)
    base = BasePage(driver)

    report.reports_menu()
    load.messaging_history_report()
    now = (datetime.today()).date()
    app.view_message_details(alert_type=BhaUserInput.clinic_admission_request)
    base.switch_to_tab(1)
    app.check_if_alert_triggered(content=BhaUserInput.clinic_admission_request_content,
                                 date=str(now.strftime("%#m/%#d/%Y")))
    app.view_message_details(alert_type=BhaUserInput.clinic_same_admit_discahrge)
    base.switch_to_tab(2)
    app.check_if_alert_triggered(content=BhaUserInput.clinic_same_admit_discahrge_content,
                                 date=str(now.strftime("%Y-%m-%d")))
    app.view_message_details(alert_type=BhaUserInput.clinic_update_lock_status)
    base.switch_to_tab(3)
    app.check_if_alert_triggered(content=BhaUserInput.clinic_update_lock_status_content,
                                 date=str(now.strftime("%#m/%#d/%Y")))
    app.view_message_details(alert_type=BhaUserInput.state_determination_lock_status)
    # Commenting this until Anthony is able to help with the required setup
    """base.switch_to_tab(4)
    app.check_if_alert_triggered(content=BhaUserInput.state_determination_lock_status_content,
                                 date=str(now.strftime("%#m/%#d/%Y")))"""
