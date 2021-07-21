import os

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UserInputs.userInputsData import UserInputsData
import pandas as pd
from TestBase.environmentSetupPage import load_settings


def latest_download_file():
    os.chdir(UserInputsData.download_path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = max(files, key=os.path.getctime)
    print("File downloaded: " + newest)
    return newest


class ExportDataPage:

    def __init__(self, driver):  # initialize each WebElement here
        self.driver = driver
        self.data_dropdown = '//*[@id="ProjectDataTab"]/a'  # Data dropdown
        self.view_all_link = '//*[@id="ProjectDataTab"]/ul/li[6]/a'  # View All link

        # Delete Export
        # self.delete_button = "//input[@style='']//following::a[@class='btn btn-danger'][1]"
        self.delete_button = "//a[@class='btn btn-danger'][1]"
        self.delete_confirmation_button = "//button[@data-bind='click: deleteExport']"

        # Add Export
        self.add_export_button = '//*[@id="create-export"]/p/a'  # Add Export button
        self.app_dropdown = '//*[@id="div_id_application"]/div/span/span[1]/span'  # Application dropdown in the modal
        self.select_app = '//*[@id="select2-id_application-results"]/li'  # Selecting first app
        self.menu_dropdown = '//*[@id="div_id_module"]/div/span/span[1]/span'  # Menu dropdown in the modal
        self.select_menu = '//*[@id="select2-id_module-results"]/li[1]'  # Selecting first menu item
        self.form_dropdown = '//*[@id="div_id_form"]/div/span/span[1]/span'  # Form dropdown in the modal
        self.select_form = '//*[@id="select2-id_form-results"]/li[1]'  # Selecting first form item
        self.add_export_conf = '//*[@id="createExportOptionsModal"]/div/form/div/div[7]/button[2]'  # Confirm and add export
        self.export_name = '//*[@id="export-name"]'  # Custom name for the export
        self.export_settings_create = '//*[@id="customize-export"]/form/div/div[1]/button'  # Creating export with the default settings
        self.date_range = "id_date_range"
        self.date_range_key = "//li[@data-range-key='Last 30 Days']"

        # Export Form data variables
        self.export_form_data_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[1]/a'  # Export Form Data link on the left panel
        self.export_form_data_button = '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[2]/a[1]'  # click form exports
        self.prepare_export_button = '//*[@id="download-export-form"]/form/div[2]/div/div[2]/div[1]/button'  # click prepare exports
        self.download_button = '//*[@id="download-progress"]/div/div/div[2]/div[1]/form/a'  # click download
        self.find_data_by_ID_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[4]/a'  # Click findDataByID link
        self.find_data_by_ID_textbox = '//*[@id="find-form"]/div[2]/div[1]/input'  # Find data by ID textbox
        self.find_data_by_ID_button = '//*[@id="find-form"]/div[2]/div[2]/button'
        self.view_FormID = '//*[@id="find-form"]/div[2]/div[1]/div[2]/a'
        self.womanName_HQ = '//*[@id="form-data"]/div[3]/div/div/table/tbody/tr[2]/td[2]/div' # Property 'Woman's name' value on HQ
        self.woman_case_name_HQ = "//th[@title='name']//following::td[1]"

        # Export Case data variables
        self.export_case_data_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[2]/a'  # Export Case Data link on the left panel
        self.export_case_data_button = '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr/td[3]/a[1]'
        self.view_caseID ='//*[@id="find-form"]/div[2]/div[1]/div[2]/a'

        # Export SMS variables
        self.export_sms_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[3]/a'  # Export Case Data on the left panel

        # Daily Saved Export variables, form
        self.edit_form_export = '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div[2]/div/a'  # Edit an existing form export
        self.create_DSE_checkbox = '//*[@id="daily-saved-export-checkbox"]'  # Create a Daily Saved Export checkbox

        # Daily Saved Export variables, case
        self.edit_case_export = '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div[2]/div/a'  # Edit an existing case export

        # Excel Dashboard Integrations, form
        self.export_excel_dash_int_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[6]/a'  # Excel Dashboard Integrations link on the left panel
        self.model_dropdown = '//*[@id="id_model_type"]'
        self.select_form_model = '//*[@id="id_model_type"]/option[3]'
        self.update_data = "//button[@data-toggle='modal'][1]"
        self.update_data_conf = "//button[@data-bind='click: emailedExport.updateData']"
        self.copy_dashfeed_link = "//a[@class='btn btn-default btn-sm'][1]"
        self.dashboard_feed_link = "//span[@class='input-group-btn']//preceding::a[@class='btn btn-info btn-xs']"

        # Excel Dashboard Integrations, case
        self.select_case_model = '//*[@id="id_model_type"]/option[2]'
        self.case_type_dropdown = '//*[@id="div_id_case_type"]/div/span/span[1]/span'
        self.select_case_type ='//*[@id="select2-id_case_type-results"]/li'

        # Power BI / Tableau Integration, Form
        self.powerBI_tab_int_link = '//*[@id="hq-sidebar"]/nav/ul[1]/li[7]/a'
        self.copy_odatafeed_link = '//*[@id="export-list"]/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/span/a'
        self.edit_button = "//input[@style='']//following::a[@data-bind='click: editExport'][1]"

        # Manage Forms
        self.manage_forms_link = '//*[@id="hq-sidebar"]/nav/ul[2]/li[3]/a'
        self.apply_button = '//*[@id="apply-btn"]'
        self.select_all_checkbox = "//input[@name='select_all']"
        self.checkbox1 = "(//input[@class='xform-checkbox'])[1]"
        self.archive_button = '//*[@id="submitForms"]'
        self.success_message = "//div[@class='alert alert-success']"
        self.view_form_link = "//a[@class='ajax_dialog']"
        self.archived_restored_dropdown = '//*[@id="select2-report_filter_archive_or_restore-container"]'
        self.archived_forms_option = '/html/body/span/span/span[2]/ul/li[2]'

    def wait_to_click(self, *locator, timeout=20):
        try:
            clickable = EC.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except TimeoutException:
            self.driver.refresh()


    def wait_to_clear(self, *locator, timeout=5):
        clickable = EC.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).clear()

    def switch_to_next_tab(self):
        winHandles = self.driver.window_handles
        window_after = winHandles[1]
        self.driver.switch_to.window(window_after)

    def switch_back_to_prev_tab(self):
        winHandles = self.driver.window_handles
        window_before = winHandles[0]
        self.driver.switch_to.window(window_before)

    def get_url_paste_browser(self):
        self.wait_to_click(By.XPATH, self.copy_odatafeed_link)
        time.sleep(1)
        self.wait_to_click(By.XPATH, self.edit_button)
        time.sleep(1)
        get_url = self.driver.current_url
        ID = get_url.strip ("https://staging.commcarehq.org/a/qa-automation/data/export/custom/odata_form_feed/edit/")
        odata_feed_link="https://staging.commcarehq.org/a/another-upstream/api/v0.5/odata/forms/"+ID+"/feed/"
        self.driver.back()
        self.driver.execute_script("window.open('');")  # Open a new tab
        self.switch_to_next_tab()
        username = load_settings()["login_username"]
        password = load_settings()["login_password"]
        final_URL = f"https://{username}:{password}@{odata_feed_link[8:]}"
        self.driver.get(final_URL)

    def data_tab(self):
        self.wait_to_click(By.XPATH, self.data_dropdown)
        self.wait_to_click(By.XPATH, self.view_all_link)

    def deletion(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.delete_button).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.delete_confirmation_button).click()
        print("Delete Confirmation Button clicked")

    # Test Case 20_a - Verify Export functionality for Forms
    def add_form_exports(self):
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Export created!!")

    def form_exports(self):
        self.wait_to_click(By.XPATH, self.export_form_data_button)
        # Date filter
        # self.wait_to_click(By.ID, self.date_range)
        # self.wait_to_click(By.XPATH, self.date_range_key)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        print("Download form button clicked")
        time.sleep(3)

    # Test Case 22_a -  Find Data By ID, forms
    def validate_downloaded_form_exports(self):
        self.wait_to_click(By.XPATH, self.find_data_by_ID_link)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data = pd.read_excel(newest_file)
        df = pd.DataFrame(data, columns=['form.womans_name', 'formid'])
        formID = df['formid'].values[0]
        woman_name_excel = df['form.womans_name'].values[0]

        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((
            By.XPATH, self.find_data_by_ID_textbox))).send_keys(str(formID))
        self.wait_to_click(By.XPATH, self.find_data_by_ID_button)
        self.wait_to_click(By.XPATH, self.view_FormID)
        self.switch_to_next_tab()
        time.sleep(3)
        womanName_HQ = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((
            By.XPATH, self.womanName_HQ))).text
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 20_b - Verify Export functionality for Cases
    def add_case_exports(self):
        self.wait_to_click(By.XPATH, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Export created!!")

    def case_exports(self):
        self.wait_to_click(By.XPATH, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.export_case_data_button)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        time.sleep(3)

    # Test Case 22_b - Find Data by ID for Case Exports
    def validate_downloaded_case_exports(self):
        self.wait_to_click(By.XPATH, self.find_data_by_ID_link)
        newest_file = latest_download_file()
        print("Newest file:" + newest_file)
        data2 = pd.read_excel(newest_file)
        df2 = pd.DataFrame(data2, columns=['name', 'caseid'])
        caseID = df2['caseid'].values[0]
        woman_name_excel = df2['name'].values[0]

        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((
                By.XPATH, self.find_data_by_ID_textbox))).send_keys(str(caseID))
        self.wait_to_click(By.XPATH, self.find_data_by_ID_button)
        self.wait_to_click(By.XPATH, self.view_caseID)
        time.sleep(3)
        self.switch_to_next_tab()
        womanName_HQ = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH, self.woman_case_name_HQ))).text
        assert woman_name_excel == womanName_HQ
        print("Downloaded file has the required data!")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case 21 - Export SMS Messages
    def sms_exports(self):
        self.wait_to_click(By.XPATH, self.export_sms_link)
        self.wait_to_click(By.XPATH, self.prepare_export_button)
        self.wait_to_click(By.XPATH, self.download_button)
        time.sleep(3)
        newest_file = latest_download_file()
        print("Newest:", newest_file)
        modTimesinceEpoc = (UserInputsData.download_path / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert "Messages" in newest_file and diff_seconds in range(0, 600)
        print("Export successful")

    # Test Case 23_a - Daily saved export, form
    def daily_saved_exports_form(self):
        self.wait_to_click(By.XPATH, self.export_form_data_link)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.edit_form_export)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.form_export_name)
        self.wait_to_click(By.XPATH, self.create_DSE_checkbox)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        assert UserInputsData.form_export_name in self.driver.page_source
        print("Form Export creation successful")

    # Test Case 23_b - Daily saved export, case
    def daily_saved_exports_case(self):
        self.wait_to_click(By.XPATH, self.export_case_data_link)
        self.wait_to_click(By.XPATH, self.edit_case_export)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.case_export_name)
        self.wait_to_click(By.XPATH, self.create_DSE_checkbox)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)
        assert UserInputsData.case_export_name in self.driver.page_source
        print("Form Export creation successful")

    # Test Case - 24 - Excel Dashboard Integration, form
    def excel_dashboard_integration_form(self):
        self.wait_to_click(By.XPATH, self.export_excel_dash_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_form_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Dashboard Feed added!!")
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((
                    By.XPATH, self.export_name))).send_keys(UserInputsData.dashboard_feed_form)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Dashboard Form Feed created!!")
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(1)
        self.driver.refresh()
        try:
            self.driver.find_element(By.XPATH, self.copy_dashfeed_link).click()
            dashboard_feed_link = self.driver.find_element(By.XPATH, self.dashboard_feed_link).get_attribute("href")
            print("Feed Link: "+dashboard_feed_link)
            self.driver.execute_script("window.open('');")  # Open a new tab
            self.switch_to_next_tab()
            self.driver.get(dashboard_feed_link)
            dashboard_feed_data = self.driver.page_source
            if dashboard_feed_data != "":
                print("Excel Dashboard (form) has data")
            else:
                print("Excel Dashboard (form) is empty")
            self.driver.close()
            self.switch_back_to_prev_tab()
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    # Test Case - 25 - Excel Dashboard Integration, case

    def excel_dashboard_integration_case(self):
        self.wait_to_click(By.XPATH, self.export_excel_dash_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Dashboard Feed added!!")
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.dashboard_feed_case)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Dashboard Form Feed created!!")
        self.wait_to_click(By.XPATH, self.update_data)
        self.wait_to_click(By.XPATH, self.update_data_conf)
        time.sleep(1)
        self.driver.refresh()
        try:
            self.driver.find_element(By.XPATH, self.copy_dashfeed_link).click()
            dashboard_feed_link = self.driver.find_element(By.XPATH, self.dashboard_feed_link).get_attribute("href")
            print(dashboard_feed_link)
            self.driver.execute_script("window.open('');")  # Open a new tab
            self.switch_to_next_tab()
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
    def power_bi_tableau_integration_form(self):
        self.wait_to_click(By.XPATH, self.powerBI_tab_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_form_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.menu_dropdown)
        self.wait_to_click(By.XPATH, self.select_menu)
        self.wait_to_click(By.XPATH, self.form_dropdown)
        self.wait_to_click(By.XPATH, self.select_form)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Odata form Feed added!!")
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.odata_feed_form)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Odata Form Feed created!!")
        self.driver.refresh()
        self.get_url_paste_browser()
        odata_feed_data = self.driver.page_source
        assert odata_feed_data != ""
        print("Odata form feed has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

    # Test Case - 27 - Power BI / Tableau Integration, Case`
    def power_bi_tableau_integration_case(self):
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.powerBI_tab_int_link)
        self.wait_to_click(By.XPATH, self.add_export_button)
        print("Add OData_feed_button clicked")
        self.wait_to_click(By.XPATH, self.model_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_model)
        self.wait_to_click(By.XPATH, self.app_dropdown)
        self.wait_to_click(By.XPATH, self.select_app)
        self.wait_to_click(By.XPATH, self.case_type_dropdown)
        self.wait_to_click(By.XPATH, self.select_case_type)
        self.wait_to_click(By.XPATH, self.add_export_conf)
        print("Odata Case Feed added!!")
        time.sleep(5)
        self.wait_to_clear(By.XPATH, self.export_name)
        self.driver.find_element(By.XPATH, self.export_name).send_keys(UserInputsData.odata_feed_case)
        self.wait_to_click(By.XPATH, self.export_settings_create)
        print("Odata Case Feed created!!")
        self.driver.refresh()
        self.get_url_paste_browser()
        odata_feed_data = self.driver.page_source
        assert odata_feed_data != ""  # This condition can be improvised
        print("Odata case feed has data")
        self.driver.close()  # Close the feed URL
        self.switch_back_to_prev_tab()
        self.driver.refresh()

    # Test Case - 30 - Verify user is able to manage forms and archive a form
    def manage_forms(self):
        # Forms archival
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.wait_to_click(By.XPATH, self.checkbox1)
        self.wait_to_click(By.XPATH, self.archive_button)
        assert WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH, self.success_message))).is_displayed()
        print("Forms archival successful!!")

        # View Normal Forms
        self.wait_to_click(By.XPATH, self.manage_forms_link)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != ""  # This condition can be improvised
        print("normal_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

        # View Archived Forms
        self.wait_to_click(By.XPATH, self.archived_restored_dropdown)
        self.wait_to_click(By.XPATH, self.archived_forms_option)
        self.wait_to_click(By.XPATH, self.apply_button)
        self.driver.refresh()
        self.wait_to_click(By.XPATH, self.view_form_link)
        self.switch_to_next_tab()
        normal_form_data = self.driver.page_source
        assert normal_form_data != "" # This condition can be improvised
        print("archived_form has data")
        self.driver.close()
        self.switch_back_to_prev_tab()

        # Restore Archived Forms
        self.wait_to_click(By.XPATH, self.checkbox1)
        self.wait_to_click(By.XPATH, self.archive_button)
        assert WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((
            By.XPATH, self.success_message))).is_displayed()
        print("Forms archival successful!!")
