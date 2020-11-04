import time

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By

from CommcareHQ.UserInputs.generateUserInputs import fetch_random_string


class GroupPage:

    def __init__(self, driver):
        self.driver = driver
        self.group_name_id = "id_group_name"
        self.add_group_button = "//button[@type='submit' and @class='btn btn-primary']"
        self.group_menu_xpath = "//a[@data-title='Groups']"
        self.users_drop_down_xpath = "//input[@class='select2-search__field']"
        self.select_user_xpath = "//li[text()='" + "username_" + fetch_random_string() + "']"
        self.update_button_id = "submit-id-submit"
        self.edit_settings_link_text = "Edit Settings"
        self.group_name_input_id = "group-name-input"
        self.save_button_xpath = "//button[@type='submit' and text()='Save']"
        self.success_alert_id = "save-alert"
        self.remove_user_xpath = "//span[@role='presentation']"
        self.delete_group = "//a[@class='btn btn-danger pull-right']"
        self.confirm_delete = "//button[@class='btn btn-danger disable-on-submit']"
        self.delete_success_message = "//div[@class='alert alert-margin-top fade in html alert-success']"

    def click_group_menu(self):
        self.driver.find_element_by_xpath(self.group_menu_xpath).click()
        time.sleep(2)

    def enter_group_name(self, groupname):
        time.sleep(2)
        self.driver.find_element_by_id(self.group_name_id).send_keys(groupname)
        time.sleep(2)

    def add_group(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.add_group_button).click()
        time.sleep(2)

    def click_on_users_drop_down(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.users_drop_down_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.users_drop_down_xpath).send_keys("username_" + fetch_random_string())
        time.sleep(2)

    def add_user_to_group(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.select_user_xpath).click()
        time.sleep(2)

    def update_group(self):
        time.sleep(2)
        try:
            self.driver.find_element_by_id(self.update_button_id).click()
            time.sleep(2)
            self.click_group_menu()
            time.sleep(2)
            assert True == self.driver.find_element_by_link_text("group_" + fetch_random_string()).is_displayed()
        except UnexpectedAlertPresentException as e:
            print(e)

    def click_on_created_group(self):
        self.driver.find_element(By.LINK_TEXT, "group_" + fetch_random_string()).click()

    def edit_existing_group(self):
        self.driver.find_element(By.LINK_TEXT, self.edit_settings_link_text).click()
        time.sleep(2)

    def rename_existing_group(self):
        self.driver.find_element(By.ID, self.group_name_input_id).clear()
        self.driver.find_element(By.ID, self.group_name_input_id).send_keys(
            "group_" + fetch_random_string() + "_rename")
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
        time.sleep(3)
        assert True == self.driver.find_element(By.ID, self.success_alert_id).is_displayed()

    def remove_user_from_group(self):
        self.driver.find_element(By.XPATH, self.remove_user_xpath).click()
        self.driver.find_element(By.ID, self.update_button_id).click()
        time.sleep(2)
        assert True == self.driver.find_element(By.ID, self.success_alert_id).is_displayed()

    def cleanup_group(self):
        self.driver.find_element(By.LINK_TEXT, "group_" + fetch_random_string() + "_rename").click()
        self.driver.find_element(By.XPATH, self.delete_group).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.confirm_delete).click()
        time.sleep(4)
        assert True == self.driver.find_element(By.XPATH, self.delete_success_message).is_displayed()
