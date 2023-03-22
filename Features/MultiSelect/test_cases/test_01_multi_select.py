import pytest

from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from Features.CaseSearch.user_inputs.casesearch_user_inputs import CaseSearchUserInput
from Features.MultiSelect.test_pages.multiselect_page import MultiSelectWorkflows
from Features.MultiSelect.user_inputs.multiselect_user_inputs import MultiSelectUserInput
from common_utilities.generate_random_string import fetch_random_string
from common_utilities.selenium.webapps import WebApps
from Features.CaseSearch.constants import *

""""Contains all multi-select related test cases"""


def test_case_01_multiple_selected_cases_accessible_on_form(driver):
    multiselect = MultiSelectWorkflows(driver)
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(MultiSelectUserInput.multiselect_app_name)
    webapps.open_menu(MultiSelectUserInput.Songs_MS_SF_IS)
    webapps.search_button_on_case_search_page()
    cases_selected = multiselect.select_cases(case_count=3)
    multiselect.continue_to_forms_multiselect()
    webapps.open_form(MultiSelectUserInput.update_song_back_to_menu_form)
    multiselect.check_selected_cases_present_on_form(cases_selected)
    webapps.answer_repeated_questions(question_label=CaseSearchUserInput.add_show_question,
                                      input_type=textarea,
                                      input_value=fetch_random_string())
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav=MENU,
                                    menu=MultiSelectUserInput.Songs_MS_SF_IS)


@pytest.skip(reason="Failing, Kiran to check and raise a support ticket")
def test_case_02_multiselect_with_omnisearch(driver):
    multiselect = MultiSelectWorkflows(driver)
    webapps = WebApps(driver)
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(MultiSelectUserInput.multiselect_app_name)
    webapps.open_menu(MultiSelectUserInput.Songs_MS_N_NIS)
    case_name = webapps.omni_search(CaseSearchUserInput.song_automation_song_1)
    webapps.select_case(case_name)
    multiselect.select_case_on_case_detail()
    webapps.omni_search(CaseSearchUserInput.song_automation_song_1)
    multiselect.check_if_checkbox_is_selected(case_name)


def test_case_03_multiselect_with_pagination(driver):
    multiselect = MultiSelectWorkflows(driver)
    webapps = WebApps(driver)
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(MultiSelectUserInput.multiselect_app_name)
    webapps.open_menu(MultiSelectUserInput.Songs_MS_N_NIS)
    webapps.search_all_cases()
    webapps.clear_and_search_all_cases_on_case_search_page()
    cases_selected = multiselect.select_cases(case_count=3)
    webapps.change_page_number("25")
    multiselect.check_if_checkbox_are_selected(cases_selected)
    webapps.switch_bw_pages()
    multiselect.check_if_checkbox_are_selected(cases_selected)
    webapps.go_to_page("2")
    multiselect.check_if_checkbox_are_selected(cases_selected)
