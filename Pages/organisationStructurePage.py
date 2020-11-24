import os
import sys
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from UserInputs.generateUserInputs import fetch_random_string
from UserInputs.userInputsData import UserInputsData


def latest_download_file():
    global cwd
    try:
        cwd = os.getcwd()
        os.chdir(UserInputsData.download_path)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newest = files[-1]
        print("File downloaded: " + newest)
        return newest
    except EnvironmentError as err:
        print('Something wrong with specified directory. Exception- ', err + sys.exc_info())
    finally:
        print("Restoring the path...")
        os.chdir(cwd)
        print("Current directory is-", os.getcwd())


newest_file = latest_download_file()


class OrganisationStructurePage:

    def __init__(self, driver):
        self.driver = driver
        self.org_menu_link_text = "Organization Structure"
        self.add_loc_btn_xpath = "//span[@data-bind='text: new_child_caption' and text()='New location at top level']"
        self.loc_name_xpath = "//input[@type='text']"
        self.create_loc_xpath = "//button[@type='submit']"
        self.loc_saved_success_msg = "//div[@class ='alert alert-margin-top fade in alert-success']"
        self.error_1_id = "error_1_id_name"
        self.loc_created = "location_" + fetch_random_string()
        self.loc_created_edit_path = "//span[text ()='" + self.loc_created + "']" + \
                                     "//following::a[@data-bind='attr: { href: loc_edit_url(uuid()) }'][1]"
        self.loc_name_input_id = "id_name"
        self.update_loc_xpath = "//*[@id='users']//preceding::button"
        self.location_created_xpath = "//span[text()='" + self.loc_created + "']"
        self.location_renamed_xpath = "//span[text()='" + self.loc_created + "new" + "']"
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
        self.update_loc_btn_xpath = "//*[@id='new_user']//preceding::button[2]"
        self.duplicate_msg_xpath = "//div[@class='alert alert-danger']"
        self.org_level_menu_link_text = "Organization Levels"
        self.new_org_level_btn_xpath = "//button[@data-bind='click: new_loctype']"
        self.org_level_value_xpath = "(//input[@data-bind='value: name'])[last()]"
        self.save_btn_xpath = "//button[@type='submit' and @class='btn btn-default pull-right btn-primary']"
        self.download_loc_btn = "Download Organization Structure"
        self.upload_loc_btn = "Bulk Upload"
        self.upload = "//button[@class='btn btn-primary disable-on-submit']"
        self.import_complete = "//legend[text()='Import complete.']"

    def organisation_menu_open(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        time.sleep(4)
        print(self.driver.title)
        assert "Organization Structure : Locations :: - CommCare HQ" in self.driver.title

    def create_location(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.add_loc_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).send_keys(self.loc_created)
        self.driver.find_element(By.XPATH, self.create_loc_xpath).click()
        time.sleep(2)
        try:
            assert self.driver.find_element(By.XPATH, self.loc_saved_success_msg).is_displayed()
            self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
            assert self.driver.find_element(By.XPATH, self.location_created_xpath).is_displayed()
        except NoSuchElementException:
            if self.driver.find_element(By.ID, self.error_1_id).is_displayed():
                self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
                time.sleep(2)
                assert False, "name conflicts with another location with this parent"

    def edit_location(self):
        self.driver.find_element(By.XPATH, self.loc_created_edit_path).click()
        self.driver.find_element(By.ID, self.loc_name_input_id).clear()
        self.driver.find_element(By.ID, self.loc_name_input_id).send_keys(
            "location_" + str(fetch_random_string()) + "new")
        self.driver.find_element(By.XPATH, self.update_loc_xpath).click()
        assert self.driver.find_element(By.XPATH, self.loc_saved_success_msg).is_displayed()
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        assert self.driver.find_element(By.XPATH, self.location_renamed_xpath).is_displayed()

    def edit_location_fields(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.driver.find_element(By.XPATH, self.edit_loc_field_btn_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_field_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.loc_property_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_property_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.loc_label_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_label_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element_by_xpath(self.choice_selection).click()
        self.driver.find_element(By.XPATH, self.add_choice_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.choice_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element(By.ID, self.save_btn_id).click()
        assert self.driver.find_element(By.XPATH, self.success_msg_xpath).is_displayed()

    def selection_location_field_for_location_created(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.loc_created_edit_path).click()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.additional_info_drop_down)).click(
            self.driver.find_element(By.XPATH, self.additional_info_drop_down)).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.select_value_drop_down).click()
        self.driver.find_element(By.XPATH, self.update_loc_btn_xpath).click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, self.success_msg_xpath).is_displayed()

    def create_org_level(self):
        self.driver.find_element(By.LINK_TEXT, self.org_level_menu_link_text).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.new_org_level_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.org_level_value_xpath).send_keys("loc_level_" + fetch_random_string())
        self.driver.find_element(By.XPATH, self.save_btn_xpath).click()
        time.sleep(2)

    def download_locations(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.download_loc_btn).click()
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((
                By.LINK_TEXT, self.download_loc_btn))).click()
            time.sleep(7)
        except TimeoutException as e:
            print("Still preparing for download.." + str(e))
            assert False
        # verify_downloaded_location
        modTimesinceEpoc = os.path.getmtime(str(UserInputsData.download_path) + "\\" + newest_file)
        modificationTime = datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M')
        print("Last Modified Time : ", modificationTime)
        timeNow = datetime.now().strftime('%Y-%m-%d %H:%M')
        print('Current Time : ', timeNow)
        if "locations" in newest_file and modificationTime == timeNow:
            assert True
            print("File downloaded successfully")

    def upload_locations(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.upload_loc_btn).click()
        self.driver.find_element(By.ID, "id_bulk_upload_file").send_keys(str(
            UserInputsData.download_path) + "\\" + newest_file)
        self.driver.find_element(By.XPATH, self.upload).click()
        assert WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
            By.XPATH, self.import_complete))).is_displayed()
        print("File uploaded successfully")
