import pytest

from RequestAPI.testMethods.web_user_methods import WebUserMethods
from RequestAPI.userInputs.user_inputs import UserData

""""Contains all test cases that aren't specifically related any menu modules"""


@pytest.mark.xfail
def test_case_5_web_user_creation(settings):
    uri = settings["url"] + UserData.domain + UserData.post_domain_url
    mw = WebUserMethods(settings)
    mobile_user_id = mw.web_user_creation(uri, "POST_web_user.json", settings['login_user'], settings['login_pass'])
    settings["web_user_id"] = mobile_user_id


@pytest.mark.xfail
def test_case_6_web_user_edit(settings):
    uri = settings["url"] + UserData.domain + UserData.post_domain_url
    mw = WebUserMethods(settings)
    mw.web_user_edit(uri, settings["web_user_id"], "POST_web_user.json", settings['login_user'],
                     settings['login_pass'])


def test_case_7_web_user_get(settings):
    uri = settings["url"] + UserData.domain + UserData.post_domain_url
    mw = WebUserMethods(settings)
    mw.web_user_get(uri, settings['login_user'],
                    settings['login_pass'])
