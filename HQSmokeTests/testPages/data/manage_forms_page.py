import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class ManageFormsPage:

    def __init__(self, driver):
        self.driver = driver
        self.data_dropdown = 'Data'
        self.view_all_link = 'View All'
        self.date_range_manage_forms = "filter_range"
        self.manage_forms_link = '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a'
        self.select_app_dropdown = 'report_filter_form_app_id'
        self.village_app = "//option[text()='Village Health']"
        self.basic_tests_app = "//option[text()='Basic Tests']"
        self.apply_button = '//*[@id="apply-btn"]'
        self.select_all_checkbox = "//input[@name='select_all']"
        self.first_form_checkbox = "(//input[@type='checkbox' and @name='xform_ids'])[1]"
        self.checkbox1 = "//*[@id='form_options']//*[@type='checkbox']"
        self.archive_button = '//*[@id="submitForms"]'
        self.success_message = "//div[@class='alert alert-success']"
        self.view_form_link = "//a[@class='ajax_dialog']"
        self.archived_restored_dropdown = '//*[@id="select2-report_filter_archive_or_restore-container"]'
        self.archived_forms_option = '/html/body/span/span/span[2]/ul/li[2]'
        self.manage_forms_return = '//span[contains(text(),"Return to")]/a[.="Manage Forms"]'
        self.apply = "//button[@class='applyBtn btn btn-sm btn-primary']"
        self.date_having_submissions = "2022-01-18 to 2022-01-18"

    def wait_to_click(self, *locator, timeout=20):
        time.sleep(5)
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def switch_to_next_tab(self):
        winHandles = self.driver.window_handles
        window_after = winHandles[1]
        self.driver.switch_to.window(window_after)

    def switch_back_to_prev_tab(self):
        winHandles = self.driver.window_handles
        window_before = winHandles[0]
        self.driver.switch_to.window(window_before)

    def get_normal_forms(self):
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.ID, self.select_app_dropdown)
        self.wait_to_click(By.XPATH, self.basic_tests_app)
        # Date Filter
        self.wait_to_click(By.ID, self.date_range_manage_forms)
        self.driver.find_element(By.ID, self.date_range_manage_forms).clear()
        self.driver.find_element(By.ID, self.date_range_manage_forms).send_keys(self.date_having_submissions)
        self.wait_to_click(By.XPATH, self.apply)
        # Report Apply
        self.wait_to_click(By.XPATH, self.apply_button)
        time.sleep(5)

    def view_normal_form(self):
        # View Normal Forms
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("normal_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    def achieve_forms(self):
        self.wait_to_click(By.XPATH, self.first_form_checkbox)
        self.wait_to_click(By.XPATH, self.archive_button)
        assert WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((
            By.XPATH, self.success_message))).is_displayed()
        print("Forms archival successful!!")
        time.sleep(3)

    def get_archieved_forms(self):
        # View Archived Forms
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.ID, self.select_app_dropdown)
        self.wait_to_click(By.XPATH, self.basic_tests_app)
        self.wait_to_click(By.XPATH, self.archived_restored_dropdown)
        self.wait_to_click(By.XPATH, self.archived_forms_option)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.driver.refresh()

    def view_archieved_forms(self):
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("archived_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    def restore_forms(self):
        # Restore Archived Forms
        self.wait_to_click(By.XPATH, self.first_form_checkbox)
        self.wait_to_click(By.XPATH, self.archive_button)
        assert WebDriverWait(self.driver, 60).until(ec.presence_of_element_located((
            By.XPATH, self.success_message))).is_displayed()
        print("Forms Restoration successful!!")
