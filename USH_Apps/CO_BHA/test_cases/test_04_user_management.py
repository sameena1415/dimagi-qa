from USH_Apps.CO_BHA.test_pages.bha_app_pages import BhaWorkflows
from USH_Apps.CO_BHA.user_inputs.bha_user_inputs import BhaUserInput
from common_utilities.selenium.webapps import WebApps


def test_case_access_to_module_state(driver):
    """use case: A state level user access the list of users and can enter the form to view their credential."""
    webapps = WebApps(driver)
    app = BhaWorkflows(driver)

    webapps.login_as(BhaUserInput.state_level_user)
    webapps.open_app(BhaUserInput.bha_app_name)
    """Add Clinic"""
    webapps.open_menu(BhaUserInput.user_management)
    app.check_headers_on_case_list([BhaUserInput.name, BhaUserInput.username, BhaUserInput.creation_date])
    case = webapps.omni_search(BhaUserInput.central_registry_2)
    webapps.select_case(case)
    app.select_clinic(BhaUserInput.aurora_therapy_center)
    webapps.submit_the_form()
    """Remove Clinic"""
    webapps.open_menu(BhaUserInput.user_management)
    case = webapps.omni_search(BhaUserInput.central_registry_2)
    webapps.select_case(case)
    app.remove_clinic(BhaUserInput.aurora_therapy_center)
    webapps.submit_the_form()
