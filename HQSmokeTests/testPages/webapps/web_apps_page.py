from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.userInputs.user_inputs import UserData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WebAppsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.case_name_created = "case_" + fetch_random_string()

        self.login_as_css = (By.CLASS_NAME, "js-restore-as-item")
        self.login_user = (By.XPATH, "//*[text()='" + UserData.login_as + "']")
        self.confirm_user_login = (By.XPATH, "//button[@id='js-confirmation-confirm']")

        self.apps_links = (By.XPATH, "//*[@class='fcc fcc-flower appicon-icon']")
        self.web_app_link = (By.XPATH, "//*[text()='" + UserData.reassign_cases_application + "']")
        self.case_list_link = (By.XPATH, "//*[text()='" + UserData.case_list_name + "']")
        self.form_link = (By.XPATH, "//*[text()='" + UserData.form_name + "']")
        self.form_case_name_input = (By.XPATH, "//textarea[@class='textfield form-control']")
        self.form_submit_button = (By.XPATH, "//button[@class='submit btn btn-primary']")
        self.success_message = (By.XPATH, "//p[text()='Form successfully saved!']")
        self.show_full_menu_link = (By.LINK_TEXT, "Show Full Menu")

    def verify_apps_presence(self):
        clickable = ec.presence_of_all_elements_located(self.apps_links)
        element = WebDriverWait(self.driver, 10).until(clickable, message="Couldn't find locator: "
                                                                          + str(self.apps_links))
        count = len(element)
        if count >= 1:
            print(count, " Web apps are present in the page")
            return True
        else:
            print("No web apps are present")
            return False

    def login_as(self):
        self.wait_to_click(self.login_as_css)
        self.wait_to_click(self.login_user)
        self.wait_to_click(self.confirm_user_login)

    def submit_case_form(self):
        self.wait_to_click(self.web_app_link)
        self.wait_to_click(self.case_list_link)
        self.wait_to_click(self.form_link)
        self.wait_to_send_keys(self.form_case_name_input, self.case_name_created)
        self.wait_to_click(self.form_submit_button)
        assert self.is_displayed(self.success_message), "Form not submitted"
        print("Form successfully submitted")
        return self.case_name_created
