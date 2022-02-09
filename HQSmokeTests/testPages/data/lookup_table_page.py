from HQSmokeTests.testPages.base.base_page import BasePage
from HQSmokeTests.userInputs.generate_random_string import fetch_random_string

from selenium.webdriver.common.by import By


class LookUpTablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.table_id_name = "lookuptable_" + str(fetch_random_string())
        self.table_fields = "//label[@class=\"control-label col-sm-2\"]//following::input[@type='text' and @class = 'form-control']"
        self.table_created = "(//span[text()='" + self.table_id_name + "'])[1]"

        self.manage_tables_link = (By.LINK_TEXT, "Manage Tables")
        self.add_table = (By.XPATH, "//button[@data-bind='click: $root.addDataType']")
        self.table_fields_path = (By.XPATH, self.table_fields)
        self.table_id = (By.XPATH, self.table_fields + "[last()-3]")
        self.table_id_description = (By.XPATH, self.table_fields + "[last()-2]")
        self.add_field = (By.XPATH, "(//button[@data-bind='click: addField'])[last()]")
        self.field_name = (By.XPATH, "(//input[@data-bind=\"value: tag, valueUpdate: 'afterkeydown', hasfocus: true\"])[last()]")
        self.save_table = (By.XPATH, "(//button[@data-bind='click: saveEdit'])[last()]")
        self.table_created_path = (By.XPATH, self.table_created)
        self.view_tables_link = (By.LINK_TEXT, "View Tables")
        self.select_table_drop_down = (By.ID, "select2-report_filter_table_id-container")
        self.select_table_from_dropdown = (By.XPATH, "//li[contains(.,'" + self.table_id_name + "')]")
        self.view_table = (By.ID, "apply-btn")
        self.column_name = (By.XPATH, "(//div[contains(i/following-sibling::text(), '" + self.table_id_name + "')])[1]")
        self.delete_table = (By.XPATH, self.table_created + "//following::button[@data-bind='click: $root.removeDataType'][1]")

    def create_lookup_table(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.add_table)
        self.send_keys(self.table_id, self.table_id_name)
        self.send_keys(self.table_id_description, self.table_id_name)
        self.wait_to_click(self.add_field)
        self.send_keys(self.field_name, self.table_id_name)
        self.wait_to_click(self.save_table)
        assert self.is_present_and_displayed(self.table_created_path)
        print("LookUp Table created successfully!")

    def view_lookup_table(self):
        self.wait_to_click(self.view_tables_link)
        self.wait_to_click(self.select_table_drop_down)
        self.wait_to_click(self.select_table_from_dropdown)
        self.wait_to_click(self.view_table)
        assert self.is_present_and_displayed(self.column_name)
        print("LookUp Table can be viewed successfully!")

    def delete_lookup_table(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.delete_table)
        obj = self.driver.switch_to.alert
        obj.accept()
        print("LookUp Table deleted successfully!")
