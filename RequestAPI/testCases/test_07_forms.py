from RequestAPI.testMethods.forms_methods import FormsMethods
from RequestAPI.userInputs.user_inputs import UserData


def test_case_22_list_of_all_forms(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = FormsMethods(settings)
    mw.get_all_forms_list(uri, settings['login_user'], settings['login_pass'])


def test_case_23_form_data_list(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = FormsMethods(settings)
    mw.get_form_data(uri ,settings['login_user'], settings['login_pass'])
