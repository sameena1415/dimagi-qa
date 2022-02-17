import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.userInputs.user_inputs import UserData
from HQSmokeTests.testPages.users.org_structure_page import latest_download_file


class ApplicationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.app_name = "App " + fetch_random_string()
        self.question_display_text_name = "Name"

        # Create New Application
        self.applications_menu_id = (By.ID, "ApplicationsTab")
        self.new_application = (By.LINK_TEXT, "New Application")
        self.edit_app_name = (By.XPATH, '//span[@class="inline-edit-icon h3 app-title"]')
        self.app_name_textbox = (By.XPATH, "(//input[@type='text'])[1]")
        self.confirm_change = (By.XPATH, "(//button[@data-bind=\"click: save, hasFocus: saveHasFocus, visible: !isSaving()\"])[1]")
        self.add_module = (By.XPATH, "//a[@class='appnav-add js-add-new-item']")
        self.add_case_list = (By.XPATH, "//button[@data-type='case']")
        self.add_questions = (By.XPATH, "//div[@class='dropdown fd-add-question-dropdown']")
        self.text_question = (By.XPATH, "//a[@data-qtype='Text']")
        self.question_display_text = (By.XPATH, "(//div[@role='textbox'])[1]")
        self.save_button = (By.XPATH, "//span[text()='Save']")
        self.app_created = (By.XPATH, "//span[text()='"+self.app_name+"']")

        # Delete Application
        self.settings = (By.XPATH, "//i[@class='fa fa-gear']")
        self.delete_app = (By.XPATH, "//a[@href='#delete-app-modal']")
        self.delete_confirm = (By.XPATH, "(//button[@class='disable-on-submit btn btn-danger'])[last()]")

        # Application Contents
        self.menu_settings = (By.XPATH, "//a[@class='appnav-title appnav-title-secondary appnav-responsive']")
        self.menu_settings_content = (By.ID, "js-appmanager-body")
        self.form_settings = (By.XPATH, "(//a[@data-action='View Form'])[1]")
        self.form_settings_content = (By.XPATH, "//div[@class='tabbable appmanager-tabs-container']")

        # Form XML
        self.download_xml = (By.XPATH, "//a[contains(i/following-sibling::text(), 'Download')]")
        self.upload_xml = (By.XPATH, "//a[@href='#upload-xform']")
        self.add_form_button = (By.XPATH, "(//i[@class='fa fa-plus'])[1]")
        self.register_form = (By.XPATH, "//button[@data-case-action='open']")
        self.new_form_settings = (By.XPATH, "(//a[@data-action='View Form'])[3]")
        self.choose_file = (By.ID, "xform_file_input")
        self.upload = (By.ID, 'xform_file_submit')
        self.same_question_present = (By.XPATH, "//a[contains(i/following-sibling::text(), 'Name')]")

        # App Settings
        self.languages_tab = (By.XPATH, "//a[@href='#languages']")
        self.languages_tab_content = (By.ID, "language-settings-options")
        self.multimedia_tab = (By.XPATH, "//a[@href='#multimedia-tab']")
        self.multimedia_tab_content = (By.ID, "multimedia-tab")
        self.actions_tab = (By.XPATH, "//a[text()='Actions']")
        self.actions_tab_content = (By.ID, "actions")
        self.add_ons_tab = (By.XPATH, "//a[@href='#add-ons']")
        self.add_ons_tab_content = (By.ID, "add-ons")
        self.advanced_settings_tab = (By.XPATH, "//a[@href='#commcare-settings']")
        self.advanced_settings_tab_content = (By.ID, "app-settings-options")

    def create_new_application(self):
        self.wait_to_click(self.applications_menu_id)
        self.wait_to_click(self.new_application)
        self.wait_to_click(self.edit_app_name)
        self.clear(self.app_name_textbox)
        self.send_keys(self.app_name_textbox, self.app_name)
        self.wait_to_click(self.confirm_change)
        self.wait_to_click(self.add_module)
        time.sleep(1)
        self.wait_to_click(self.add_case_list)
        time.sleep(2)
        self.wait_to_click(self.add_questions)
        time.sleep(2)
        self.wait_to_click(self.text_question)
        self.send_keys(self.question_display_text, self.question_display_text_name)
        self.wait_to_click(self.save_button)
        assert self.is_present_and_displayed(self.app_created)
        print("New App created successfully!")

    def form_builder_exploration(self):
        time.sleep(2)
        self.click(self.menu_settings)
        time.sleep(2)
        self.wait_for_element(self.menu_settings_content)
        assert self.is_displayed(self.menu_settings_content)
        print("Menu Settings loaded successfully!")
        self.wait_to_click(self.form_settings)
        assert self.is_present_and_displayed(self.form_settings_content)
        print("Form Settings loaded successfully!")

    def delete_application(self):
        time.sleep(2)
        self.js_click(self.settings)
        self.wait_to_click(self.actions_tab)
        self.wait_to_click(self.delete_app)
        self.wait_to_click(self.delete_confirm)
        print("Deleted the application")

    def form_xml_download_upload(self):
        try:
            self.wait_to_click(self.actions_tab)
        except TimeoutException:
            self.wait_to_click(self.form_settings)
            self.wait_to_click(self.actions_tab)
        self.wait_and_sleep_to_click(self.download_xml)
        self.wait_and_sleep_to_click(self.add_form_button)
        try:
            self.wait_and_sleep_to_click(self.register_form)
        except TimeoutException:
            self.driver.refresh()
        self.wait_and_sleep_to_click(self.new_form_settings)
        self.wait_and_sleep_to_click(self.actions_tab)
        self.wait_and_sleep_to_click(self.upload_xml)
        newest_file = latest_download_file()
        file_that_was_downloaded = UserData.DOWNLOAD_PATH / newest_file
        self.send_keys(self.choose_file, str(file_that_was_downloaded))
        time.sleep(1)
        self.click(self.upload)
        time.sleep(1)
        assert self.is_present_and_displayed(self.same_question_present)
        print("XML copied successfully!")

    def app_settings_exploration(self):
        try:
            self.wait_to_click(self.settings)
        except TimeoutException:
            self.driver.refresh()
            self.click(self.settings)
        assert self.is_present_and_displayed(self.languages_tab_content)
        self.wait_to_click(self.multimedia_tab)
        assert self.is_present_and_displayed(self.multimedia_tab_content)
        self.wait_to_click(self.actions_tab)
        assert self.is_present_and_displayed(self.actions_tab_content)
        self.wait_to_click(self.add_ons_tab)
        assert self.is_present_and_displayed(self.add_ons_tab_content)
        time.sleep(2)
        self.wait_to_click(self.advanced_settings_tab)
        assert self.is_present_and_displayed(self.advanced_settings_tab_content)
        print("App Settings loading successfully!")
