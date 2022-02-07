import os
import time
import pandas as pd

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.user_inputs import UserData

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


def latest_download_file():
    os.chdir(UserData.DOWNLOAD_PATH)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = max(files, key=os.path.getctime)
    print("File downloaded: " + newest)
    return newest


class ExportDataPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.date_having_submissions = "2022-01-18 to 2022-02-18"

        self.data_dropdown = (By.LINK_TEXT, 'Data')
        self.view_all_link = (By.LINK_TEXT, 'View All')

        # Delete Export
        self.delete_button = (By.XPATH, "//a[@class='btn btn-danger'][1]")
        self.delete_confirmation_button = (By.XPATH, "//button[@data-bind='click: deleteExport']")

        # Add Export
        self.add_export_button = (By.XPATH, "//a[@href='#createExportOptionsModal']")
        self.app_dropdown = (By.XPATH, "//span[@aria-labelledby='select2-id_application-container']")
        self.select_app = (By.XPATH, "//li[text()='Village Health']")
        self.menu_dropdown = (By.XPATH, "//span[@aria-labelledby='select2-id_module-container']")
        self.select_menu = (By.XPATH, '//*[@id="select2-id_module-results"]/li[1]')
        self.form_dropdown = (By.XPATH, "//span[@aria-labelledby='select2-id_form-container']")
        self.select_form = (By.XPATH, '//*[@id="select2-id_form-results"]/li[1]')
        self.add_export_conf = (By.XPATH, "//button[@data-bind='visible: showSubmit, disable: disableSubmit']")
        self.export_name = (By.XPATH, '//*[@id="export-name"]')
        self.export_settings_create = (By.XPATH,  "//button[@class='btn btn-lg btn-primary']")
        self.date_range = (By.ID, "id_date_range")

        # Export Form and Case data variables
        self.export_form_data_link = (By.LINK_TEXT, 'Export Form Data')
        self.export_case_data_link = (By.LINK_TEXT, 'Export Case Data')
        self.export_form_case_data_button = (By.XPATH, "(//a[@class='btn btn-primary'])[2]")
        self.prepare_export_button = (By.XPATH, "//button[@data-bind='disable: disablePrepareExport']")
        self.download_button = (By.XPATH, "//a[@class='btn btn-primary btn-full-width']")
        self.apply = (By.XPATH, "//button[@class='applyBtn btn btn-sm btn-primary']")
        self.users_filter = (By.XPATH, "//span[@class='select2-selection select2-selection--multiple']")

        # Find Data By ID
        self.find_data_by_ID = (By.LINK_TEXT, 'Find Data by ID')
        self.find_data_by_ID_textbox = (By.XPATH, "//input[@placeholder='Form Submission ID']")
        self.find_data_by_ID_button = (By.XPATH, "(//button[@data-bind='click: find, enable: allowFind'])[2]")
        self.view_FormID_CaseID = (By.LINK_TEXT, 'View')
        self.womanName_HQ = (By.XPATH, "(//div[@class='form-data-readable form-data-raw'])[1]")
        self.woman_case_name_HQ = (By.XPATH, "//th[@title='name']//following::td[1]")

        # Export SMS variables
        self.export_sms_link = (By.LINK_TEXT, "Export SMS Messages")

        # Daily Saved Export variables, form, case
        self.daily_saved_export_link = (By.LINK_TEXT, 'Daily Saved Exports')
        self.edit_form_case_export = (By.XPATH, "(//a[@data-bind='click: editExport'])[1]")
        self.create_DSE_checkbox = (By.XPATH, '//*[@id="daily-saved-export-checkbox"]')
        self.download_dse_form = (By.XPATH, "(//span[text()='" + UserData.form_export_name + "']//following::a[@class='btn btn-info btn-xs'])[1]")
        self.download_dse_case = (By.XPATH, "(//span[text()='" + UserData.case_export_name + "']//following::a[@class='btn btn-info btn-xs'])[1]")
        self.data_upload_msg = (By.XPATH, "//*[contains(text(),'Data update complete')]")

        # Excel Dashboard Integrations, form, case
        self.export_excel_dash_int = (By.LINK_TEXT, 'Excel Dashboard Integration')
        self.model_dropdown = (By.XPATH, '//*[@id="id_model_type"]')
        self.select_form_model = (By.XPATH, '//*[@id="id_model_type"]/option[3]')
        self.select_case_model = (By.XPATH, '//*[@id="id_model_type"]/option[2]')
        self.case_type_dropdown = (By.XPATH, '//*[@id="div_id_case_type"]/div/span/span[1]/span')
        self.select_case_type = (By.XPATH, '//*[@id="select2-id_case_type-results"]/li')
        self.update_data = (By.XPATH, "//button[@data-toggle='modal'][1]")
        self.form_update_data = (By.XPATH, "(//span[text()='" + UserData.form_export_name + "']//following::button[@data-toggle='modal'])[1]")
        self.case_update_data = (By.XPATH, "(//span[text()='" + UserData.case_export_name + "']//following::button[@data-toggle='modal'])[1]")
        self.update_data_conf = (By.XPATH, "//button[@data-bind='click: emailedExport.updateData']")
        self.copy_dashfeed_link = (By.XPATH, "(//span[contains(@data-bind, 'copyLinkRequested')])[1]")
        self.dashboard_feed_link = (
            By.XPATH, "//span[@class='input-group-btn']//preceding::a[@class='btn btn-info btn-xs']")

        # Power BI / Tableau Integration, Form
        self.powerBI_tab_int = (By.LINK_TEXT, 'PowerBi/Tableau Integration')
        self.copy_odatafeed_link = (By.XPATH, "//a[@class='btn btn-default btn-sm']")
        self.edit_button_case = (By.XPATH, "(//span[text()='"+UserData.odata_feed_case+"']//following::a[@data-bind='click: editExport'])[1]")
        self.edit_button_form = (By.XPATH, "(//span[text()='"+UserData.odata_feed_form+"']//following::a[@data-bind='click: editExport'])[1]")
        self.select_none = (By.XPATH, "(//a[@data-bind='click: table.selectNone'])[1]")
        self.first_checkbox = (By.XPATH, "(//input[@type='checkbox'])[3]")
        self.third_checkbox = (By.XPATH, "(//input[@type='checkbox'])[5]")
        self.failed_to_export = (By.XPATH, "//div[@class='alert alert-danger']")

        # bulk export delete
        self.select_all_btn = (By.XPATH, '//button[@data-bind="click: selectAll"]')
        self.delete_selected_exports = (By.XPATH, '//a[@href= "#bulk-delete-export-modal"]')
        self.bulk_delete_confirmation_btn = (By.XPATH, '//button[@data-bind="click: BulkExportDelete"]')
        self.no_records = (By.XPATH, "//td[text()='No data available to display. Please try changing your filters.']")
        self.alert_button_accept = (By.ID, "hs-eu-confirmation-button")

    def generate_odata_feed_link(self, item):
        # self.wait_and_sleep_to_click(self.copy_odatafeed_link) # Alternative:Copy and Paste
        time.sleep(5)
        get_url = self.driver.current_url
        ID = get_url.split("/")[10]
        odata_feed_link_case = "https://" + self.get_environment() + "/a/" + self.get_domain() + "/api/v0.5/odata/"+item+"/" + ID + "/feed/"
        self.driver.back()
        self.switch_to_new_tab()
        return odata_feed_link_case

    def get_url_paste_browser(self, username, password, item):
        odata_feed_link = self.generate_odata_feed_link(item)
        final_URL_case = f"https://{username}:{password}@{odata_feed_link[8:]}"
        self.driver.get(final_URL_case)

    def date_filter(self):
        self.wait_and_sleep_to_click(self.date_range)
        self.wait_to_clear(self.date_range)
        self.wait_to_send_keys(self.date_range, self.date_having_submissions)
        self.wait_and_sleep_to_click(self.apply)

    def data_tab(self):
        self.driver.refresh()
        try:
            self.wait_and_sleep_to_click(self.data_dropdown)
        except ElementClickInterceptedException:
            self.driver.find_element(self.alert_button_accept).click()
            self.wait_and_sleep_to_click(self.data_dropdown)
        self.wait_and_sleep_to_click(self.view_all_link)

    # Test Case 20_a - Verify Export functionality for Forms
    def add_form_exports(self):
        self.wait_to_click(self.add_export_button)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.menu_dropdown)
        self.wait_and_sleep_to_click(self.select_menu)
        self.wait_and_sleep_to_click(self.form_dropdown)
        self.wait_and_sleep_to_click(self.select_form)
        self.wait_and_sleep_to_click(self.add_export_conf)
        self.wait_and_sleep_to_click(self.export_settings_create)
        print("Export created!!")

    def form_exports(self):
        self.wait_and_sleep_to_click(self.export_form_case_data_button)
        self.date_filter()
        self.wait_and_sleep_to_click(self.prepare_export_button)
        try:
            self.wait_and_sleep_to_click(self.download_button)
        except TimeoutException:
            if self.is_visible_and_displayed(self.failed_to_export):
                self.driver.refresh()
                self.wait_and_sleep_to_click(self.prepare_export_button)
                self.wait_and_sleep_to_click(self.download_button)
                time.sleep(5)
                print("Download form button clicked")

    # Test Case 22_a -  Find Data By ID, forms
    def validate_downloaded_form_exports(self):
        self.wait_and_sleep_to_click(self.find_data_by_ID)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data = pd.read_excel(newest_file)
        df = pd.DataFrame(data, columns=['form.womans_name', 'formid'])
        formID = df['formid'].values[0]
        woman_name_excel = df['form.womans_name'].values[0]
        self.wait_to_send_keys(self.find_data_by_ID_textbox, str(formID))
        self.wait_and_sleep_to_click(self.find_data_by_ID_button)
        self.wait_and_sleep_to_click(self.view_FormID_CaseID)
        self.switch_to_next_tab()
        time.sleep(3)
        womanName_HQ = self.wait_to_get_text(self.womanName_HQ)
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 20_b - Verify Export functionality for Cases
    def add_case_exports(self):
        self.wait_to_click(self.export_case_data_link)
        self.wait_and_sleep_to_click(self.add_export_button)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.case_type_dropdown)
        self.wait_and_sleep_to_click(self.select_case_type)
        self.wait_and_sleep_to_click(self.add_export_conf)
        self.wait_and_sleep_to_click(self.export_settings_create)
        print("Export created!!")

    def case_exports(self):
        self.wait_and_sleep_to_click(self.export_case_data_link)
        self.wait_and_sleep_to_click(self.export_form_case_data_button)
        self.date_filter()
        self.wait_and_sleep_to_click(self.prepare_export_button)
        self.wait_and_sleep_to_click(self.download_button)
        time.sleep(3)

    # Test Case 22_b - Find Data by ID for Case Exports
    def validate_downloaded_case_exports(self):
        self.wait_and_sleep_to_click(self.find_data_by_ID)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data2 = pd.read_excel(newest_file)
        df2 = pd.DataFrame(data2, columns=['name', 'caseid'])
        caseID = df2['caseid'].values[0]
        woman_name_excel = df2['name'].values[0]
        self.wait_to_send_keys(self.find_data_by_ID_textbox, str(caseID))
        self.wait_and_sleep_to_click(self.find_data_by_ID_button)
        self.wait_and_sleep_to_click(self.view_FormID_CaseID)
        time.sleep(3)
        self.switch_to_next_tab()
        time.sleep(3)
        womanName_HQ = self.wait_to_get_text(self.woman_case_name_HQ)
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 21 - Export SMS Messages
    def sms_exports(self):
        self.wait_and_sleep_to_click(self.export_sms_link)
        self.date_filter()
        self.wait_and_sleep_to_click(self.prepare_export_button)
        self.wait_and_sleep_to_click(self.download_button)
        time.sleep(5)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        self.assert_downloaded_file(newest_file, "Messages")
        print("SMS Export successful")

    # Test Case 23_a - Daily saved export, form
    def daily_saved_exports_form(self):
        try:
            self.wait_and_sleep_to_click(self.edit_form_case_export)
        except TimeoutException:
            self.add_form_exports()
            self.wait_and_sleep_to_click(self.edit_form_case_export)
        self.wait_to_clear(self.export_name)
        self.send_keys(self.export_name, UserData.form_export_name)
        self.wait_and_sleep_to_click(self.create_DSE_checkbox)
        self.wait_and_sleep_to_click(self.export_settings_create)
        self.wait_and_sleep_to_click(self.update_data)
        time.sleep(2)
        self.wait_and_sleep_to_click(self.update_data_conf)
        print("Display message:", self.get_text(self.data_upload_msg))
        self.driver.refresh()
        time.sleep(5)
        try:
            self.wait_and_sleep_to_click(self.download_dse_form)
        except TimeoutException:
            self.driver.refresh()
            self.wait_and_sleep_to_click(self.update_data_conf)
            self.driver.refresh()
            self.wait_and_sleep_to_click(self.download_dse_form)
        time.sleep(5)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        self.assert_downloaded_file(newest_file, "Form Export DSE")
        print("DSE Form Export successful")

    # Test Case 23_b - Daily saved export, case
    def daily_saved_exports_case(self):
        self.wait_and_sleep_to_click(self.export_case_data_link)
        try:
            self.wait_and_sleep_to_click(self.edit_form_case_export)
        except TimeoutException:
            self.add_case_exports()
            self.wait_and_sleep_to_click(self.edit_form_case_export)
        self.wait_to_clear(self.export_name)
        self.send_keys(self.export_name, UserData.case_export_name)
        self.wait_and_sleep_to_click(self.create_DSE_checkbox)
        self.wait_and_sleep_to_click(self.export_settings_create)
        self.wait_and_sleep_to_click(self.update_data)
        time.sleep(2)
        self.wait_and_sleep_to_click(self.update_data_conf)
        print("Display message:", self.get_text(self.data_upload_msg))
        self.driver.refresh()
        self.wait_and_sleep_to_click(self.download_dse_case)
        time.sleep(5)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        self.assert_downloaded_file(newest_file, "Case Export DSE")
        print("DSE Case Export successful")

    # Test Case - 24 - Excel Dashboard Integration, form
    def excel_dashboard_integration_form(self):
        self.wait_and_sleep_to_click(self.export_excel_dash_int)
        self.wait_and_sleep_to_click(self.add_export_button)
        self.wait_and_sleep_to_click(self.model_dropdown)
        self.wait_and_sleep_to_click(self.select_form_model)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.menu_dropdown)
        self.wait_and_sleep_to_click(self.select_menu)
        self.wait_and_sleep_to_click(self.form_dropdown)
        self.wait_and_sleep_to_click(self.select_form)
        self.wait_and_sleep_to_click(self.add_export_conf)
        print("Dashboard Feed added!!")
        self.wait_to_clear(self.export_name)
        self.wait_to_send_keys(self.export_name, UserData.dashboard_feed_form)
        self.click(self.export_settings_create)
        print("Dashboard Form Feed created!!")
        self.wait_and_sleep_to_click(self.update_data)
        self.wait_and_sleep_to_click(self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        try:
            time.sleep(2)
            self.click(self.copy_dashfeed_link)
            dashboard_feed_link = self.get_attribute(self.dashboard_feed_link, "href")
            print("Feed Link: " + dashboard_feed_link)
            self.switch_to_new_tab()
            self.driver.get(dashboard_feed_link)
            dashboard_feed_data = self.driver.page_source
            if dashboard_feed_data != "":
                print("Excel Dashboard form has data")
            else:
                print("Excel Dashboard (form) is empty")
            self.driver.close()
            self.switch_back_to_prev_tab()
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    # Test Case - 25 - Excel Dashboard Integration, case

    def excel_dashboard_integration_case(self):
        self.wait_and_sleep_to_click(self.export_excel_dash_int)
        self.wait_and_sleep_to_click(self.add_export_button)
        self.wait_and_sleep_to_click(self.model_dropdown)
        self.wait_and_sleep_to_click(self.select_case_model)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.case_type_dropdown)
        self.wait_and_sleep_to_click(self.select_case_type)
        self.wait_and_sleep_to_click(self.add_export_conf)
        print("Dashboard Feed added!!")
        self.wait_to_clear(self.export_name)
        self.wait_to_send_keys(self.export_name, UserData.dashboard_feed_case)
        self.click(self.export_settings_create)
        print("Dashboard Form Feed created!!")
        self.wait_and_sleep_to_click(self.update_data)
        self.wait_and_sleep_to_click(self.update_data_conf)
        time.sleep(2)
        self.driver.refresh()
        try:
            time.sleep(2)
            self.click(self.copy_dashfeed_link)
            dashboard_feed_link = self.get_attribute(self.dashboard_feed_link, "href")
            print(dashboard_feed_link)
            self.switch_to_new_tab()
            self.driver.get(dashboard_feed_link)
            dashboard_feed_data = self.driver.page_source
            if dashboard_feed_data != "":
                print("Excel Dashboard (case) has data")
            else:
                print("Excel Dashboard (case) is empty")
            self.driver.close()
            self.switch_back_to_prev_tab()
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    # Test Case - 28 - Power BI / Tableau Integration, Form
    def power_bi_tableau_integration_form(self, username, password):
        try:
            self.wait_and_sleep_to_click(self.powerBI_tab_int)
        except ElementClickInterceptedException:
            menu = self.wait_for_element(self.powerBI_tab_int)
            self.driver.execute_script("arguments[0].click();", menu)
        self.wait_and_sleep_to_click(self.add_export_button)
        self.wait_and_sleep_to_click(self.model_dropdown)
        self.wait_and_sleep_to_click(self.select_form_model)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.menu_dropdown)
        self.wait_and_sleep_to_click(self.select_menu)
        self.wait_and_sleep_to_click(self.form_dropdown)
        self.wait_and_sleep_to_click(self.select_form)
        self.wait_and_sleep_to_click(self.add_export_conf)
        print("Odata form Feed added!!")
        time.sleep(5)
        self.wait_to_clear(self.export_name)
        self.send_keys(self.export_name, UserData.odata_feed_form)
        self.click(self.export_settings_create)
        print("Odata Form Feed created!!")
        self.driver.refresh()
        self.wait_and_sleep_to_click(self.edit_button_form)
        self.get_url_paste_browser(username, password, "forms")
        self.assert_odata_feed_data()

    # Test Case - 27 - Power BI / Tableau Integration, Case`
    def power_bi_tableau_integration_case(self, username, password):
        self.driver.refresh()
        self.wait_and_sleep_to_click(self.powerBI_tab_int)
        self.wait_and_sleep_to_click(self.add_export_button)
        print("Add OData_feed_button clicked")
        self.wait_and_sleep_to_click(self.model_dropdown)
        self.wait_and_sleep_to_click(self.select_case_model)
        self.wait_and_sleep_to_click(self.app_dropdown)
        self.wait_and_sleep_to_click(self.select_app)
        self.wait_and_sleep_to_click(self.case_type_dropdown)
        self.wait_and_sleep_to_click(self.select_case_type)
        self.wait_and_sleep_to_click(self.add_export_conf)
        print("Odata Case Feed added!!")
        time.sleep(5)
        self.wait_to_clear(self.export_name)
        self.send_keys(self.export_name, UserData.odata_feed_case)
        # selcting first three property
        self.wait_and_sleep_to_click(self.select_none)
        self.wait_and_sleep_to_click(self.first_checkbox)
        self.wait_and_sleep_to_click(self.third_checkbox)
        # saving export
        self.click(self.export_settings_create)
        print("Odata Case Feed created!!")
        self.driver.refresh()
        self.wait_and_sleep_to_click(self.edit_button_case)
        self.get_url_paste_browser(username, password, "cases")
        self.assert_odata_feed_data()

    def delete_bulk_exports(self):
        try:
            self.wait_to_click(self.select_all_btn)
            self.wait_to_click(self.delete_selected_exports)
            self.wait_to_click(self.bulk_delete_confirmation_btn)
        except TimeoutException:
            print("No exports available")

    def delete_all_bulk_exports(self):
        self.wait_and_sleep_to_click(self.export_form_data_link)
        self.delete_bulk_exports()
        print("Bulk exports deleted for Export Form data")
        self.wait_and_sleep_to_click(self.export_case_data_link)
        self.delete_bulk_exports()
        print("Bulk exports deleted for Export Case data")
        self.wait_and_sleep_to_click(self.daily_saved_export_link)
        self.delete_bulk_exports()
        print("Bulk exports deleted for Daily Saved Export Cases")
        self.wait_and_sleep_to_click(self.powerBI_tab_int)
        self.delete_bulk_exports()
        print("Bulk exports deleted for Power BI Reports")
        self.wait_and_sleep_to_click(self.export_excel_dash_int)
        self.delete_bulk_exports()
        print("Bulk exports deleted for Export Excel Int Reports")

    def assert_odata_feed_data(self):
        odata_feed_data = self.driver.page_source
        assert odata_feed_data != ""  # This condition can be improvised
        print("Odata case feed has data")
        self.driver.close()  # Close the feed URL
        self.switch_back_to_prev_tab()
