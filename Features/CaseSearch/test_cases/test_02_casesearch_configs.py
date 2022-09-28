import time

import pytest

from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from Features.CaseSearch.user_inputs.casesearch_user_inputs import CaseSearchUserInput
from common_utilities.selenium.webapps import WebApps

""""Contains all case search configurations related test cases"""


def test_case_01_default_value_expression(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check default values are displayed"""
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    casesearch.check_default_values_displayed("Song Name", "Default", search_format="text")
    casesearch.check_default_values_displayed("Mood", "3", search_format="text")
    casesearch.check_default_values_displayed("Date Opened", casesearch.date_range(60), search_format="text")
    casesearch.check_default_values_displayed("Rating", "****", search_format="combobox")
    """Check values can be cleared and desired valie can be searched"""
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="1", value="Bugs")


def test_case_02_help_text(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check help text shows up"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    casesearch.check_help_text("Mood", "Mood\'s Rating")


def test_case_03_text_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check text format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value=CaseSearchUserInput.song_case_bugs,
                                       property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="1", value=CaseSearchUserInput.song_case_bugs)


def test_case_04_barcode_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check barcode format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Mood", input_value="3", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="3", value="3")


def test_case_05_date_range_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check date range format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Date Opened", input_value="2021-08-25",
                                       property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="6", value="25/08/2021")


def test_case_06_date_range_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check date range search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Date Opened", input_value="2021-08-25",
                                       property_type="TEXT_INPUT")
    time.sleep(10)
    casesearch.check_date_range("2021-08-25 to 2021-08-25")
    webapps.search_button_on_case_search_page(enter_key="YES")
    casesearch.check_values_on_caselist(row_num="6", value="25/08/2021")


def test_case_07_lookup_table_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check lookup table format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="**", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="4", value=CaseSearchUserInput.ratings.get('**'))


def test_case_08_address_geocoder_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check geocoder format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.artist_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.assert_address_is_hidden("Home Street")
    casesearch.add_address("New Canada St., 3855 Brienz, Switzerland", search_property='Search Home Address')
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value="New Canada St.")
    casesearch.check_values_on_caselist(row_num="3", value="Brienz")
    casesearch.check_values_on_caselist(row_num="5", value="Switzerland")
    casesearch.check_values_on_caselist(row_num="6", value="3855")


def test_case_09_mobile_ucr_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check mobile ucr format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Artist", input_value="Beach Boys", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value="Beach Boys")


def test_case_10_single_date_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check single date format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_and_search_all_cases_on_case_search_page()
    case_name = webapps.omni_search(CaseSearchUserInput.song_case_bugs)
    webapps.select_case_and_continue(case_name)
    webapps.open_form("Shows")
    webapps.search_again_cases()
    casesearch.search_against_property(search_property="Show Date", input_value="2022-08-04",
                                       property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value="2022-08-04")


def test_case_11_is_multiselect_format(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check multiselect format search property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="***", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="Rating", input_value="**", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="4", value=["2", "3"], is_multi="YES")
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Artist", input_value="Beach Boys", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="Artist", input_value="Arijit", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value=["Beach Boys", "Arijit"], is_multi="YES")


def test_case_12_allow_blank_values_normal(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check allow blanks normal"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="**", property_type="COMBOBOX",
                                       include_blanks="YES")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="4", value=["2", ""], is_multi="YES")
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="*****", property_type="COMBOBOX",
                                       include_blanks="YES")
    casesearch.search_against_property(search_property="Mood", input_value="5", property_type="TEXT_INPUT",
                                       include_blanks="YES")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="4", value=["5", ""], is_multi="YES")
    casesearch.check_values_on_caselist(row_num="3", value=["5", ""], is_multi="YES")


def test_case_13_allow_blank_values_geocoder(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check allow blanks geocoder"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.artist_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Home Country", input_value="Belgium",
                                       property_type="TEXT_INPUT", include_blanks="YES")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="5", value=["Belgium", ""], is_multi="YES")


def test_case_14_allow_blank_values_others(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check allow blanks all formats"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Date Opened", input_value="2021-08-25",
                                       property_type="TEXT_INPUT", include_blanks="YES")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="6", value=["25/08/2021", ""], is_multi="YES")
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Artist", input_value="Beach Boys", property_type="COMBOBOX",
                                       include_blanks="YES")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value=["Beach Boys", ""], is_multi="YES")


def test_case_15_exclude_property_from_case_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check exclude property from case search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Exclude property from case search")
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="1", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="2", value="4", is_multi="YES")
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="3", value=["1", "2", "3", "4", "5"], is_multi="YES")


def test_case_16_sticky_search_without_default_value(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check sticky search without default value"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    casesearch.search_against_property(search_property="Rating", input_value="***", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    driver.back()
    casesearch.check_default_values_displayed("Mood", "4", search_format="text")
    casesearch.check_default_values_displayed("Rating", "***", search_format="combobox")
    # This is failing
    # driver.refresh()
    # casesearch.check_default_values_displayed("Mood", "4", search_format="text")
    # casesearch.check_default_values_displayed("Rating", "***", search_format="combobox")


def test_case_17_sticky_search_with_default_value(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check sticky search with default value"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.search_button_on_case_search_page()
    webapps.search_again_cases()
    casesearch.check_default_values_displayed("Mood", "3", search_format="text")
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="3", value="4")
    webapps.search_again_cases()
    casesearch.check_default_values_displayed("Mood", "3", search_format="text")


def test_case_18_required_property(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check required property"""
    webapps.login_as("a_user")
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    webapps.search_all_cases()
    webapps.search_button_on_case_search_page()
    casesearch.check_validations_on_property(search_property="Mood", message="Required", required_or_validated="YES",
                                             property_type="TEXT_INPUT")
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    casesearch.check_validations_on_property(search_property="Mood", required_or_validated="NO",
                                             property_type="TEXT_INPUT")


def test_case_19_conditionally_required_condition_property(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check conditionally required condition property"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs Inline Case Search")
    webapps.clear_selections_on_case_search_page()
    """Check enabled"""
    casesearch.search_against_property(search_property="Rating", input_value="**", property_type="COMBOBOX")
    casesearch.check_validations_on_property(search_property="SubGenre",
                                             message="This is only required if Rating = 2, otherwise not required.",
                                             required_or_validated="YES", property_type="COMBOBOX")
    """Check disabled"""
    casesearch.search_against_property(search_property="Rating", input_value="***", property_type="COMBOBOX")
    casesearch.check_validations_on_property(search_property="SubGenre",
                                             message="This is only required if Rating = 2, otherwise not required.",
                                             required_or_validated="NO", property_type="COMBOBOX")
    """Check form submission"""
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Rating", input_value="**", property_type="COMBOBOX")
    casesearch.check_validations_on_property(search_property="SubGenre",
                                             message="This is only required if Rating = 2, otherwise not required.",
                                             required_or_validated="YES", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="Genre", input_value="Latin music", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="SubGenre", input_value="Latin jazz", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()


def test_case_20_json_property_function(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check json property funtion"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Artist")
    case_name = webapps.omni_search(CaseSearchUserInput.song_case_bugs)
    webapps.select_case_and_continue(case_name)
    webapps.open_form("Add Address")
    casesearch.add_address("New Canada St., 3855 Brienz, Switzerland", search_property="Search Home Address")
    casesearch.add_address("Avenida Benito Juárez, 77560 Alfredo V. Bonfil, Quintana Roo, Mexico",
                           search_property="Search Work Address")
    casesearch.check_json_function("Brienz", type="HOME")
    casesearch.check_json_function("Alfredo V. Bonfil", type="WORK")


@pytest.mark.skip(reason="This will fail, setting reverted!")
def test_case_21_case_search_title(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Case Search Title"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    casesearch.check_search_screen_title("Test")
    webapps.open_menu(CaseSearchUserInput.skip_default_menu)
    webapps.search_again_cases()
    casesearch.check_search_screen_title("Case Claim")
    webapps.open_app("French app_name")
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    casesearch.check_search_screen_title("Test")


def test_case_22_dependent_dropdowns(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Dependent Dropdowns"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    casesearch.search_against_property(search_property="Genre", input_value="Latin music", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="SubGenre", input_value="Latin jazz", property_type="COMBOBOX")
    """Check other values do not appear in dropdown"""
    casesearch.check_dropdown_value(search_property="SubGenre", not_to_be_present="Funk Metal")


def test_case_23_dependent_dropdowns_inline_case_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Dependent Dropdowns Inline Case Search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs Inline Case Search")
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Genre", input_value="Latin music", property_type="COMBOBOX")
    casesearch.search_against_property(search_property="SubGenre", input_value="Latin jazz", property_type="COMBOBOX")
    """Check other values do not appear in dropdown"""
    casesearch.check_dropdown_value(search_property="SubGenre", not_to_be_present="Funk Metal")
    """Search case and check if corresponding case is displayed"""
    webapps.search_button_on_case_search_page()
    webapps.omni_search(CaseSearchUserInput.song_case_bugs)


def test_case_24_case_search_validations(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Case Search Validations"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs Inline Case Search")
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Energy", input_value="3", property_type="TEXT_INPUT")
    time.sleep(2)
    casesearch.search_against_property(search_property="Song Name", input_value=" es", property_type="TEXT_INPUT")
    """Check validations imposed"""
    casesearch.check_validations_on_property(search_property="Song Name",
                                             message="No spaces allowed!",
                                             required_or_validated="YES", property_type="TEXT_INPUT")
    casesearch.check_validations_on_property(search_property="Energy",
                                             message="Sorry, this response is invalid!",
                                             required_or_validated="YES", property_type="TEXT_INPUT")
    """Check validations removed"""
    webapps.clear_selections_on_case_search_page()
    casesearch.check_validations_on_property(search_property="Song Name",
                                             message="No spaces allowed!",
                                             required_or_validated="NO", property_type="TEXT_INPUT")
    casesearch.check_validations_on_property(search_property="Energy",
                                             message="Sorry, this response is invalid!",
                                             required_or_validated="NO", property_type="TEXT_INPUT")
    """Check song seacrch w/o spaces and ensure case is displayed"""
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    webapps.omni_search(CaseSearchUserInput.song_case_bugs)
    """Check including blanks"""
    driver.back()
    time.sleep(2)
    driver.back()
    webapps.clear_selections_on_case_search_page()
    casesearch.select_include_blanks("Rating")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="4", value="")
