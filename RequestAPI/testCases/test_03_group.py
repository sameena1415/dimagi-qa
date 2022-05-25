import pytest

from RequestAPI.testMethods.groups_methods import GroupsMethods
from RequestAPI.userInputs.user_inputs import UserData

""""Contains all test cases that aren't specifically related any menu modules"""


def test_case_8_bulk_api_create_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    # mw.bulk_api_create_group(uri, "POST_group.json", settings['login_user'], settings['login_pass'])
    mobile_user_id = mw.bulk_api_create_group(uri, "POST_web_user.json", settings['login_user'], settings['login_pass'])
    settings["group_id"]= mobile_user_id


def test_case_9_list_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    mw.get_group_list(uri, settings['login_user'], settings['login_pass'])

@pytest.mark.xfail
def test_case_10_bulk_api_create_multiple_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    mw.bulk_api_create_multiple_group(uri, "PATCH_group.json", settings['login_user'],
                                               settings['login_pass'])

def test_case_11_individual_api_get_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    mw.get_individual_api_group(uri, settings["group_id"], settings['login_user'], settings['login_pass'])

def test_case_12_individual_api_edit_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    mw.individual_api_edit_group(uri, settings["group_id"], "POST_web_user.json", settings['login_user'], settings['login_pass'])

def test_case_13_individual_api_delete_group(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = GroupsMethods(settings)
    mw.delete_individual_api_group(uri, settings["group_id"], settings['login_user'], settings['login_pass'])

