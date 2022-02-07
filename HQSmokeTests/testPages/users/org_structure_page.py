import datetime
import os
import time
from datetime import date

from HQSmokeTests.userInputs.generate_random_string import fetch_random_string
from HQSmokeTests.userInputs.user_inputs import UserData
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def latest_download_file():
    cwd = os.getcwd()
    try:
        os.chdir(UserData.DOWNLOAD_PATH)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getctime)
        print(files)
        if files[-1].endswith(".log"):
            newest = sorted(files, key=os.path.getctime)[-2]
        elif files[-1].endswith(".xlsx"):
            newest = sorted(files, key=os.path.getctime)[-1]
        else:
            newest = max(files, key=os.path.getctime)
        print("File downloaded: " + newest)
        return newest
    finally:
        print("Restoring the path...")
        os.chdir(cwd)
        print("Current directory is-", os.getcwd())


class OrganisationStructurePage:

    def __init__(self, driver):
        self.driver = driver
        self.org_menu_link_text = "Organization Structure"
        self.add_loc_btn_xpath = "//span[@data-bind='text: new_child_caption' and text()='New location at top level']"
        self.loc_name_xpath = "//input[@type='text']"
        self.create_loc_xpath = "//button[@type='submit']"
        self.loc_saved_success_msg = "//div[@class ='alert alert-margin-top fade in alert-success']"
        self.error_1_id = "error_1_id_name"
        self.new_location_name = "location_" + fetch_random_string()
        self.edit_this_loc = "(//span[contains(text(),'updated_on:')])[1]"
        self.edit_loc_button_xpath = self.edit_this_loc + \
                                     "//preceding::a[@data-bind='attr: { href: loc_edit_url(uuid()) }'][1]"
        self.loc_name_input_id = "id_name"
        self.update_loc_xpath = "(//button[@type='submit'])[1]"
        self.location_created_xpath = "//span[text()='" + self.new_location_name + "']"
        self.renamed_location = "//span[text()='updated_on:" + str(date.today()) + "']"
        self.edit_loc_field_btn_xpath = "//a[@data-action='Edit Location Fields']"
        self.add_field_btn_xpath = "//button[@data-bind='click: addField']"
        self.loc_property_xpath = "(//input[@data-bind='value: slug'])[last()]"
        self.loc_label_xpath = "(//input[@data-bind='value: label'])[last()]"
        self.choice_selection = "(//div[contains(@data-bind, \"validationMode('choice')\")])[last()]"
        self.add_choice_btn_xpath = "(//button[@data-bind='click: addChoice'])[last()]"
        self.choice_xpath = "(//input[@data-bind='value: value'])[last()]"
        self.save_btn_id = "save-custom-fields"
        self.success_msg_xpath = "//div[@class='alert alert-margin-top fade in alert-success']"
        self.additional_info_drop_down = "//*[@id='select2-id_data-field-" + "location_field_" + str(
            fetch_random_string()) + "-container']"
        self.select_value_drop_down = "//li[text()='" + "location_field_" + str(fetch_random_string()) + "']"
        self.duplicate_msg_xpath = "//div[@class='alert alert-danger']"
        self.org_level_menu_link_text = "Organization Levels"
        self.new_org_level_btn_xpath = "//button[@data-bind='click: new_loctype']"
        self.org_level_value_xpath = "(//input[@data-bind='value: name'])[last()]"
        self.save_btn_xpath = "//button[@type='submit' and @class='btn btn-default pull-right btn-primary']"
        self.save_btn_delete = "//button[@class='btn btn-default pull-right']"
        self.download_loc_btn = "Download Organization Structure"
        self.upload_loc_btn = "Bulk Upload"
        self.upload = "//button[@class='btn btn-primary disable-on-submit']"
        self.import_complete = "//legend[text()='Import complete.']"
        self.download_filter = "//button[@data-bind='html: buttonHTML']"

        # cleanup
        self.delete_location_created = "//span[text ()='" + self.new_location_name + \
                                       "']//preceding::button[@class='btn btn-danger'][1]"
        self.delete_confirm = '//input[@data-bind ="value: signOff, valueUpdate: \'input\'"]'
        self.delete_confirm_button = "//button[@data-bind ='click: delete_fn, css: {disabled: !(signOff() == count)}']"
        self.delete_loc_field = "(//a[@class='btn btn-danger'])[last()]"
        self.delete_org_level = "(//button[@class='btn btn-danger'])[last()]"
        self.delete_success = "//div[@class='alert fade in message-alert alert-success']"

    def wait_to_click(self, *locator, timeout=10):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except TimeoutException:
            print(TimeoutException)

    def organisation_menu_open(self):
        self.wait_to_click(By.LINK_TEXT, self.org_menu_link_text)
        print(self.driver.title)
        assert "Organization Structure : Locations :: - CommCare HQ" in self.driver.title

    def create_location(self):
        self.wait_to_click(By.XPATH, self.add_loc_btn_xpath)
        self.driver.find_element(By.XPATH, self.loc_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).send_keys(self.new_location_name)
        self.driver.find_element(By.XPATH, self.create_loc_xpath).click()
        assert WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
            By.XPATH, self.loc_saved_success_msg))).is_displayed(), "Location not created!"
        self.wait_to_click(By.LINK_TEXT, self.org_menu_link_text)
        self.driver.refresh()
        try:
            assert WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
                By.XPATH, self.location_created_xpath))).is_displayed(), "Location not created!"
        except StaleElementReferenceException:
            assert WebDriverWait(self.driver, 3).until(ec.presence_of_element_located((
                By.XPATH, self.location_created_xpath))).is_displayed(), "Location not created!"

    def edit_location(self):
        try:
            self.wait_to_click(By.LINK_TEXT, self.org_menu_link_text)
            self.driver.find_element(By.XPATH, self.edit_loc_button_xpath).click()
            self.driver.find_element(By.ID, self.loc_name_input_id).clear()
            self.driver.find_element(By.ID, self.loc_name_input_id).send_keys("updated_on:" + str(date.today()))
            self.driver.find_element(By.XPATH, self.update_loc_xpath).click()
            time.sleep(2)
            assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((
                By.XPATH, self.loc_saved_success_msg))).is_displayed(),  "Location editing not successful!"
            self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
            self.driver.refresh()
            assert WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((
                By.XPATH, self.renamed_location))).is_displayed(), "Location editing not successful!"
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    def edit_location_fields(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.wait_to_click(By.XPATH, self.edit_loc_field_btn_xpath)
        self.wait_to_click(By.XPATH, self.add_field_btn_xpath)
        self.driver.find_element(By.XPATH, self.loc_property_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_property_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.loc_label_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_label_xpath).send_keys("location_field_" + fetch_random_string())
        # self.driver.find_element(By.XPATH, self.choice_selection).click() # required when reg exp FF enabled
        self.driver.find_element(By.XPATH, self.add_choice_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.choice_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element(By.ID, self.save_btn_id).click()
        assert self.driver.find_element(By.XPATH, self.success_msg_xpath).is_displayed(), "Location field edit not successful!"
        self.driver.refresh()

    def selection_location_field_for_location_created(self):
        try:
            self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
            self.wait_to_click(By.XPATH, self.edit_loc_button_xpath)
            self.wait_to_click(By.XPATH, self.additional_info_drop_down)
            self.driver.find_element(By.XPATH, self.select_value_drop_down).click()
            self.driver.find_element(By.XPATH, self.update_loc_xpath).click()
            assert WebDriverWait(self.driver, 2).until(ec.presence_of_element_located((
                By.XPATH, self.success_msg_xpath))).is_displayed(), "Location field not assigned!"
        except StaleElementReferenceException:
            print(StaleElementReferenceException)

    def create_org_level(self):
        self.driver.find_element(By.LINK_TEXT, self.org_level_menu_link_text).click()
        self.wait_to_click(By.XPATH, self.new_org_level_btn_xpath)
        self.driver.find_element(By.XPATH, self.org_level_value_xpath).send_keys("loc_level_" + fetch_random_string())
        self.wait_to_click(By.XPATH, self.save_btn_xpath)

    def download_locations(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.download_loc_btn).click()
        self.wait_to_click(By.XPATH, self.download_filter)
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((
                By.LINK_TEXT, self.download_loc_btn))).click()
            time.sleep(10)
        except TimeoutException as e:
            print("Still preparing for download..")
            assert False
        # verify_downloaded_location
        newest_file = latest_download_file()
        modTimesinceEpoc = (UserData.DOWNLOAD_PATH / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert "_locations" in newest_file and diff_seconds in range(0, 600), "Download not completed!"
        print("File download successful")

    def upload_locations(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.upload_loc_btn).click()
        newest_file = latest_download_file()
        file_that_was_downloaded = UserData.DOWNLOAD_PATH / newest_file
        self.driver.find_element(By.ID, "id_bulk_upload_file").send_keys(str(file_that_was_downloaded))
        time.sleep(2)
        self.wait_to_click(By.XPATH, self.upload)
        assert WebDriverWait(self.driver, 100).until(ec.presence_of_element_located((
            By.XPATH, self.import_complete))).is_displayed(), "Upload not completed!"
        print("File uploaded successfully")

    def cleanup_location(self):
        # Delete User Field
        self.wait_to_click(By.LINK_TEXT, self.org_menu_link_text)
        self.wait_to_click(By.XPATH, self.edit_loc_field_btn_xpath)
        self.wait_to_click(By.XPATH, self.delete_loc_field)
        self.wait_to_click(By.XPATH, self.delete_org_level)
        self.wait_to_click(By.ID, self.save_btn_id)
        print("Location field deleted successfully")
        # Delete Location
        self.wait_to_click(By.LINK_TEXT, self.org_menu_link_text)
        time.sleep(2)
        try:
            self.wait_to_click(By.XPATH, self.delete_location_created)
        except (StaleElementReferenceException, TimeoutException):
            self.driver.refresh()
            self.wait_to_click(By.XPATH, self.delete_location_created)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.delete_confirm).send_keys("1")
        self.driver.find_element(By.XPATH, self.delete_confirm_button).click()
        assert WebDriverWait(self.driver, 100).until(ec.presence_of_element_located((
            By.XPATH, self.delete_success))).is_displayed(), "Location Not Deleted!"
        print("Location deleted successfully")
        # Delete Org Level
        org_level_menu = self.driver.find_element(By.LINK_TEXT, self.org_level_menu_link_text)
        self.driver.execute_script("arguments[0].click();", org_level_menu)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.delete_org_level).click()
        self.wait_to_click(By.XPATH, self.save_btn_delete)
        print("Org level deleted successfully")
