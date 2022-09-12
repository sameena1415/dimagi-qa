from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from common_utilities.selenium.webapps import WebApps

""""Contains all test cases that aren't specifically related any menu modules"""

case_search_app_name = "Music App (Case Search & Claim)"


def test_case_01_normal_workflow_search_all(driver):
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    """Checks if user can submit a form"""
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
    """Checks if user can submit a form"""
    webapps.open_app(case_search_app_name)
    webapps.open_menu("Songs (Normal)")
    webapps.search_all_cases()
    webapps.search_all_cases_on_case_search_page()
    webapps.search_again_cases()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()
    """Checks if claim successful"""
    webapps.open_app("Music App (Case Search & Claim)")
    webapps.open_menu("Songs (Normal)")
    casesearch.check_element_claimed(case_name)

