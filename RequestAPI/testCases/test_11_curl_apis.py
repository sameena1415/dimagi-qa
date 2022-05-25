import pytest

from RequestAPI.testMethods.curl_methods import CurlMethods
from RequestAPI.testMethods.forms_methods import FormsMethods
from RequestAPI.userInputs.user_inputs import UserData


def test_case_35_submission_api(settings):
    uri = settings["url"]+UserData.domain
    mw = CurlMethods(settings)
    mw.submission_api(uri, "Test_XML.xml",settings['login_user'], settings['login_pass'])

def test_case_36_restore_ota(settings):
    uri = settings["url"]+UserData.domain
    mw = CurlMethods(settings)
    mw.get_restore_ota(uri, settings['login_user'], settings['login_pass'])

def test_case_37_lookup_table_upload(settings):
    uri = settings["url"]
    mw = CurlMethods(settings)
    mw.post_lookup_table_upload(uri,"case search.xlsx", settings['login_user'], settings['login_pass'])

def test_case_38_import_cases_from_excel(settings):
    uri = settings["url"]
    mw = CurlMethods(settings)
    mw.post_import_cases_from_excel(uri, "Test File.xlsx", settings['login_user'], settings['login_pass'])

@pytest.mark.xfail
def test_case_39_form_data_export(settings):
    uri = settings["url"]
    mw = FormsMethods(settings)
    mw.post_form_data_export(uri, "POST_form_data_export.json", settings['login_user'], settings['login_pass'])