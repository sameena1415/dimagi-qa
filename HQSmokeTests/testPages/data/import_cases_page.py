import os

from openpyxl import load_workbook
from selenium.webdriver.common.by import By

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.userInputs.user_inputs import UserData


def edit_spreadsheet(edited_file, cell, renamed_file):
    workbook = load_workbook(filename=edited_file)
    sheet = workbook.active
    sheet[cell] = fetch_random_string()
    workbook.save(filename=renamed_file)


class ImportCasesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.file_new_name = "reassign_cases_" + str(fetch_random_string()) + ".xlsx"

        self.village_name_cell = "C2"
        self.to_be_edited_file = os.path.abspath(os.path.join(UserData.BASE_DIR, "test_data/reassign_cases.xlsx"))
        self.renamed_file = os.path.abspath(os.path.join(UserData.BASE_DIR, "test_data/" + self.file_new_name))

        self.import_cases_menu = (By.LINK_TEXT, "Import Cases from Excel")
        self.download_file = (By.XPATH, "(//span[@data-bind='text: upload_file_name'])[1]")
        self.choose_file = (By.ID, "file")
        self.next_step = (By.XPATH, "(//button[@type='submit'])[1]")
        self.case_type = (By.ID, "select2-case_type-container")
        self.case_type_option_value = (By.XPATH, "//option[@value='pregnancy']")
        self.success = (By.XPATH, "//span[text()='" + self.file_new_name + "']//preceding::span[@class='label label-success']")

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
        assert self.is_visible_and_displayed(self.success), "Waitinng to start import. Celery might have a high queue."
