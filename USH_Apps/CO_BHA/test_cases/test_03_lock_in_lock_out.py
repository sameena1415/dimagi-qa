from Features.CaseSearch.constants import *
from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from USH_Apps.CO_BHA.test_pages.bha_app_pages import BhaWorkflows
from USH_Apps.CO_BHA.user_inputs.bha_user_inputs import BhaUserInput
from common_utilities.selenium.webapps import WebApps
import test_01_admit_client


def test_case_lock_in_1_1(driver):
    """use case: no existing lock status for clinic user"""
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    app = BhaWorkflows(driver)

    webapps.login_as(BhaUserInput.clinic_level_user)
    webapps.open_app(BhaUserInput.bha_app_name)
    webapps.open_menu(BhaUserInput.search_my_clients)
    first_name = casesearch.search_against_property(search_property=BhaUserInput.first_name,
                                                    input_value=test_01_admit_client.first_name,
                                                    property_type=TEXT_INPUT)
    last_name = casesearch.search_against_property(search_property=BhaUserInput.last_name,
                                                   input_value=test_01_admit_client.first_name,
                                                   property_type=TEXT_INPUT)
    dob = casesearch.search_against_property(search_property=BhaUserInput.dob,
                                             input_value=BhaUserInput.date_1950_05_01,
                                             property_type=TEXT_INPUT)
    webapps.search_button_on_case_search_page()
    webapps.omni_search(first_name)
    webapps.open_form(BhaUserInput.update_lock_status_request)
    app.select_radio(BhaUserInput.lock_in)
    app.select_clinic(BhaUserInput.aurora_therapy_center)
    app.select_radio(BhaUserInput.yes)
    app.check_question_label(label=BhaUserInput.bha_approval_needed, displayed=YES)
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav=MENU, menu=BhaUserInput.admit_client_form)


def test_case_lock_in_1_2(driver):
    """use case: no existing lock status for state user"""
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    app = BhaWorkflows(driver)

    webapps.login_as(BhaUserInput.state_level_user)
    webapps.open_app(BhaUserInput.bha_app_name)
    webapps.open_menu(BhaUserInput.pending_requests)
    webapps.select_case(test_01_admit_client.first_name + " " + test_01_admit_client.last_name)
    app.select_radio(BhaUserInput.approve)
    app.check_question_label(label=BhaUserInput.lock_out_confirmation, displayed=YES)
    webapps.submit_the_form()
    casesearch.check_eof_navigation(eof_nav=MENU, menu=BhaUserInput.pending_requests)

