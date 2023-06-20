from Features.CaseSearch.constants import *
from USH_Apps.CO_BHA.constants import *
from Features.CaseSearch.test_pages.casesearch_page import CaseSearchWorkflows
from USH_Apps.CO_BHA.test_pages.bha_app_pages import BhaWorkflows
from USH_Apps.CO_BHA.user_inputs.bha_user_inputs import BhaUserInput
from common_utilities.selenium.base_page import BasePage
from common_utilities.selenium.webapps import WebApps
import names

global first_name, last_name


def test_case_admit_case_1(driver):
    """use case: Admit the client - case doesn't exist"""
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    app = BhaWorkflows(driver)
    base = BasePage(driver)

    webapps.login_as(BhaUserInput.clinic_level_user)
    webapps.open_app(BhaUserInput.bha_app_name)
    webapps.open_menu(BhaUserInput.search_and_admit_client)
    app.check_search_properties_present([BhaUserInput.client_id, BhaUserInput.ssn, BhaUserInput.medicaid_id])
    global first_name, last_name
    first_name = casesearch.search_against_property(search_property=BhaUserInput.first_name,
                                                    input_value=Automation + names.get_first_name(),
                                                    property_type=TEXT_INPUT)
    last_name = casesearch.search_against_property(search_property=BhaUserInput.last_name,
                                                   input_value=Automation + names.get_last_name(),
                                                   property_type=TEXT_INPUT)
    dob = casesearch.search_against_property(search_property=BhaUserInput.dob,
                                             input_value=BhaUserInput.date_1950_05_01,
                                             property_type=TEXT_INPUT)
    casesearch.search_against_property(search_property=BhaUserInput.reason_for_no_ssn,
                                       input_value=BhaUserInput.does_not_have_ssn,
                                       property_type=COMBOBOX)
    casesearch.select_checkbox(BhaUserInput.consent, [1])
    webapps.search_button_on_case_search_page()
    assert base.is_displayed(webapps.list_is_empty)
    app.expected_count_on_continue_button("0")
    app.click_on_admit_new_client()
    casesearch.check_eof_navigation(eof_nav=MENU, menu=BhaUserInput.admit_client_form)
    app.select_radio(BhaUserInput.yes)
    app.check_client_info_on_form(search_property=BhaUserInput.first_name_on_form,
                                  search_value=first_name)
    app.check_client_info_on_form(search_property=BhaUserInput.last_name_on_form,
                                  search_value=last_name)
    app.check_client_info_on_form(search_property=BhaUserInput.dob_on_form,
                                  search_value=dob)
    app.select_clinic(BhaUserInput.aurora_therapy_center)
    webapps.submit_the_form()


def test_case_admit_case_2(driver):
    """use case: Admit a client - case does exist -> Request pending admission"""
    webapps = WebApps(driver)
    casesearch = CaseSearchWorkflows(driver)
    app = BhaWorkflows(driver)

    webapps.login_as(BhaUserInput.clinic_level_user)
    webapps.open_app(BhaUserInput.bha_app_name)
    webapps.open_menu(BhaUserInput.search_and_admit_client)
    casesearch.search_against_property(search_property=BhaUserInput.first_name,
                                       input_value=app.replace_one_char(first_name),
                                       property_type=TEXT_INPUT)
    typo_first_name = casesearch.search_against_property(search_property=BhaUserInput.last_name,
                                                         input_value=app.replace_one_char(last_name),
                                                         property_type=TEXT_INPUT)
    typo_last_name = casesearch.search_against_property(search_property=BhaUserInput.dob,
                                                        input_value=BhaUserInput.date_1950_05_01,
                                                        property_type=TEXT_INPUT)
    casesearch.search_against_property(search_property=BhaUserInput.reason_for_no_ssn,
                                       input_value=BhaUserInput.does_not_have_ssn,
                                       property_type=COMBOBOX)
    casesearch.select_checkbox(BhaUserInput.consent, [1])
    webapps.search_button_on_case_search_page()
    # CHECK QUESTION TEXT
    app.select_radio(BhaUserInput.yes)
    # CHECK TABLE CONTENT
    app.check_answer_options(label=BhaUserInput.admit_client_form, displayed=NO)
    """Admission question is hidden upon selecting cancel"""
    app.select_radio(BhaUserInput.cancel)
    app.check_question_label(label=BhaUserInput.where_admit, displayed=NO)
    """Selection of center"""
    app.select_radio(BhaUserInput.request_admission_review)
    app.select_clinic(BhaUserInput.aurora_therapy_center)
    webapps.submit_the_form()
    """Check if case present in pending requests menu"""
    webapps.open_menu(BhaUserInput.pending_requests)
    webapps.omni_search(typo_first_name + " " + typo_last_name)
    casesearch.check_values_on_caselist(row_num=BhaUserInput.one,
                                        expected_value=BhaUserInput.pending)
    casesearch.check_values_on_caselist(row_num=BhaUserInput.two,
                                        expected_value=typo_first_name + " " + typo_last_name)
    """Check message history"""
    # Navigate to Messaging History in Reports
    

# def test_case_admit_case_7(driver):
#     """use case: match on inactive client"""
#     webapps = WebApps(driver)
#     casesearch = CaseSearchWorkflows(driver)
#     app = BhaWorkflows(driver)
#
#     webapps.login_as(BhaUserInput.clinic_level_user)
#     webapps.open_app(BhaUserInput.bha_app_name)
#     webapps.open_menu(BhaUserInput.search_my_clients)
#     casesearch.search_against_property(search_property=BhaUserInput.first_name,
#                                        input_value=BhaUserInput.inactive_first_name,
#                                        property_type=TEXT_INPUT)
#     casesearch.search_against_property(search_property=BhaUserInput.last_name,
#                                        input_value=BhaUserInput.inactive_last_name,
#                                        property_type=TEXT_INPUT)
#     casesearch.search_against_property(search_property=BhaUserInput.dob,
#                                        input_value=BhaUserInput.inactive_dob,
#                                        property_type=TEXT_INPUT)
#     casesearch.search_against_property(search_property=BhaUserInput.reason_for_no_ssn,
#                                        input_value=BhaUserInput.does_not_have_ssn,
#                                        property_type=COMBOBOX)
#     casesearch.select_checkbox(BhaUserInput.consent, [1])
#     webapps.search_button_on_case_search_page()
#     webapps.submit_the_form()
#     # Navigate to Case List in Reports
