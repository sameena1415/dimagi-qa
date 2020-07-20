import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class MobileWorkerPage:

    def __init__(self, driver):
        self.driver = driver
        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'
        self.new_user_created_xpath = "//*[@class='success']//a[contains(@data-bind,'attr: {href: edit_url}, visible: "\
                                      "user_id')]//following-sibling::strong"
        self.edit_user_field_xpath = "//*[@id='btn-edit_user_fields']"
        self.add_field_xpath = "//button[@type='button' and @class='btn btn-primary']"
        self.user_property_xpath = "//input[@data-bind='value: slug']"
        self.label_xpath = "//input[@data-bind='value: label']"
        self.add_choice_button_xpath = "//button[@data-bind='click: addChoice']"
        self.choice_xpath = "//input[@data-bind='value: value']"
        self.save_field_id = "save-custom-fields"
        self.mobile_worker_on_left_panel = "//a[@data-title='Mobile Workers']"
        self.next_page_button_xpath = "//a[contains(@data-bind,'click: nextPage')]"
        self.additional_info_dropdown = "select2-id_data-field-"+UserInputs.user_property+"-container"
        self.select_value_dropdown = "//li[text()='" + UserInputs.choice + "']"
        self.update_info_button = "//button[text()='Update Information']"

    def mobile_worker_menu(self):
        time.sleep(2)
        users_menu = self.driver.find_element_by_id(self.users_menu_id)
        if users_menu.is_enabled():
            try:
                users_menu.click()
                self.driver.find_element_by_link_text(self.mobile_workers_menu_link_text).click()
                time.sleep(2)
            except Exception as e:
                print(e)

    def create_mobile_worker(self):
        try:
            self.driver.find_element_by_id(self.create_mobile_worker_id).click()
            time.sleep(2)
        except Exception as e:
            print(e)

    def mobile_worker_enter_username(self, username):
        try:
            self.driver.find_element_by_id(self.mobile_worker_username_id).clear()
            self.driver.find_element_by_id(self.mobile_worker_username_id).send_keys(username)
            time.sleep(2)
        except Exception as e:
            print(e)
        return username

    def mobile_worker_enter_password(self, password):
        try:
            self.driver.find_element_by_id(self.mobile_worker_password_id).clear()
            self.driver.find_element_by_id(self.mobile_worker_password_id).send_keys(password)
            time.sleep(2)
        except Exception as e:
            print(e)

    def click_create(self):
        create_button = self.driver.find_element_by_xpath(self.create_button_xpath)
        if create_button.is_enabled():
            try:
                create_button.click()
                time.sleep(2)
                new_user_created = self.driver.find_element_by_xpath(self.new_user_created_xpath)
                print("Username is : " + new_user_created.text)
                assert UserInputs.mobile_worker_username == new_user_created.text
            except Exception as e:
                print(e)
        else:
            print("Button disabled")
            assert False

    def edit_user_field(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.edit_user_field_xpath).click()
        time.sleep(2)

    def add_field(self):
        try:
            self.driver.find_element_by_xpath(self.add_field_xpath).click()
            time.sleep(1)
        except Exception as e:
            print(e)

    def add_user_property(self, user_pro):
        try:
            self.driver.find_element_by_xpath(self.user_property_xpath).clear()
            self.driver.find_element_by_xpath(self.user_property_xpath).send_keys(user_pro)
            time.sleep(2)
        except Exception as e:
            print(e)

    def add_label(self, label):
        try:
            self.driver.find_element_by_xpath(self.label_xpath).clear()
            self.driver.find_element_by_xpath(self.label_xpath).send_keys(label)
            time.sleep(2)
        except Exception as e:
            print(e)

    def add_choice(self, choice):
        try:
            self.driver.find_element_by_xpath(self.add_choice_button_xpath).click()
            self.driver.find_element_by_xpath(self.choice_xpath).clear()
            self.driver.find_element_by_xpath(self.choice_xpath).send_keys(choice)
            time.sleep(2)
        except Exception as e:
            print(e)

    def save_field(self):
        try:
            if self.driver.find_element_by_id(self.save_field_id).is_enabled:
                self.driver.find_element_by_id(self.save_field_id).click()
                time.sleep(10)
        except Exception as e:
            print(e)

    def go_back_to_mobile_workers(self):
        try:
            self.driver.find_element_by_xpath(self.mobile_worker_on_left_panel).click()
            time.sleep(5)
        except Exception as e:
            print(e)

    def select_mobile_worker_created(self):
        while True:
            try:
                mobile_worker_created = self.driver.find_element_by_link_text(UserInputs.mobile_worker_username)
                if mobile_worker_created.is_displayed():
                    mobile_worker_created.click()
                    time.sleep(2)
                    break
            except NoSuchElementException:
                next_page_btn = self.driver.find_element_by_xpath(self.next_page_button_xpath)
                actions = ActionChains(self.driver)
                actions.move_to_element(next_page_btn).perform()
                time.sleep(2)
                next_page_btn.click()
                time.sleep(2)

    def enter_value_for_created_userfield(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_id(self.additional_info_dropdown)).perform()
        time.sleep(2)
        self.driver.find_element_by_id(self.additional_info_dropdown).click()
        self.driver.find_element_by_xpath(self.select_value_dropdown).click()
        time.sleep(5)

    def update_information(self):
        try:
            self.driver.find_element_by_xpath(self.update_info_button).click()
            time.sleep(5)
        except Exception as e:
            print(e)