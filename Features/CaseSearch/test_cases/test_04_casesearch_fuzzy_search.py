import time

from Features.CaseSearch.constants import *
from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from Features.CaseSearch.user_inputs.casesearch_user_inputs import CaseSearchUserInput
from HQSmokeTests.testPages.reports.report_page import ReportPage
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.mobile_workers_page import MobileWorkerPage
from common_utilities.selenium.base_page import BasePage
from common_utilities.selenium.webapps import WebApps

""""Contains all fuzzy search related test cases"""


def test_case_01_fuzzy_search_and_case_claim(driver):
    menu = HomePage(driver)
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    user = MobileWorkerPage(driver)
    """Create new user"""
    user.mobile_worker_menu()
    user.create_mobile_worker()
    username = user.mobile_worker_enter_username(user.username)
    user.mobile_worker_enter_password(username)
    user.click_create()
    """Check fuzzy search"""
    menu.web_apps_menu()
    webapps.login_as(username)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    "Fuzzy search"
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                       input_value=CaseSearchUserInput.song_case_bugs,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    casename = casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.one,
                                                   expected_value=CaseSearchUserInput.song_case_bugs_user2)
    "Select case to cliam"
    webapps.select_case_and_continue(casename)
    "Check case claimed on user caselist"
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.omni_search(casename)


def test_case_02_loose_access_to_case_search(driver):
    webapps = WebApps(driver)
    base = BasePage(driver)
    """Check access loss to Case Search and Claim functionality"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.without_search_setting_menu)
    assert not base.is_displayed(webapps.search_all_cases_button)


def test_case_03_non_fuzzy_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    base = BasePage(driver)
    """Check non fuzzy search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.musical_instruments_menu)
    webapps.open_form(CaseSearchUserInput.view_instruments_form)
    webapps.search_all_cases()
    casesearch.search_against_property(search_property=CaseSearchUserInput.instrument_name,
                                       input_value=CaseSearchUserInput.incomplete_word_guitar,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    assert base.is_visible_and_displayed(webapps.list_is_empty)
    driver.back()
    casesearch.search_against_property(search_property=CaseSearchUserInput.instrument_name,
                                       input_value=CaseSearchUserInput.acoustic_bass_guitar,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search("Acoustic bass guitar")


def test_case_04_default_search_properties(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Default Search Properties"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.skip_default_menu)
    casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.four,
                                        expected_value=CaseSearchUserInput.five)


def test_case_05_remove_special_characters(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Remove Special Characters"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_id,
                                       input_value=CaseSearchUserInput.id_with_hyphen,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.seven,
                                        expected_value=CaseSearchUserInput.id_without_hyphen)


# Elastic search takes time to reflect the case so executing this last
def test_case_06_claimed_cases_on_report(driver):
    report = HomePage(driver)
    load = ReportPage(driver)
    user = MobileWorkerPage(driver)
    casesearch = CaseSearchWorkflows(driver)
    report.reports_menu()
    load.case_list_report()
    time.sleep(200)  # explore case list explorer
    casesearch.check_case_claim_case_type(claimed_case_name=CaseSearchUserInput.song_case_bugs_user2,
                                          claimed_user=user.username + "@casesearch.commcarehq.org")
    """Delete the user"""
    user.mobile_worker_menu()
    user.select_and_delete_mobile_worker(user.username)
