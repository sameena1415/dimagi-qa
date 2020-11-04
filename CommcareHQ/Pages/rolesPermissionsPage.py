from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from CommcareHQ.UserInputs.generateUserInputs import fetch_random_string


class RolesPermissionPage:

    def __init__(self, driver):
        self.driver = driver
        self.roles_menu_xpath = "//a[@data-title='Roles & Permissions']"
        self.add_role_btn_xpath = "//*[@id='user-roles-table']/div[2]/button"
        self.role_name_id = "role-name"
        self.edit_web_user_checkbox = "edit-web-users-checkbox"
        self.save_btn_xpath = "//button[@class='btn btn-primary disable-on-submit']"
        self.role_created = "//span[text()='" + "role_name_" + fetch_random_string() + "']"
        self.edit_role_xpath = "//span[text()='" + "role_name_" + fetch_random_string() + "']//following::td[11]/button[1]"
        self.delete_role_xpath = "//span[text()='" + "role_name_" + fetch_random_string() + "']//following::td[11]/button[2]"
        self.edit_mobile_worker_checkbox = "edit-commcare-users-checkbox"
        self.role_renamed = "//span[text()='" + "role_name_" + fetch_random_string() + "']"
        self.confirm_role_delete = "//div[@class='btn btn-danger']"

    def roles_menu_click(self):
        self.driver.find_element(By.XPATH, self.roles_menu_xpath).click()
        time.sleep(2)

    def add_role(self):
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.add_role_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.add_role_btn_xpath)).perform()
        self.driver.find_element(By.ID, self.role_name_id).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys("role_name_" + fetch_random_string())
        self.driver.find_element(By.ID, self.edit_web_user_checkbox).click()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.role_created).is_displayed()

    def edit_role(self):
        self.driver.find_element(By.XPATH, self.edit_role_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.role_name_id).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys("role_name_" + fetch_random_string())
        self.driver.find_element(By.ID, self.edit_mobile_worker_checkbox).click()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        time.sleep(2)
        assert True == self.driver.find_element(By.XPATH, self.role_renamed).is_displayed()

    def cleanup_role(self):
        self.driver.find_element(By.XPATH, self.delete_role_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.confirm_role_delete).click()
        time.sleep(2)
