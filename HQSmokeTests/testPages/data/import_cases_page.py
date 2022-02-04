import os
import time

from openpyxl import load_workbook

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from HQSmokeTests.userInputs.generateUserInputs import fetch_random_string
from HQSmokeTests.userInputs.userInputsData import UserInputsData


def latest_download_file():
    os.chdir(UserInputsData.download_path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = max(files, key=os.path.getctime)
    print("File downloaded: " + newest)
    return newest


def edit_spreadsheet(newest_file, cell):
    workbook = load_workbook(filename=newest_file)
    sheet = workbook.active
    sheet[cell] = fetch_random_string()
    workbook.save(filename=newest_file)


class ImportCasesPage:

    def __init__(self, driver):
        self.driver = driver
        self.import_cases_menu = (By.LINK_TEXT, "Import Cases from Excel")
        self.download_file = (By.XPATH, "(//span[@data-bind='text: upload_file_name'])[1]")
        self.choose_file = (By.ID, "file")
        self.next_step = (By.XPATH, "(//button[@type='submit'])[1]")
        self.case_type = (By.ID, "select2-case_type-container")
        self.case_type_option_value = (By.XPATH, "//option[@value='pregnancy']")
        self.success = (By.XPATH, "(//span[@class='label label-success'])[1]")

    def wait_to_click(self, locator, timeout=10):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def send_keys(self, locator, user_input):
        element = self.driver.find_element(*locator)
        element.send_keys(user_input)

    def is_displayed(self, locator, timeout=10):
        visible = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, timeout).until(visible)
        return bool(element)

    def download_last_import(self):
        self.wait_to_click(self.import_cases_menu)
        self.wait_to_click(self.download_file)
        time.sleep(3)  # Let the file download completely
        print("Latest File downloaded!")

    def replace_property_and_upload(self):
        newest_file = latest_download_file()
        edit_spreadsheet(newest_file, "C2")
        print("Edited File")
        file_that_was_downloaded = UserInputsData.download_path / newest_file
        self.send_keys(self.choose_file, str(file_that_was_downloaded))
        self.wait_to_click(self.next_step)
        self.wait_to_click(self.case_type)
        self.wait_to_click(self.case_type_option_value)
        self.wait_to_click(self.next_step)
        self.wait_to_click(self.next_step)
        print("Uploaded File")
        time.sleep(3)  # Let the file upload completely
        assert self.is_displayed(self.success)

