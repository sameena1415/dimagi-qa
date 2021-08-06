import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from UserInputs.generateUserInputs import fetch_random_string


class ApplicationPage:

    def __init__(self, driver):
        self.driver = driver

        # Create New Application
        self.applications_menu_id = "ApplicationsTab"
        self.new_application = "New Application"
        self.edit_app_name = '//span[@class="inline-edit-icon h3 app-title"]'
        self.app_name_textbox = "(//input[@type='text'])[1]"
        self.app_name = "App "+fetch_random_string()
        self.confirm_change = "(//button[@data-bind=\"click: save, hasFocus: saveHasFocus, visible: !isSaving()\"])[1]"
        self.add_module = "//a[@class='appnav-add js-add-new-item']"
        self.add_case_list = "//button[@data-type='case']"
        self.add_questions = "//div[@class='dropdown fd-add-question-dropdown']"
        self.text_question = "//a[@data-qtype='Text']"
        self.question_display_text = "(//div[@role='textbox'])[1]"
        self.question_display_text_name = "Name"
        self.save_button = "//span[text()='Save']"
        self.app_created = "//span[text()='"+self.app_name+"']"

        # Delete Application
        self.settings = "//i[@class='fa fa-gear']"
        self.actions_tab = "//a[text()='Actions']"
        self.delete_app = "//a[@href='#delete-app-modal']"
        self.delete_confirm = "(//button[@class='disable-on-submit btn btn-danger'])[last()]"

        # Application Contents
        self.menu_settings = "//a[@class='appnav-title appnav-title-secondary appnav-responsive']"
        self.menu_settings_content = "js-appmanager-body"
        self.form_settings = "(//a[@data-action='View Form'])[1]"
        self.form_settings_content = "//div[@class='tabbable appmanager-tabs-container']"

    def wait_to_click(self, *locator, timeout=10):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except TimeoutException:
            print(TimeoutException)

    def create_new_application(self):
        self.wait_to_click(By.ID, self.applications_menu_id)
        self.wait_to_click(By.LINK_TEXT, self.new_application)
        self.wait_to_click(By.XPATH, self.edit_app_name)
        self.driver.find_element(By.XPATH, self.app_name_textbox).clear()
        self.driver.find_element(By.XPATH, self.app_name_textbox).send_keys(self.app_name)
        self.wait_to_click(By.XPATH, self.confirm_change)
        self.wait_to_click(By.XPATH, self.add_module)
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.add_case_list)
        self.wait_to_click(By.XPATH, self.add_questions)
        self.wait_to_click(By.XPATH, self.text_question)
        self.driver.find_element(By.XPATH, self.question_display_text).send_keys(self.question_display_text_name)
        self.wait_to_click(By.XPATH, self.save_button)
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.app_created))).is_displayed()
        print("New App created successfully!")

    def form_builder_exploration(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.menu_settings).click()
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.ID, self.menu_settings_content))).is_displayed()
        print("Menu Settings loaded successfully!")
        self.driver.find_element(By.XPATH, self.form_settings).click()
        assert True == WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((
            By.XPATH, self.form_settings_content))).is_displayed()
        print("Form Settings loaded successfully!")

    def delete_application(self):
        time.sleep(2)
        self.wait_to_click(By.XPATH, self.settings)
        self.wait_to_click(By.XPATH, self.actions_tab)
        self.wait_to_click(By.XPATH, self.delete_app)
        self.wait_to_click(By.XPATH, self.delete_confirm)