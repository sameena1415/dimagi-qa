import pytest

from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.messaging.messaging_page import MessagingPage
from HQSmokeTests.testPages.reports.report_page import ReportPage

""""Contains test cases related to the Messaging module"""


@pytest.mark.messaging
@pytest.mark.messagingDashboard
def test_case_41_dashboard(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.open_dashboard_page()


@pytest.mark.messaging
@pytest.mark.composeSMS
def test_case_42_compose_sms(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.compose_sms()


@pytest.mark.messaging
@pytest.mark.broadcasts
def test_case_43_broadcast(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.send_broadcast_message()



@pytest.mark.messaging
@pytest.mark.conditionalAlerts
@pytest.mark.report
@pytest.mark.reportMessaging
def test_case_44_create_cond_alert(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    cond_alert = msg.create_cond_alert()
    menu.reports_menu()
    history = ReportPage(driver)
    history.validate_messaging_history_for_cond_alert(cond_alert)
    menu.messaging_menu()
    msg.remove_cond_alert()



@pytest.mark.messaging
@pytest.mark.conditionalAlerts
@pytest.mark.bulkUploadSMS
def test_case_45_cond_alert_bulk_upload(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.cond_alert_download()
    msg.cond_alert_upload()



@pytest.mark.messaging
@pytest.mark.keywords
def test_case_46_keyword_creation(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.add_keyword_trigger()
    msg.remove_keyword()
    msg.add_structured_keyword_trigger()
    msg.remove_structured_keyword()


@pytest.mark.messaging
@pytest.mark.chat
def test_case_47_chats(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.chat_page()



@pytest.mark.messaging
@pytest.mark.messagingGeneralSettings
def test_case_49_general_settings(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.general_settings_page()



@pytest.mark.messaging
@pytest.mark.messagingLanguages
def test_case_50_languages(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.languages_page()


@pytest.mark.messaging
@pytest.mark.messagingLanguages
@pytest.mark.messagingTranslations
def test_case_51_translations(driver):
    menu = HomePage(driver)
    msg = MessagingPage(driver)
    menu.messaging_menu()
    msg.msg_trans_download()
    msg.msg_trans_upload()


@pytest.mark.projectSettings
@pytest.mark.currentSubscription
def test_case_52_settings_pages(driver):
    msg = MessagingPage(driver)
    msg.project_settings_page()
    msg.current_subscription_page()
