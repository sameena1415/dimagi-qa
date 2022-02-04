from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ReassignCasesPage:

    def __init__(self, driver):
        self.driver = driver
        self.new_user = "henry"
        self.reassign_cases_menu = (By.LINK_TEXT, "Reassign Cases")
        self.apply = (By.ID, "apply-btn")
        self.case_type = (By.ID, "select2-report_filter_case_type-container")
        self.case_type_option_value = (By.XPATH, "//option[@value='reassign']")
        self.select_first_case = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.user_search_dropdown = (By.ID, "select2-reassign_owner_select-container")
        self.user_to_be_reassigned = (By.XPATH, "(//li[contains(.,'Active Mobile Worker')])[1]")
        self.submit = (By.XPATH, "(//button[text()='Reassign'])[1]")
        self.new_owner_name = (By.XPATH, "((//td)[4])[1]")

    def wait_to_click(self, locator, timeout=10):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def wait_for_element(self, locator, timeout=10):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        element_text = element.text
        print(element_text)
        return element_text

    def send_keys(self, locator, user_input):
        element = self.driver.find_element(*locator)
        element.send_keys(user_input)

    def is_displayed(self, locator, timeout=10):
        visible = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, timeout).until(visible)
        return bool(element)

    def get_cases(self):
        self.wait_to_click(self.reassign_cases_menu)
        self.wait_to_click(self.case_type)
        self.wait_to_click(self.case_type_option_value)
        self.wait_to_click(self.apply)

    def reassign_case(self):
        self.wait_to_click(self.select_first_case)
        self.wait_to_click(self.user_search_dropdown)
        assigned_username = self.get_text(self.user_to_be_reassigned).split('"')[0]
        self.wait_to_click(self.user_to_be_reassigned)
        self.wait_to_click(self.submit)
        self.driver.refresh()
        reassigned_username = self.get_text(self.new_owner_name).split('@')[0]
        assert reassigned_username in assigned_username



