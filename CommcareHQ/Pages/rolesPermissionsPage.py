from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class RolesPermissionPage:

    def __init__(self, driver):
        self.driver = driver
        self.roles_menu_xpath = "//a[@data-title='Roles & Permissions']"
        self.add_role_btn_xpath = "//*[@id='user-roles-table']/div[2]/button"
        self.role_name_id = "role-name"
        self.edit_web_user_checkbox = "edit-web-users-checkbox"
        self.save_btn_xpath = "//button[@class='btn btn-primary disable-on-submit']"
        self.role_created = "//span[text()='"+UserInputs.role_name+"']"
        self.edit_role_xpath = "//span[text()='"+UserInputs.role_name+"']//following::td[9]/button[1]"
        self.edit_mobile_worker_checkbox = "edit-commcare-users-checkbox"
        self.role_renamed = "//span[text()='" + UserInputs.role_rename + "']"

    def roles_menu_click(self):
        self.driver.find_element(By.XPATH, self.roles_menu_xpath).click()
        time.sleep(2)

    def add_role(self):
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.add_role_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.add_role_btn_xpath)).perform()
        self.driver.find_element(By.ID, self.role_name_id).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys(UserInputs.role_name)
        self.driver.find_element(By.ID, self.edit_web_user_checkbox).click()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, self.role_created).is_displayed()==True

    def edit_role(self):
        self.driver.find_element(By.XPATH, self.edit_role_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.ID, self.role_name_id).clear()
        self.driver.find_element(By.ID, self.role_name_id).send_keys(UserInputs.role_rename)
        self.driver.find_element(By.ID, self.edit_mobile_worker_checkbox).click()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).click(
            self.driver.find_element(By.XPATH, self.save_btn_xpath)).perform()
        time.sleep(2)
        assert self.driver.find_element (By.XPATH, self.role_renamed).is_displayed()==True











