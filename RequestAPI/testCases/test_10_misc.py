import pytest

from RequestAPI.testMethods.miscellaneous_methods import MiscellaneousMethods
from RequestAPI.testMethods.mobile_worker_methods import MobileWorkerMethods
from RequestAPI.userInputs.user_inputs import UserData

""""Contains all test cases that aren't specifically related any menu modules"""


@pytest.mark.xfail
def test_case_31_sso_api(settings):
    uri = settings["url"] + UserData.domain + UserData.post_domain_url
    mw = MiscellaneousMethods(settings)
    mw.sso_api_post(uri, "POST_sso_api.json", settings['login_user'], settings['login_pass'])


def test_case_32_list_data_forwarding_api(settings):
    uri = settings["url"] + UserData.domain + UserData.post_domain_url
    mw = MiscellaneousMethods(settings)
    mw.get_list_data_forwarding_api(uri, settings['login_user'], settings['login_pass'])


def test_case_33_user_identity_api(settings):
    uri = settings["url"] + UserData.post_domain_url
    mw = MiscellaneousMethods(settings)
    mw.get_user_identity_api(uri, settings['login_user'], settings['login_pass'])


def test_case_34_user_domain_list_api(settings):
    uri = settings["url"] + UserData.post_domain_url
    mw = MiscellaneousMethods(settings)
    mw.get_user_domain_list_api(uri, settings['login_user'], settings['login_pass'])
