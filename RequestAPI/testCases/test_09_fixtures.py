from RequestAPI.testMethods.fixtures_methods import FixturesMethods
from RequestAPI.userInputs.user_inputs import UserData


def test_case_28_list_of_fixture_type_api_all_lookup_table(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = FixturesMethods(settings)
    mw.get_list_of_fixture_type_api_all_lookup_table(uri, settings['login_user'], settings['login_pass'])

def test_case_29_specific_fixture_type_api_single_fixture_item(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = FixturesMethods(settings)
    mw.get_specific_fixture_type_api_single_fixture_item(uri,  settings['login_user'], settings['login_pass'])

def test_case_30_specific_fixture_type_api_specific_fixture_table(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = FixturesMethods(settings)
    mw.get_specific_fixture_type_api_specific_fixture_table(uri, settings['login_user'], settings['login_pass'])

