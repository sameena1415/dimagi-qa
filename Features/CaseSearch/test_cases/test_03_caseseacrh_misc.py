import time

import pytest

from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from Features.CaseSearch.user_inputs.casesearch_user_inputs import CaseSearchUserInput
from common_utilities.selenium.base_page import BasePage
from common_utilities.selenium.webapps import WebApps

""""Contains all case search miscellaneous test cases"""


def test_case_01_eof_navigations(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check eof navs"""
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    webapps.select_case_and_continue("Bugs")
    """EOF Nav - Prev Menu"""
    webapps.open_form("Play Song")
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav="PREV_MENU", menu=CaseSearchUserInput.search_first_menu)
    """EOF Nav - Menu-Songs"""
    webapps.open_form("Add Show")
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav="MENU", menu=CaseSearchUserInput.search_first_menu)
    """EOF Nav - First Menu"""
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    search_first_form_names = webapps.select_case_and_continue("Bugs")
    webapps.open_form("Update Rating, Mood, or Energy")
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav="FIRST_MENU", menu=CaseSearchUserInput.case_search_app_name)
    """EOF Nav - Home Screen"""
    # This fails on prod currently so commenting..
    # webapps.open_form("Close Song --> redirects to Home Screen")
    # webapps.submit_the_form()
    # casesearch.check_eof_navigation(eof_nav="HOME_SCREEN")


def test_case_02_related_property_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check related property search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    webapps.select_case_and_continue("Bugs")
    webapps.open_form("Shows")
    webapps.omni_search("Justin")
    casesearch.check_values_on_caselist(row_num="4", value="Justin")
    case_name = webapps.omni_search("Bangalore")
    webapps.select_case(case_name)
    casesearch.check_value_on_case_detail(search_property="Parent Artist", expected_value="Justin")


def test_case_03_auto_advance_menus(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check auto advance to forms"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.artist_menu)
    case_name = webapps.omni_search("Bugs Artist")
    webapps.select_case_and_continue(case_name)
    casesearch.check_eof_navigation(eof_nav="MENU", menu="Bugs Artist")


def test_case_04_display_only_forms(driver):
    webapps = WebApps(driver)
    base = BasePage(driver)
    """Check display only form modes"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Play Song - Display Only Forms")
    assert not base.is_displayed(webapps.search_all_cases_button)


def test_case_05_shadow_menu(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check forms in normal menu"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    search_first_form_names = webapps.select_case_and_continue("Bugs")
    """Check search and forms in shadow menu"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Shadow Menu")
    casesearch.search_against_property(search_property="Rating", input_value="*****", property_type="COMBOBOX")
    webapps.search_button_on_case_search_page()
    case_name = webapps.omni_search("Kyon")
    shadow_form_names = webapps.select_case_and_continue(case_name)
    assert shadow_form_names == search_first_form_names


def test_case_06_performance_check(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check performance"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Musical Instruments (Performance)")
    webapps.open_form("View Instruments")
    webapps.search_all_cases()
    casesearch.search_against_property(search_property="Instrument Name", input_value="Guitar",
                                       property_type="TEXT_INPUT")
    start_time = time.perf_counter()  # Start capturing time
    webapps.search_button_on_case_search_page()
    end_time = time.perf_counter()  # Stop capturing time
    run_time = end_time - start_time
    assert run_time <= 10
    webapps.search_again_cases()
    casesearch.search_against_property(search_property="Instrument Name", input_value="Guitar",
                                       property_type="TEXT_INPUT")
    start_time = time.perf_counter()
    webapps.search_button_on_case_search_page()
    end_time = time.perf_counter()
    run_time = end_time - start_time
    assert run_time <= 10


@pytest.mark.skip(reason="This is failing app setup error but bocked due Dominic's bug")
def test_case_07_multi_case_types(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    """Check multi case type case list"""
    webapps.open_menu("Mixed Case Types")
    webapps.search_button_on_case_search_page()
    # Checks case type song
    webapps.omni_search("Bugs")
    # Checks case type show
    webapps.omni_search("Jubin")
    webapps.select_case_and_continue("Jubin")
    casesearch.check_eof_navigation(eof_nav="MENU", menu="Mixed Case Types")
    webapps.submit_the_form()  # This is failing app setup error but bocked due Dominic's bug
    """Check multi case type case list for DR workflow"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Mixed Case Types")
    webapps.search_button_on_case_search_page()
    webapps.omni_search("SAMTHIRD")  # Checks case type show: This may fail due to current app settings, DR not enabled
    webapps.select_case_and_continue("SAMTHIRD")
    casesearch.check_eof_navigation(eof_nav="MENU", menu="Mixed Case Types")
    webapps.submit_the_form()


def test_case_08_display_condition(driver):
    webapps = WebApps(driver)
    base = BasePage(driver)
    """Check Display condition for a_user"""
    webapps.login_as("a_user")
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    assert base.is_displayed(webapps.search_all_cases_button)
    """Check Display condition for another user"""
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    assert not base.is_displayed(webapps.search_all_cases_button)


@pytest.mark.skip(reason="This is failing app setup error but bocked due Dominic's bug")
def test_case_09_search_filter(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Search Filter"""
    webapps.login_as("a_user")
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    webapps.search_all_cases()
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="3", value="5")


def test_case_10_claim_condition(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Claim Condition"""
    webapps.login_as("a_user")
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    webapps.search_all_cases()
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    case_name = webapps.omni_search("Kala Chashma")
    form_name = webapps.select_case_and_continue(case_name)
    assert not bool(form_name)


def test_case_11_do_not_search_cases(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    base = BasePage(driver)
    """Check don't search cases owned by the following ids"""
    webapps.login_as("a_user")
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Case Search Settings")
    webapps.search_all_cases()
    casesearch.search_against_property(search_property="Mood", input_value="4", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    webapps.omni_search("b_users song")
    assert base.is_displayed(webapps.list_is_empty)
