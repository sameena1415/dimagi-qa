import time

from selenium.webdriver.common.by import By
from QA_Requests.PerfTickets.testPages.base.base_page import BasePage
from QA_Requests.PerfTickets.userInputs.test_data import TestData


class DataGenerationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.data_dropdown = (By.LINK_TEXT, 'Data')
        self.view_all_link = (By.LINK_TEXT, 'View All')
        self.close_notification = (By.XPATH, "//div[@class='frame-close']/button[1]")
        self.iframe = (By.XPATH, "//iframe[contains(@src,'/embed/frame')]")
        self.view_latest_updates = (By.XPATH, "//*[.='View latest updates']")
        self.import_cases_from_excel_link = (By.LINK_TEXT, "Import Cases from Excel")
        self.choose_file = (By.XPATH, "//input[@name='file']")
        self.next_step = (By.XPATH, "//i[@class='fa fa-forward']")
        self.case_type = (By.XPATH, "//select[@id='case_type']")
        self.excel_column = (By.XPATH, "//select[@id='search_column']")
        self.case_id = (By.XPATH, "//button[text()='Case ID']")
        self.external_id = (By.XPATH, "//button[text()='External ID']")
        self.handle_cases_checkbox = (By.XPATH, "//input[@id='create_new_cases']")

    def excel_upload(self, filepath, case_type, column):

        self.wait_to_click(self.data_dropdown)
        self.wait_to_click(self.view_all_link)
        self.wait_to_click(self.import_cases_from_excel_link)
        self.send_keys(self.choose_file, str(filepath))
        time.sleep(20)
        self.wait_to_click(self.next_step)
        time.sleep(10)
        self.success_status = (By.XPATH,
                               "(//td[contains(text(), '" + case_type + "')]/preceding-sibling::td/span[@class='label label-success'])[1]")
        self.case_id_download = (By.XPATH,
                                 "(// td[contains(text(), '" + case_type + "')]/following-sibling::td//a[.//text() = '" + TestData.file_name + "'])[1]")

        self.select_by_text(self.case_type, case_type)
        self.select_by_text(self.excel_column, column)
        if column == 'caseid':
            self.wait_to_click(self.case_id)
        else:
            self.wait_to_click(self.external_id)
        self.wait_to_click(self.handle_cases_checkbox)
        self.wait_to_click(self.next_step)
        self.wait_to_click(self.next_step)
        assert self.is_visible_and_displayed(self.success_status), "Cases upload not completed!"
        print("Cases uploaded successfully!")
