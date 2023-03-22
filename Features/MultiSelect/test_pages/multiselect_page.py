import time

from selenium.webdriver.common.by import By

from common_utilities.selenium.base_page import BasePage

""""Contains test page elements and functions related to the Case Search functionality"""


class MultiSelectWorkflows(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.row_checkbox_xpath = "(//*[@class='select-row-checkbox'])[{}]"
        self.value_in_table_format = "(//td[@class='module-case-list-column-checkbox']//following::td[@class='module-case-list-column'][1])[{}]"
        self.select_all_checkbox = (By.ID, "select-all-checkbox")
        self.case_names = (By.XPATH, "//td[contains(@class,'case-list-column')][3]")
        self.multi_select_continue = (By.ID, "multi-select-continue-btn")
        self.selected_case_names_on_forms = (By.XPATH, "//span[@class='caption webapp-markdown-output']")
        self.select_case_button = (By.ID, "select-case")
        self.checkbox = "(//td[@class='module-case-list-column' and text() = '{}'][1]//preceding::input[1])[1]"

    def select_cases(self, case_count):
        song_names = []
        for i in range(1, case_count):
            row_checkbox = self.get_element(self.row_checkbox_xpath, str(i))
            self.js_click(row_checkbox)
            case_name_in_table = self.get_element(self.value_in_table_format, str(i))
            selected_song_names = self.get_text(case_name_in_table)
            song_names.append(selected_song_names)
        return song_names

    def continue_to_forms_multiselect(self):
        self.js_click(self.multi_select_continue)

    def check_selected_cases_present_on_form(self, items_selected_on_case_list):
        time.sleep(5)
        song_names_on_form = self.find_elements_texts(self.selected_case_names_on_forms)
        stripped = list(filter(None, [s.partition(" by")[0] for s in song_names_on_form]))
        stripped_final = list(filter(None, [s.replace("song: ", "") for s in stripped]))
        assert items_selected_on_case_list == stripped_final, f"No, list1 {items_selected_on_case_list} doesn't match list2{stripped_final}"

    def select_case_on_case_detail(self):
        self.js_click(self.select_case_button)

    def check_if_checkbox_is_selected(self, case_name):
        checkbox = self.get_element(self.checkbox, case_name)
        assert self.is_selected(checkbox)

    def check_if_checkbox_are_selected(self, case_names):
        for case in case_names:
            checkbox = self.get_element(self.checkbox, case)
            assert self.is_selected(checkbox)


