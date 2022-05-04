import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.user_inputs import UserData

""""Contains test page elements and functions related to the User's Web Users module"""


class WebUsersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        self.users_menu_id = (By.ID, "ProjectUsersTab")
        self.web_users_menu = (By.LINK_TEXT, "Web Users")
        self.invite_web_user_button = (By.XPATH, "//i[@class='fa fa-plus']")
        self.email_input = (By.XPATH, "//input[@class='emailinput form-control']")
        self.select_project_role_id = "id_role"
        self.send_invite = (By.XPATH, "//button[contains(text(),'Send Invite')]")
        self.delete_confirm_button = (By.XPATH, "//button[@data-bind='click: $root.removeInvitation']")
        self.verify_user = (By.XPATH,
                            "//td[.//text()[contains(.,'" + UserData.web_user_mail + "')]]/following-sibling::td[.//text()[contains(.,'Delivered')]]")
        self.remove_user_invite = (By.XPATH,
                                   "//td[.//text()[contains(.,'" + UserData.web_user_mail + "')]]/following-sibling::td//i[@class='fa fa-trash']")

    def invite_new_web_user(self, role):
        self.wait_to_click(self.users_menu_id)
        self.wait_to_click(self.web_users_menu)
        # delete invitation if already sent
        self.delete_invite()
        self.wait_to_click(self.invite_web_user_button)
        self.wait_to_clear_and_send_keys(self.email_input, UserData.web_user_mail)
        select_role = Select(self.driver.find_element_by_id(self.select_project_role_id))
        select_role.select_by_value(role)
        self.wait_to_click(self.send_invite)


    def assert_invite(self):
        time.sleep(5)
        self.wait_to_click(self.users_menu_id)
        self.wait_to_click(self.web_users_menu)
        assert self.is_displayed(self.verify_user), "Unable to find invite."
        print("Web user invitation sent successfully")

    def delete_invite(self ):
        self.wait_to_click(self.remove_user_invite)
        self.wait_to_click(self.delete_confirm_button)
        print("Invitation deleted")
