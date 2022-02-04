import os
import time

from pathlib import Path
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


def edit_spreadsheet(edited_file, cell, renamed_file):
    workbook = load_workbook(filename=edited_file)
    sheet = workbook.active
    sheet[cell] = fetch_random_string()
    workbook.save(filename=renamed_file)


class ImportCasesPage:

    def __init__(self, driver):
        self.driver = driver
        self.data_folder = Path("..\\userInputs\\test_data\\")
        self.reassign_cases_file = "reassign_cases.xlsx"
        self.village_name_cell = "C2"
        self.to_be_edited_file = self.data_folder / self.reassign_cases_file
        self.file_new_name = "reassign_cases_" + str(fetch_random_string()) + ".xlsx"
        self.renamed_file = os.path.abspath(os.path.join(self.data_folder, self.file_new_name))

        self.import_cases_menu = (By.LINK_TEXT, "Import Cases from Excel")
        self.download_file = (By.XPATH, "(//span[@data-bind='text: upload_file_name'])[1]")
        self.choose_file = (By.ID, "file")
        self.next_step = (By.XPATH, "(//button[@type='submit'])[1]")
        self.case_type = (By.ID, "select2-case_type-container")
        self.case_type_option_value = (By.XPATH, "//option[@value='pregnancy']")
        self.success = (By.XPATH, "//span[text()='" + self.file_new_name + "']//preceding::span[@class='label label-success']")

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

    def replace_property_and_upload(self):
        self.wait_to_click(self.import_cases_menu)
        edit_spreadsheet(self.to_be_edited_file, self.village_name_cell, self.renamed_file)
        self.send_keys(self.choose_file, self.renamed_file)
        self.wait_to_click(self.next_step)
        self.wait_to_click(self.case_type)
        self.wait_to_click(self.case_type_option_value)
        self.wait_to_click(self.next_step)
        self.wait_to_click(self.next_step)
        print("Imported case!")
        time.sleep(3)  # Let the file upload completely
        assert self.is_displayed(self.success)
