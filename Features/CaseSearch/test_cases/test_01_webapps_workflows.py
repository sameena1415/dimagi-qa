from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from common_utilities.selenium.webapps import WebApps

""""Contains all test cases that aren't specifically related any menu modules"""


def test_case_01_normal_workflow(driver):
    webapps = WebApps(driver)
    webapps.open_app("Music App (Case Search & Claim)")
    webapps.open_menu("Songs (Normal)")
    webapps.search_all_cases()
    webapps.search_all_cases_on_case_search_page()
    case_name = webapps.omni_search("Bugs")
    webapps.select_case(case_name)
    webapps.open_form("Play Song")
    webapps.submit_the_form()

