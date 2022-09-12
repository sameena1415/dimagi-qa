from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from common_utilities.selenium.webapps import WebApps

""""Contains all test cases that aren't specifically related any menu modules"""

case_search_app_name = "Music App (Case Search & Claim)"


def test_case_01_normal_workflow(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for normal search"""
    webapps.login_as('automation-user-1')
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Normal)")
    webapps.search_all_cases()
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()
    """Checks if claim successful"""
    webapps.open_app_home(case_search_app_name)
    webapps.open_menu("Songs (Normal)")
    casesearch.check_element_claimed(case_name)


def test_case_02_normal_workflow_search_again(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for normal search when re-searched"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Normal)")
    webapps.search_all_cases()
    webapps.search_all_cases_on_case_search_page()
    webapps.search_again_cases()
    webapps.search_all_cases()
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()
    """Checks if claim successful"""
    webapps.open_app("Music App (Case Search & Claim)")
    webapps.open_menu("Songs (Normal)")
    casesearch.check_element_claimed(case_name)


def test_case_03_search_first(driver):
    webapps = WebApps(driver)
    """Checks if user can submit a form for search first"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Search First)")
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()


def test_case_04_search_first_search_again(driver):
    webapps = WebApps(driver)
    """Checks if user can submit a form for search first when re-searched"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Search First)")
    webapps.search_all_cases_on_case_search_page()
    webapps.search_again_cases()
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()


def test_case_05_see_more(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for see more"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (See More)")
    webapps.search_all_cases()
    casesearch.check_default_rating_on_caselist("5")
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()


def test_case_06_see_more_search_again(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for see more when re-searched"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (See More)")
    webapps.search_all_cases()
    casesearch.check_default_rating_on_caselist("5")
    webapps.search_again_cases()
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()


def test_case_07_skip_to_default_search(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for skip to default search"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Skip to Default Search)")
    casesearch.check_default_rating_on_caselist("5")
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()


def test_case_08_skip_to_default_search_seach_again(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form for skip to default search when re-searched """
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Skip to Default Search)")
    webapps.search_again_cases()
    webapps.search_all_cases_on_case_search_page()
    casesearch.check_default_rating_on_caselist("5")
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()
