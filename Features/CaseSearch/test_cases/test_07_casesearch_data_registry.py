from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from Features.CaseSearch.user_inputs.casesearch_user_inputs import CaseSearchUserInput
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from common_utilities.selenium.webapps import WebApps
from Features.CaseSearch.constants import *

""""Contains all data registry related test cases"""


def test_case_01_no_access_dr_caselist(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.login_as(CaseSearchUserInput.user_1)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    case_name = casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                                   input_value=CaseSearchUserInput.song_case_on_casesearch2,
                                                   property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(case_name, displayed=NO)
    webapps.open_menu(CaseSearchUserInput.load_external_search_first_menu)
    webapps.clear_selections_on_case_search_page()
    case_name = casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                                   input_value=CaseSearchUserInput.song_case_on_casesearch2,
                                                   property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(case_name, displayed=NO)
    webapps.open_menu(CaseSearchUserInput.smart_link_skip_default_menu)
    webapps.clear_selections_on_case_search_page()
    case_name = casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                                   input_value=CaseSearchUserInput.song_case_on_casesearch2,
                                                   property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(case_name, displayed=NO)


def test_case_02_access_to_non_dr_caselist(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.search_first_menu)
    webapps.clear_selections_on_case_search_page()
    case_name = casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                                   input_value=CaseSearchUserInput.song_case_bugs_on_casesearch_1,
                                                   property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(case_name, displayed=NO)


def test_case_03_load_external_case_into_caselist_skip_default(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.load_external_skip_default_menu)
    casename = webapps.omni_search(CaseSearchUserInput.song_case_cs2_song_11, displayed=NO)
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                       input_value=casename,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(casename)
    webapps.select_case_and_continue(casename)
    domain_url = driver.current_url
    assert "casesearch" in domain_url
    webapps.submit_the_form()


def test_case_04_load_external_case_into_caselist_search_first(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.load_external_search_first_menu)
    casename = webapps.omni_search(CaseSearchUserInput.song_case_cs2_song_13, displayed=NO)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                       input_value=casename,
                                       property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(casename)
    webapps.select_case_and_continue(casename)
    domain_url = driver.current_url
    assert "casesearch" in domain_url
    webapps.submit_the_form()


def test_case_05_reports_load_external(driver, settings):
    report = HomePage(driver, settings)
    load = ReportPage(driver)
    report.reports_menu()
    load.submit_history_report()
    domain_url = driver.current_url
    assert "casesearch" in domain_url
    load.verify_form_data_submit_history(CaseSearchUserInput.song_case_cs2_song_11, CaseSearchUserInput.user_1)
    load.verify_form_data_submit_history(CaseSearchUserInput.song_case_cs2_song_13, CaseSearchUserInput.user_1)


def test_case_06_smart_link_skip_default(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    driver.get(CaseSearchUserInput.casesearch)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.smart_link_skip_default_menu)
    casename = webapps.omni_search(CaseSearchUserInput.song_case_cs2_song_14, displayed=NO)
    webapps.search_again_cases()
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                        input_value=casename,
                                        property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(casename)
    webapps.select_case_and_continue(casename)
    webapps.select_user(CaseSearchUserInput.kiran)
    domain_url = driver.current_url
    assert "casesearch-1" in domain_url
    webapps.submit_the_form()


def test_case_07_smart_link_search_first(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    driver.get(CaseSearchUserInput.casesearch)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.smart_link_search_first_menu)
    casename = webapps.omni_search(CaseSearchUserInput.song_case_cs2_song_12, displayed=NO)
    webapps.clear_selections_on_case_search_page()
    casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                        input_value=casename,
                                        property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(casename)
    webapps.select_case_and_continue(casename)
    webapps.select_user(CaseSearchUserInput.kiran)
    domain_url = driver.current_url
    assert "casesearch-1" in domain_url
    webapps.submit_the_form()


def test_case_08_reports_smart_link(driver, settings):
    report = HomePage(driver, settings)
    load = ReportPage(driver)
    driver.get(CaseSearchUserInput.casesearch_1)
    report.reports_menu()
    load.submit_history_report()
    domain_url = driver.current_url
    assert "casesearch" in domain_url
    load.verify_form_data_submit_history(CaseSearchUserInput.song_case_cs2_song_14, CaseSearchUserInput.kiran)
    load.verify_form_data_submit_history(CaseSearchUserInput.song_case_cs2_song_12, CaseSearchUserInput.kiran)


def test_case_09_unrelated_case_property(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    driver.get(CaseSearchUserInput.casesearch)
    webapps.open_app(CaseSearchUserInput.case_search_app_name)
    webapps.open_menu(CaseSearchUserInput.unrelated_case_load_external_menu)
    webapps.clear_selections_on_case_search_page()
    casename = casesearch.search_against_property(search_property=CaseSearchUserInput.song_name,
                                                  input_value=CaseSearchUserInput.song_8th_dec,
                                                  property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(casename)
    casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.two,
                                        expected_value=CaseSearchUserInput.case_with_unrelated_id.get("case_id"))
    casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.three,
                                        expected_value=CaseSearchUserInput.case_with_unrelated_id.get("song_name"))
    casesearch.check_values_on_caselist(row_num=CaseSearchUserInput.four,
                                        expected_value=CaseSearchUserInput.case_with_unrelated_id.get("rating"))
    webapps.select_case_and_continue(casename)
    webapps.submit_the_form()
