import pytest

from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.messaging.messaging_page import MessagingPage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from common_utilities.generate_random_string import fetch_random_string

""""Contains test cases related to the Messaging module"""



@pytest.mark.messaging
@pytest.mark.broadcasts
@pytest.mark.p1p2EscapeDefect
def test_case_43_broadcast(driver, settings, rerun_count):
    menu = HomePage(driver, settings)
    msg = MessagingPage(driver)
    broadcast_input = f"broadcast_{fetch_random_string()}{rerun_count}"
    menu.messaging_menu()
    msg.send_broadcast_message(broadcast_input)


@pytest.mark.messaging
@pytest.mark.conditionalAlerts
@pytest.mark.report
@pytest.mark.reportMessaging
@pytest.mark.p1p2EscapeDefect
def test_case_44_create_cond_alert(driver, settings, rerun_count):
    menu = HomePage(driver, settings)
    msg = MessagingPage(driver)
    cond_alert_name_input = f"cond_alert_{fetch_random_string()}{rerun_count}"
    menu.messaging_menu()
    cond_alert = msg.create_cond_alert(cond_alert_name_input)
    menu.reports_menu()
    history = ReportPage(driver)
    history.validate_messaging_history_for_cond_alert(cond_alert)
    menu.messaging_menu()
    msg.remove_cond_alert(cond_alert_name_input)


@pytest.mark.projectSettings
@pytest.mark.currentSubscription
@pytest.mark.p1p2EscapeDefect
def test_case_52_settings_pages(driver, settings):
    msg = MessagingPage(driver)
    home = HomePage(driver, settings)
    home.project_settings_page()
    msg.current_subscription_page()

