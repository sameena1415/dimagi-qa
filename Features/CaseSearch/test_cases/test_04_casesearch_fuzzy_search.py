import time

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
    casesearch.search_against_property(search_property="Song Name", input_value="Bugs", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="1", value="Bugs User2")
    "Select case to cliam"
    webapps.select_case_and_continue("Bugs User2")
    "Check case claimed on user caselist"
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.omni_search("Bugs User2")


def test_case_02_loose_access_to_case_search(driver):
    webapps = WebApps(driver)
    base = BasePage(driver)
    """Check access loss to Case Search and Claim functionality"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs - Without Case Search Settings")
    assert not base.is_displayed(webapps.search_all_cases_button)


def test_case_03_non_fuzzy_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    base = BasePage(driver)
    """Check non fuzzy search"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Musical Instruments (Performance)")
    webapps.open_form("View Instruments")
    webapps.search_all_cases()
    casesearch.search_against_property(search_property="Instrument Name", input_value="Guit",
                                       property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    assert base.is_visible_and_displayed(webapps.list_is_empty)
    driver.back()
    casesearch.search_against_property(search_property="Instrument Name", input_value="Acoustic bass guitar",
                                       property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    webapps.omni_search("Acoustic bass guitar")


def test_case_04_default_search_properties(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Default Search Properties"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu("Songs (Skip to Default Search)")
    casesearch.check_values_on_caselist(row_num="4", value="5")


def test_case_05_remove_special_characters(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Check Remove Special Characters"""
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.normal_menu)
    webapps.search_all_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property="Song ID", input_value="1-2-3-4-5", property_type="TEXT_INPUT")
    webapps.search_button_on_case_search_page()
    casesearch.check_values_on_caselist(row_num="7", value="12345")


# Elastic search takes time to reflect the case so executing this last
def test_case_06_claimed_cases_on_report(driver):
    report = HomePage(driver)
    load = ReportPage(driver)
    user = MobileWorkerPage(driver)
    casesearch = CaseSearchWorkflows(driver)
    report.reports_menu()
    load.case_list_report()
    time.sleep(200)  # explore case list explorer
    casesearch.check_case_claim_case_type("Bugs User2", user.username + "@casesearch.commcarehq.org")
    """Delete the user"""
    user.mobile_worker_menu()
    user.select_and_delete_mobile_worker(user.username)
