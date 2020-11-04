from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from CommcareHQ.UserInputs.generateUserInputs import fetch_random_string


class OrganisationStructurePage:

    def __init__(self, driver):
        self.driver = driver
        self.org_menu_link_text = "Organization Structure"
        self.add_loc_btn_xpath = "//span[@data-bind='text: new_child_caption' and text()='New location at top level']"
        self.loc_name_xpath = "//input[@type='text']"
        self.create_loc_xpath = "//button[@type='submit']"
        self.loc_saved_success_msg = "//div[@class ='alert alert-margin-top fade in alert-success']"
        self.error_1_id = "error_1_id_name"
        self.edit_first_loc_xpath = "(//*[@id='button-template']/a)[1]"
        self.loc_name_input_id = "id_name"
        self.update_loc_xpath = "//*[@id='users']//preceding::button"
        self.location_created_xpath = "//span[text()='" + "location_" + fetch_random_string() + "']"
        self.location_renamed_xpath = "//span[text()='" + "location_" + str(fetch_random_string()) + "new" + "']"
        self.edit_loc_field_btn_xpath = "//a[@data-action='Edit Location Fields']"
        self.add_field_btn_xpath = "//button[@data-bind='click: addField']"
        self.loc_property_xpath = "(//input[@data-bind='value: slug'])[last()]"
        self.loc_label_xpath = "(//input[@data-bind='value: label'])[last()]"
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

    def organisation_menu_open(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        time.sleep(4)
        print(self.driver.title)
        assert "Organization Structure : Locations :: - CommCare HQ" in self.driver.title

    def create_location(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.add_loc_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).send_keys("location_" + fetch_random_string())
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
        self.driver.find_element(By.XPATH, self.edit_first_loc_xpath).click()
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
        self.driver.find_element(By.XPATH, self.add_choice_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.choice_xpath).send_keys("location_field_" + fetch_random_string())
        self.driver.find_element(By.ID, self.save_btn_id).click()
        assert self.driver.find_element(By.XPATH, self.success_msg_xpath).is_displayed()

    def selection_location_field_for_location_created(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.edit_first_loc_xpath).click()
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

    # def download_locations(self):
    #     self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
    #     self.driver.find_element(By.LINK_TEXT, self.download_loc_btn).click()
    #     time.sleep(3)
    #     try:
    #         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, self.download_loc_btn)))\
    #             .click()
    #         time.sleep(5)
    #     except TimeoutException as e:
    #         print("Still preparing for download.." + str(e))
    #         assert False
    #
    # def verify_downloaded_locations(self):
    #     pattern = '*_locations.xlsx'
    #     files = os.listdir('C:/Users/dsi-user.DESKTOP-IGCBOU4/Downloads/')
    #     for name in files:
    #         if fnmatch.fnmatch(name, pattern):
    #             print(name, fnmatch.fnmatchcase (name, pattern))
    #             print("Last modified: %s" % time.ctime (
    #                 os.path.getmtime ('C:/Users/dsi-user.DESKTOP-IGCBOU4/Downloads/' + name)))
    #             print("Created: %s" % time.ctime(
    #                 os.path.getctime ('C:/Users/dsi-user.DESKTOP-IGCBOU4/Downloads/' + name)))
    #             dateTimeObj = datetime.now ( )
    #             timestampStr = dateTimeObj.strftime ("%b %d ")
    #             print('Current Timestamp : ', timestampStr)
    #
    #     # assert if file is downloaded and matches with the file name pattern
    #
    # def upload_locations(self):
    #     self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
    #     self.driver.find_element(By.LINK_TEXT, self.upload_loc_btn).click()
    #     path = Path(str(Path.home()) + '\Downloads\*.xlsx')
    #     list_of_files = glob.glob(str(path))
    #     latest_file = max(list_of_files, key=os.path.getctime)
    #     print(latest_file)
    #     # if downloaded=file name pattern else fail
    #     self.driver.find_element(By.ID, "id_bulk_upload_file").send_keys(latest_file)
    #     # assert
