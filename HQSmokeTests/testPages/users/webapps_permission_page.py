from HQSmokeTests.testPages.base.base_page import BasePage

from selenium.webdriver.common.by import By


class WebAppPermissionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.web_app_permissions_menu = (By.LINK_TEXT, "Web Apps Permissions")
        self.first_radio_button = (By.XPATH, "//input[@name='ko_unique_1']")
        self.second_radio_button = (By.XPATH, "//input[@name='ko_unique_2']")
        self.save_button = (By.XPATH, "//div[@class='btn btn-primary']")
        self.after_save = (By.XPATH, "//div[@class='btn btn-primary disabled']")

    def webapp_permission_option_toggle(self):
        self.click(self.web_app_permissions_menu)
        self.driver.implicitly_wait(2)
        if self.is_selected(self.first_radio_button):
            self.click(self.second_radio_button)
        else:
            self.click(self.first_radio_button)
        self.click(self.save_button)
        assert self.is_visible_and_displayed(self.after_save)
        print("Webapps permissions toggled")
