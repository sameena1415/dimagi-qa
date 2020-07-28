from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import *


class OrganisationStructurePage:
    generate_location()

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
        self.location_created_xpath = "//span[text()='"+fetch_location()+"']"
        self.location_renamed_xpath = "//span[text()='"+str(fetch_location())+"new"+"']"

    def organisation_menu_open(self):
        self.driver.find_element(By.LINK_TEXT, self.org_menu_link_text).click()
        time.sleep(4)
        print(self.driver.title)
        assert "Organization Structure : Locations :: - CommCare HQ" in self.driver.title

    def create_location(self):
        x=UserInputs()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.add_loc_btn_xpath).click()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.loc_name_xpath).send_keys(fetch_location())
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
        self.driver.find_element(By.ID, self.loc_name_input_id).send_keys(str(fetch_location())+"new")
        self.driver.find_element(By.XPATH, self.update_loc_xpath).click()
        assert self.driver.find_element(By.XPATH, self.loc_saved_success_msg).is_displayed()
        self.driver.find_element (By.LINK_TEXT, self.org_menu_link_text).click()
        assert self.driver.find_element(By.XPATH, self.location_renamed_xpath).is_displayed()















