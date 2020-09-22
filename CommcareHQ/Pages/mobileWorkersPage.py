import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SeleniumCCHQ.CommcareHQ.UserInputs.userInputs import UserInputs


class MobileWorkerPage:

    def __init__(self, driver):
        self.driver = driver
        # remove these after locators page creation: redundant code
        self.web_apps_menu_id = "CloudcareTab"
        self.show_full_menu_id = "commcare-menu-toggle"
        ####################################################
        self.webapp_working_as = "//div[@class='restore-as-banner module-banner']/span/b"
        self.webapp_login_confirmation = 'js-confirmation-confirm'
        self.webapp_login_with_username = '(//h3/b)'
        self.webapp_login = "(//div[@class='js-restore-as-item appicon appicon-restore-as'])"
        self.confirm_reactivate_xpath_list = "((//div[@class='modal-footer'])/button[@data-bind=" \
                                             "'click: function(user) { user.is_active(true); }'])"
        self.reactivate_buttons_list = "(//td/div[@data-bind='visible: !is_active() && is_account_confirmed()']" \
                                       "/button[@class='btn btn-default'])"
        self.confirm_deactivate_xpath_list = "((//div[@class='modal-footer'])/button[@class='btn btn-danger'])"
        self.deactivate_buttons_list = "(//td/div[@data-bind='visible: is_active()']/button[@class='btn btn-default'])"
        self.show_deactivated_users_btn = '//button[@data-bind="visible: !deactivatedOnly(), click: function() ' \
                                          '{ deactivatedOnly(true); }"]'
        self.usernames_xpath = "//td/a/strong[@data-bind='text: username']"
        self.page_xpath = \
            "(//span[@data-bind='text: $data, visible: !$parent.showSpinner() || $data != $parent.currentPage()'])"
        ###############################
        self.users_menu_id = "ProjectUsersTab"
        self.mobile_workers_menu_link_text = "Mobile Workers"
        self.create_mobile_worker_id = "new-user-modal-trigger"
        self.mobile_worker_username_id = "id_username"
        self.mobile_worker_password_id = "id_new_password"
        self.create_button_xpath = '//button[@type="submit"]'
        self.error_message = "//span[@data-bind ='visible: $root.usernameAvailabilityStatus() !== $root.STATUS.NONE']"
        self.cancel_button = "//button[text()='Cancel']"
        self.new_user_created_xpath = "//*[@class='success']//a[contains(@data-bind,'attr: {href: edit_url}, visible: "\
                                      "user_id')]//following-sibling::strong"
        self.edit_user_field_xpath = "//*[@id='btn-edit_user_fields']"
        self.add_field_xpath = "//button[@data-bind='click: addField']"
        self.user_property_xpath = "(//input[@data-bind='value: slug'])[last()]"
        self.label_xpath = "(//input[@data-bind='value: label'])[last()]"
        self.add_choice_button_xpath = "(//button[@data-bind='click: addChoice'])[last()]"
        self.choice_xpath = "(//input[@data-bind='value: value'])[last()]"
        self.save_field_id = "save-custom-fields"
        self.user_field_success_msg = "//div[@class='alert alert-margin-top fade in alert-success']"
        self.mobile_worker_on_left_panel = "//a[@data-title='Mobile Workers']"
        self.next_page_button_xpath = "//a[contains(@data-bind,'click: nextPage')]"
        self.additional_info_dropdown = "select2-id_data-field-"+UserInputs.user_property+"-container"
        self.select_value_dropdown = "//li[text()='"+UserInputs.choice+"']"
        self.update_info_button = "//button[text()='Update Information']"
        self.user_file_additional_info = "//label[@for='id_data-field-" + UserInputs.user_property + "']"
        self.deactivate_btn_xpath = "//td/a/strong[text()='"+UserInputs.mobile_worker_username+"']" \
                                    "/following::td[5]/div[@data-bind='visible: is_active()']/button"
        self.confirm_deactivate = "(//button[@class='btn btn-danger'])[1]"
        self.show_full_menu_id = "commcare-menu-toggle"
        self.view_all_link_text = "View All"
        ######
        self.search_user_web_apps ="//input[@placeholder='Filter workers']"
        self.search_button_we_apps="//div[@class='input-group-btn']"

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
        self.driver.find_element_by_id(self.create_mobile_worker_id).click()
        time.sleep(2)

    def mobile_worker_enter_username(self, username):
        self.driver.find_element_by_id(self.mobile_worker_username_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_username_id).send_keys(username)
        time.sleep(2)

    def mobile_worker_enter_password(self, password):
        self.driver.find_element_by_id(self.mobile_worker_password_id).clear()
        self.driver.find_element_by_id(self.mobile_worker_password_id).send_keys(password)
        time.sleep(2)

    def click_create(self):
        create_button = self.driver.find_element_by_xpath(self.create_button_xpath)
        if create_button.is_enabled():
            create_button.click()
            time.sleep(3)
            new_user_created = self.driver.find_element_by_xpath(self.new_user_created_xpath)
            print("Username is : " + new_user_created.text)
            assert UserInputs.mobile_worker_username == new_user_created.text
        elif self.driver.find_element_by_xpath(self.error_message).is_displayed:
            self.driver.find_element_by_xpath(self.cancel_button).click()
            assert False, " Create Button Disabled"
        time.sleep(3)

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
        assert self.driver.find_element_by_xpath(self.user_field_success_msg).is_displayed

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

    def enter_value_for_created_user_field(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element_by_id(self.additional_info_dropdown)).perform()
        time.sleep(2)
        self.driver.find_element_by_id(self.additional_info_dropdown).click()
        self.driver.find_element_by_xpath(self.select_value_dropdown).click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath(self.user_file_additional_info).is_displayed()

    def update_information(self):
        self.driver.find_element_by_xpath(self.update_info_button).click()
        time.sleep(5)

    def deactivate_user(self):
        self.driver.find_element_by_xpath (self.mobile_worker_on_left_panel).click ( )
        time.sleep(2)
        total_pages = self.driver.find_elements_by_xpath(self.page_xpath)
        print("Total pages: ", len(total_pages))
        for i in range(1, len(total_pages)+1):
            try:
                self.driver.find_element_by_xpath(self.page_xpath+"["+str(i)+"]").click()
                time.sleep(2)
                username = self.driver.find_elements_by_xpath(self.usernames_xpath)
                for j in range(len(username)):
                    print("Username is " + username[j].text)
                    if username[j].text == UserInputs.mobile_worker_username:
                        deactivate = self.driver.find_element_by_xpath(self.deactivate_buttons_list +
                                                                       '['+str(j+1)+']')
                        deactivate.click()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, self.confirm_deactivate_xpath_list +
                                                 "["+str(j+1)+"]").click()
                        print("User deactivated")
                        break
            except Exception as e:
                print("Only one element on last page scenario" + str(e))
                time.sleep(5)
                self.driver.refresh()
                time.sleep(5)

    def verify_deactivation(self):
        total_pages = self.driver.find_elements_by_xpath(self.page_xpath)
        print("Total pages: ", len(total_pages))
        for i in range(1, len(total_pages)+1):
            try:
                time.sleep(3)
                self.driver.find_element_by_xpath(self.page_xpath+"["+str(i)+"]").click()
                time.sleep(2)
                username = self.driver.find_elements_by_xpath(self.usernames_xpath)
                for j in range(len(username)):
                    print("Username is " + username[j].text)
                    assert username[j].text != UserInputs.mobile_worker_username, "Username not removed"
                    print("Username not present")
            except NoSuchElementException as e:
                print("Only one element on last page scenario" + str(e))

    def verify_deactivation_via_login(self):
        self.driver.find_element(By.ID, self.web_apps_menu_id).click()
        self.driver.find_element(By.XPATH, self.webapp_login).click()
        time.sleep(2)
        self.driver.find_element (By.XPATH, self.search_user_web_apps).send_keys(UserInputs.mobile_worker_username)
        self.driver.find_element (By.XPATH, self.search_button_we_apps).click()
        time.sleep (2)
        login_with_username = self.driver.find_elements(By.XPATH, self.webapp_login_with_username)
        print("Checking webapp login...")
        for j in range(len(login_with_username)):
            print("Username is " + login_with_username[j].text)
            if login_with_username[j].text != UserInputs.mobile_worker_username:
                assert True
        print("Username not in list - Successfully deactivated!")

    def reactivate_user(self):
        self.driver.find_element (By.ID, self.show_full_menu_id).click()
        self.driver.find_element_by_id (self.users_menu_id).click()
        self.driver.find_element (By.LINK_TEXT, self.view_all_link_text).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.show_deactivated_users_btn).click()
        time.sleep(2)
        total_pages = self.driver.find_elements_by_xpath(self.page_xpath)
        print("Total pages: ", len(total_pages))
        for i in range(1, len(total_pages) + 1):
            try:
                self.driver.find_element_by_xpath(self.page_xpath + "[" + str(i) + "]").click()
                time.sleep(2)
                username = self.driver.find_elements_by_xpath(self.usernames_xpath)
                for j in range(len(username)):
                    print("Username is " + username[j].text)
                    if username[j].text == UserInputs.mobile_worker_username:
                        reactivate = self.driver.find_element_by_xpath(self.reactivate_buttons_list +
                                                                       "["+str(j+1)+"]")
                        reactivate.click()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, self.confirm_reactivate_xpath_list +
                                                 "["+str(j+1)+"]").click()
                        print("User reactivated")
                        break
            except Exception as e:
                print("Only one element on last page scenario" + str(e))
                time.sleep(5)

    def verify_reactivation(self):
        self.driver.refresh()
        time.sleep(5)
        total_pages = self.driver.find_elements_by_xpath(self.page_xpath)
        print("Total pages: ", len(total_pages))
        for i in range(1, len(total_pages)+1):
            try:
                self.driver.find_element(By.XPATH, self.page_xpath+"["+str(i)+"]").click()
                time.sleep(2)
                username = self.driver.find_elements(By.XPATH, self.usernames_xpath)
                for j in range(len(username)):
                    print("Username is " + username[j].text)
                    if username[j].text == UserInputs.mobile_worker_username:
                        assert True
                        break
            except NoSuchElementException as e:
                print("Only one element on last page scenario" + str(e))

    def verify_reactivation_via_login(self):
        time.sleep (2)
        self.driver.find_element (By.ID, self.web_apps_menu_id).click()
        self.driver.find_element (By.XPATH, self.webapp_login).click()
        time.sleep (2)
        self.driver.find_element (By.XPATH, self.search_user_web_apps).send_keys (UserInputs.mobile_worker_username)
        self.driver.find_element (By.XPATH, self.search_button_we_apps).click ( )
        time.sleep (2)
        login_with_username = self.driver.find_elements (By.XPATH, self.webapp_login_with_username)
        for j in range (len (login_with_username)) :
            print ("Checking webapp login...")
            print ("Username is " + login_with_username[j].text)
            if login_with_username[j].text == UserInputs.mobile_worker_username :
                self.driver.find_element (By.XPATH, self.webapp_login_with_username + "[" + str (j + 1) + "]").click ( )
                break
        time.sleep (2)
        self.driver.find_element (By.ID, self.webapp_login_confirmation).click ( )
        time.sleep (2)
        login_username = WebDriverWait (self.driver, 10).until (EC.presence_of_element_located (
            (By.XPATH, self.webapp_working_as)))
        if login_username.text == UserInputs.mobile_worker_username :
            assert True, "Login with the reactivated user failed!"
            print("Working as " + UserInputs.mobile_worker_username + " : Reactivation successful!")










