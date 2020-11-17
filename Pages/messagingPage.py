import time
import glob
from pathlib import Path
import os
from selenium.webdriver.common.by import By
from UserInputs.generateUserInputs import fetch_random_string
from UserInputs.userInputsData import UserInputsData


class MessagingPage:
    def __init__(self, driver):
        self.driver = driver
        # Messaging Dashboard
        self.messaging_menu_id = "MessagingTab"
        self.dashboard_linked_text = "Dashboard"
        self.dashboard_elements = "//div[@id='messaging_dashboard']"
        # Compose SMS
        self.compose_sms_menu = "Compose SMS Message"
        self.recipients_textarea = "//textarea[@name='recipients']"
        self.select_recipient = "(//ul[@role='listbox']/li)[1]"
        self.message_textarea = "//textarea[@name='message']"
        self.send_message = "(//button[@class='btn btn-primary' and @type='submit'])[1]"
        self.message_sent_success_msg = "//div[@class='alert alert-margin-top fade in alert-success']"
        # Broadcasts
        self.broadcasts = "Broadcasts"
        self.add_broadcast = "//div[@class='btn-group']"
        self.broadcast_name = "//input[@name='schedule-schedule_name']"
        self.recipients = "(//ul[@class='select2-selection__rendered'])[1]"
        self.select_users_recipients = "(//ul[@class='select2-results__options']/li)[1]"
        self.user_recipient = "(//span[@class='select2 select2-container " \
                              "select2-container--default select2-container--below'])[2]"
        self.select_value_dropdown = "//li[text()='" + "username_" + fetch_random_string() + "']"
        self.broadcast_message = "(//textarea[@data-bind='value: nonTranslatedMessage'])[2]"
        self.send_broadcast = "//button[@data-bind='text: saveBroadcastText()']"
        self.broadcast_created = "//a[text()='" + "broadcast_" + fetch_random_string() + "']"
        # Conditional Alerts
        self.cond_alerts = "Conditional Alerts"
        self.add_cond_alert = "New Conditional Alert"
        self.cond_alert_name = "//input[@name='conditional-alert-name']"
        self.continue_button_basic_tab = "//button[@data-bind='click: handleBasicNavContinue, enable: basicTabValid']"
        self.case_type = "//select[@data-bind='value: caseType']"
        self.case_type_option_value = "//option[@value='case']"
        self.continue_button_rule_tab =  "//button[@data-bind='click: handleRuleNavContinue, enable: ruleTabValid']"
        self.cond_alert_created = "//a[text()='" + "cond_alert_" + fetch_random_string() + "']"
        # Condition Alerts : Download and Upload
        self.bulk_upload_button = "Bulk Upload SMS Alert Content"
        self.download = "Download SMS alert content"
        self.choose_file = "//input[@name='bulk_upload_file']"
        self.upload = "Upload SMS alert content"
        # Keywords
        self.keywords = "Keywords"
        self.add_keyword = "Add Keyword"
        self.keyword_name = "//input[@name='keyword']"
        self.keyword_description = "//input[@name='description']"
        self.keyword_message = "//input[@name='sender_message']"
        self.keyword_created = "//a[text()='" + "keyword_" + fetch_random_string() + "']"
        self.add_structured_keyword = "Add Structured Keyword"
        self.keyword_survey = "(//span[@class='select2-selection__rendered'])[1]"
        self.survey_option_select = "(//li[@class='select2-results__option'])[2]"
        self.structured_keyword_created = "//a[text()='" + "structured_keyword_" + fetch_random_string() + "']"
        # Chat
        self.chat = "Chat"
        self.contact_table = "contact_list"
        # SMS Connectivity
        self.sms_connectivity = "SMS Connectivity"
        self.add_gateway= "(//button[@class='btn btn-primary'])[1]"
        self.gateway_name = "//input[@name='name']"
        self.host_and_port = "//input[@name='host_and_port']"
        self.username = "//input[@name='user_name']"
        self.password = "//input[@name='password']"
        self.sender_id = "//input[@name='sender_id']"
        self.client_name = "//input[@name='circle_name']"
        self.campaign_name = "//input[@name='campaign_name']"
        self.gateway_created = "//a[text()='" + "gateway_" + fetch_random_string() + "']"
        # General Settings
        self.general_settings = "General Settings"
        self.disable_button = "(//div[@class='btn-group-separated'])/button[1]"
        self.enable_button = "(//div[@class='btn-group-separated'])/button[2]"
        self.time_input = "(//input[@data-bind='value: end_time'])[2]"
        self.settings_success_msg = ""
        # Languages
        self.languages = "Languages"
        self.add_lang = "//button[@data-bind='click: addLanguage, disable: addLanguageDisabled']"
        self.lang_input_textarea = "(//span[@role='combobox'])[last()]"
        self.select_first_lang = "(//li[@role='treeitem'])[1]"
        self.select_second_lang = "(//li[@role='treeitem'])[2]"
        self.save_lang = "(//div[@class='btn btn-primary'])[1]"
        self.delete_lang = "(//a[@data-bind='click: $root.removeLanguage'])[last()]"

    def open_dashboard_page(self):
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.dashboard_elements).is_displayed()

    def compose_sms(self):
        self.driver.find_element(By.LINK_TEXT, self.compose_sms_menu).click()
        self.driver.find_element(By.XPATH, self.recipients_textarea).send_keys("group")
        self.driver.find_element(By.XPATH, self.select_recipient).click()
        self.driver.find_element(By.XPATH, self.message_textarea).send_keys("Test Message")
        self.driver.find_element(By.XPATH, self.send_message).click()
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.message_sent_success_msg).is_displayed()

    def send_broadcast(self):
        self.driver.find_element(By.LINK_TEXT, self.broadcasts).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_broadcast).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.broadcast_name).send_keys("broadcast_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.recipients).click()
        self.driver.find_element(By.XPATH, self.select_users_recipients).click()
        self.driver.find_element(By.XPATH, self.select_value_dropdown).click()
        self.driver.find_element(By.XPATH, self.broadcast_message).sennd_keys("Test Broadcast:" + "broadcast_"
                                                                              + fetch_random_string())
        self.driver.find_element(By.XPATH, self.send_broadcast).click()
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.broadcast_created).is_displayed()

    def create_cond_alert(self):
        self.driver.find_element(By.LINK_TEXT, self.cond_alerts).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.add_cond_alert).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.cond_alert_name).send_keys("cond_alert_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.continue_button_basic_tab).click()
        self.driver.find_element(By.XPATH, self.case_type).click()
        self.driver.find_element(By.XPATH, self.case_type_option_value).click()
        self.driver.find_element(By.XPATH, self.continue_button_rule_tab).click()
        self.driver.find_element(By.XPATH, self.recipients).click()
        self.driver.find_element(By.XPATH, self.select_users_recipients).click()
        self.driver.find_element(By.XPATH, self.broadcast_message).sennd_keys("Test Alert:" + "cond_alert_"
                                                                              + fetch_random_string())
        self.driver.find_element(By.XPATH, self.send_message).click()
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.cond_alert_created).is_displayed()

    def cond_alert_download(self):
        self.driver.find_element(By.LINK_TEXT, self.bulk_upload_button).click()
        self.driver.find_element(By.LINK_TEXT, self.download).click()

    def cond_alert_upload(self):
        path = Path(str(Path.home()) + '\Downloads\*.xlsx')
        list_of_files = glob.glob(str(path))
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        self.driver.find_element(By.LINK_TEXT, self.choose_file).send_keys(latest_file)
        self.driver.find_element(By.LINK_TEXT, self.upload).click()

    def add_keyword(self):
        self.driver.find_element(By.LINK_TEXT, self.keywords).click()
        self.driver.find_element(By.LINK_TEXT, self.add_keyword).click()
        self.driver.find_element(By.XPATH, self.keyword_name).send_keys("keyword_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.keyword_description).send_keys("keyword_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.keyword_message).send_keys("Test Message"+"keyword_"
                                                                           + fetch_random_string())
        self.driver.find_element(By.XPATH, self.send_message).click()
        assert True == self.driver.find_element(By.XPATH, self.keyword_created).is_displayed()

    def add__structured_keyword(self):
        self.driver.find_element(By.LINK_TEXT, self.keywords).click()
        self.driver.find_element(By.LINK_TEXT, self.add__structured_keyword()).click()
        self.driver.find_element(By.XPATH, self.keyword_name).send_keys("structured_keyword_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.keyword_description).send_keys("structured_keyword_"
                                                                               + fetch_random_string())
        self.driver.find_element(By.XPATH, self.keyword_survey).click()
        self.driver.find_element(By.XPATH, self.survey_option_select).click()
        self.driver.find_element(By.XPATH, self.keyword_message).send_keys("Test Message"+"structured_keyword_"
                                                                           + fetch_random_string())
        self.driver.find_element(By.XPATH, self.send_message).click()
        assert True == self.driver.find_element(By.XPATH, self.structured_keyword_created).is_displayed()

    def chats(self):
        self.driver.find_element(By.LINK_TEXT, self.chat).click()
        assert True == self.driver.find_element(By.ID, self.contact_table).is_displayed()

    def sms_connectivity(self):
        self.driver.find_element(By.LINK_TEXT, self.sms_connectivity).click()
        self.driver.find_element(By.XPATH, self.add_gateway).click()
        self.driver.find_element(By.XPATH, self.gateway_name).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.host_and_port).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.username).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.password).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.sender_id).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.client_name).send_keys("gateway_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.campaign_name).send_keys("gateway_" + fetch_random_string())
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.gateway_created).is_displayed()

    def general_settings(self):
        self.driver.find_element(By.LINK_TEXT, self.general_settings).click()
        time.sleep(2)
        if self.driver.find_element(By.XPATH, self.disable_button).is_selected():
            self.driver.find_element(By.XPATH, self.enable_button).click()
            self.driver.find_element(By.XPATH, self.time_input).send_keys("23:59")
        else:
            self.driver.find_element(By.XPATH, self.disable_button).click()
        self.driver.find_element(By.XPATH, self.send_message).click()
        assert True == self.driver.find_element(By.XPATH, self.self.message_sent_success_msg).is_displayed()

    def languages(self):
        self.driver.find_element(By.LINK_TEXT, self.languages).click()
        self.driver.find_element(By.XPATH, self.add_lang).click()
        self.driver.find_element(By.XPATH, self.lang_input_textarea).click()
        self.driver.find_element(By.XPATH, self.select_first_lang).click()
        self.driver.find_element(By.XPATH, self.save_lang).click()
        self.driver.find_element(By.XPATH, self.lang_input_textarea).click()
        self.driver.find_element(By.XPATH, self.select_second_lang).click()
        self.driver.find_element(By.XPATH, self.save_lang).click()
        self.driver.find_element(By.XPATH, self.delete_lang).click()
        self.driver.find_element(By.XPATH, self.save_lang).click()













