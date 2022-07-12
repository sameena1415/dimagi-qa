import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.user_inputs import UserData
from HQSmokeTests.testPages.users.org_structure_page import latest_download_file


""""Contains test page elements and functions related to data dictionary module"""


class DataDictionaryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.case_type_name = "case type " + str(fetch_random_string())
        self.case_type_created = "//a[@href='#" + self.case_type_name + "']"
        self.dictionary_name = "Dictionary " + str(fetch_random_string())
        self.dictionary_description = "Test dictionary"

        self.data_dictionary_link = (By.XPATH, "//a[text()[contains(.,'Data Dictionary')]]")
        self.export_button = (By.ID, "download-dict")
        self.import_button = (By.XPATH, "//i[@class ='fa fa-cloud-upload']")
        self.choose_file = (By.XPATH, "//input[@data-bind ='value: file']")
        self.upload = (By.XPATH, "//button[@data-bind ='disable: !file()']")
        self.success_message = (By.XPATH , "//div[@class= 'alert alert-margin-top fade in alert-success']")


    def open_data_dictionary_case_page(self):
        self.click(self.data_dictionary_link)

    def export_data_dictionary(self):
        try:
            self.wait_to_click(self.export_button)
            time.sleep(5)
        except TimeoutException:
            print("TIMEOUT ERROR: Still preparing for download..Celery might be down..")
            assert False
        newest_file = latest_download_file()
        self.assert_downloaded_file(newest_file, "data_dictionary"), "Download Not Completed!"
        print("File download successful")


    def import_data_dictionary(self):
        try:
            self.wait_to_click(self.import_button)
            newest_file = latest_download_file()
            file_that_was_downloaded = UserData.DOWNLOAD_PATH / newest_file
            time.sleep(5)
            self.send_keys(self.choose_file, str(file_that_was_downloaded))
            self.wait_and_sleep_to_click(self.upload)
            time.sleep(10)
        except (TimeoutException, NoSuchElementException):
            print("TIMEOUT ERROR: Could not upload file")
        assert self.is_present_and_displayed(self.success_message), "Upload Not Completed!"
        print("File uploaded successfully")
