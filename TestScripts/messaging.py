import unittest
from Pages.homePage import HomePage
from Pages.messagingPage import MessagingPage
from TestBase.environmentSetupPage import EnvironmentSetup


class MessagingTests(EnvironmentSetup):

    def test_01_dashboard(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.open_dashboard_page()

    def test_02_compose_sms(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.compose_sms()

    def test_03_send_broadcast(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.send_broadcast()

    def test_03_broadcast(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.send_broadcast()

    def test_04_create_cond_alert(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.create_cond_alert()

    def test_05_cond_alert_bulk_upload(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.cond_alert_download()
        msg.cond_alert_upload()

    def test_06_keyword(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.add_keyword()
        msg.add__structured_keyword()

    def test_07_chats(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.chat()

    def test_08_sms_connectivity(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.sms_connectivity()

    def test_09_general_settings(self):
        driver = self.driver
        menu = HomePage(driver)
        msg = MessagingPage(driver)
        menu.messaging_menu()
        msg.general_settings()


if __name__ == "__main__":
    unittest.main()

