import time

from Formplayer.testPages.app_preview.login_as_app_preview_page import LoginAsAppPreviewPage
from Formplayer.testPages.webapps.webapps_basics import WebAppsBasics
from common_utilities.generate_random_string import fetch_random_string, fetch_phone_number
from common_utilities.selenium.base_page import BasePage
from Formplayer.userInputs.user_inputs import UserData

from selenium.webdriver.common.by import By

""""Contains test page elements and functions related to the WebApps Access/Basics of Commcare"""


class BasicTestAppPreview(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.name_input1 = "basic test1 " + fetch_random_string()
        self.name_input2 = "basic test2 " + fetch_random_string()
        self.name_input3 = "basic test3 " + fetch_random_string()
        self.changed_name_input = "basic test changed " + fetch_random_string()

        self.test_question = "Test " + fetch_random_string()

        self.application_menu_id = (By.LINK_TEXT, "Applications")

        self.back_button = (By.XPATH, "//i[@class ='fa fa-chevron-left']")
        self.form_list = (By.XPATH, "//tbody[@class='menus-container']")
        self.refresh_button = (By.XPATH, "//button[contains(@class,'btn-preview-refresh js-preview-refresh')]")
        self.toggle_button = (By.XPATH, "//button[contains(@class ,'js-preview-toggle-tablet-view')]")
        self.sync_button = (By.XPATH,"//div[@class='js-sync-item appicon appicon-sync']")
        self.start_option = (By.XPATH, "//div[@class= 'js-start-app appicon appicon-start']")
        self.settings_option = (By.XPATH, "//div[@class = 'js-settings appicon appicon-settings']/i")
        self.login_as_option = (By.XPATH, "//div[@class='js-restore-as-item appicon appicon-restore-as']")
        self.incomplete_form = (By.XPATH, "//div[@class='js-incomplete-sessions-item appicon appicon-incomplete']")

        self.case_list_menu = "//h3[contains(text(), '{}')]"
        self.registration_form = "//h3[contains(text(), '{}')]"
        self.followup_form = (By.XPATH, "//h3[contains(text(), 'Followup Form')]")
        self.name_question = (By.XPATH,
                              "//label[.//span[.='Enter a Name']]/following-sibling::div//textarea[contains(@class,'textfield form-control')]")
        self.incomplete_form_list = (By.XPATH, "//tr[@class='formplayer-request']")
        self.delete_incomplete_form = "(//tr[@class='formplayer-request']/descendant::div[@aria-label='Delete form'])[{}]"
        self.edit_incomplete_form = (By.XPATH,"(//tr[@class='formplayer-request']/descendant::div//i[contains(@class,'fa fa-pencil')])[1]")
        self.click_today_date = (By.XPATH, "//a[@data-action='today']")
        self.close_date_picker = (By.XPATH, "//a[@data-action='close']")
        self.mobileno_question = (By.XPATH, "//label[.//span[text()='Mobile No.']]/following-sibling::div//input")
        self.submit_form_button = (By.XPATH, "//button[contains(@data-bind,'submitForm')]")

        self.next_question = (By.XPATH, "//button[contains(@data-bind,'nextQuestion')]")
        self.complete_form = (By.XPATH, "//button[@data-bind='visible: atLastIndex(), click: submitForm']")
        self.success_message = (By.XPATH, "//p[text()='Form successfully saved!']")
        self.view_form_link = (By.LINK_TEXT, "this form")
        self.export_form_link = (By.LINK_TEXT, "form")
        self.last_form = (
        By.XPATH, "(//ul[contains(@class,'appnav-menu-nested')]//div[contains(@class,'appnav-item')])[last()]")
        self.delete_form = (By.XPATH, "(//div[contains(@class,'appnav-item')]/a[@class='appnav-delete']/i)[last()]")
        self.delete_confirm_button = (
        By.XPATH, "(//div[contains(@id,'form_confirm_delete')]//button/i[@class='fa fa-trash'])[last()]")
        self.question_display_text = (By.XPATH, "//span[text()='Name (es)']")
        self.iframe = (By.CLASS_NAME, "preview-phone-window")
        self.home_button = (By.XPATH, "//li[./i[@class='fa fa-home']]")
        self.full_menu = (By.LINK_TEXT, "Show Full Menu")
        self.delete_confirm = (By.ID, 'js-confirmation-confirm')
        self.submitted_value = "(//tbody//td[2]/div[contains(.,'{}')])[1]"
        self.table_data = (By.XPATH, "(//tbody//td[2]/div[contains(@class,'data-raw')])[1]")


    def open_form(self, case_list, form_name):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.start_option)
        self.wait_to_click((By.XPATH, self.case_list_menu.format(case_list)))
        self.wait_to_click((By.XPATH, self.registration_form.format(form_name)))
        self.switch_to_default_content()

    def save_incomplete_form(self, value):
        self.switch_to_frame(self.iframe)
        self.send_keys(self.name_question, value)
        self.wait_to_click(self.next_question)
        self.wait_to_click(self.home_button)
        self.switch_to_default_content()
        time.sleep(2)

    def delete_all_incomplete_forms(self):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.incomplete_form)
        list = self.find_elements(self.incomplete_form_list)
        print(len(list))
        if len(list) != 0:
            for i in range(len(list)):
                self.js_click_direct((By.XPATH, self.delete_incomplete_form.format(1)))
                self.wait_to_click(self.delete_confirm)
                list = self.find_elements(self.incomplete_form_list)
        self.switch_to_default_content()
        self.wait_to_click(self.back_button)

    def verify_number_of_forms(self, no_of_forms):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.incomplete_form)
        list = self.find_elements(self.incomplete_form_list)
        assert len(list) == no_of_forms
        self.switch_to_default_content()
        self.wait_to_click(self.back_button)

    def delete_first_form(self):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.incomplete_form)
        list = self.find_elements(self.incomplete_form_list)
        print(len(list))
        if len(list) != 0:
            self.js_click_direct((By.XPATH, self.delete_incomplete_form.format(1)))
            self.wait_to_click(self.delete_confirm)
        else:
            print("There are no incomplete forms")
        list_new = self.find_elements(self.incomplete_form_list)
        assert len(list)-1 == len(list_new)
        print("deleted first incomplete form")
        self.switch_to_default_content()
        self.wait_to_click(self.back_button)

    def verify_saved_form_and_submit_unchanged(self, value):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.incomplete_form)
        list = self.find_elements(self.incomplete_form_list)
        print(len(list))
        if len(list) != 0:
            self.js_click(self.edit_incomplete_form)
            text = self.get_attribute(self.name_question,"value")
            assert text == value
            self.wait_to_click(self.next_question)
            self.wait_to_click(self.submit_form_button)
            print("Form submitted with unchanged value")
        else:
            print("There are no incomplete forms")
        time.sleep(2)
        self.wait_to_click(self.home_button)
        time.sleep(2)
        self.wait_to_click(self.sync_button)
        time.sleep(2)
        self.switch_to_default_content()

    def verify_saved_form_and_submit_changed(self, value):
        self.switch_to_frame(self.iframe)
        self.wait_to_click(self.incomplete_form)
        list = self.find_elements(self.incomplete_form_list)
        print(len(list))
        if len(list) != 0:
            self.js_click(self.edit_incomplete_form)
            text = self.get_attribute(self.name_question,"value")
            assert text == value
            self.wait_to_clear_and_send_keys(self.name_question, self.changed_name_input)
            self.wait_to_click(self.next_question)
            self.wait_to_click(self.submit_form_button)
            print("Form submitted with changed value")
        else:
            print("There are no incomplete forms")
        time.sleep(2)
        self.wait_to_click(self.home_button)
        time.sleep(2)
        self.wait_to_click(self.sync_button)
        time.sleep(2)
        self.switch_to_default_content()

    def verify_submit_history(self, value, username):
        web_app = WebAppsBasics(self.driver)
        web_app.open_submit_history_form_link(UserData.basic_tests_app, username)
        print(value)
        text = self.get_text(self.table_data)
        print(str(text).strip())
        assert str(text).strip() == value




