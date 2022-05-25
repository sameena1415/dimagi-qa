from RequestAPI.testMethods.reports_methods import ReportsMethods
from RequestAPI.userInputs.user_inputs import UserData


def test_case_18_list_of_reports(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = ReportsMethods(settings)
    mw.get_report_list(uri, settings['login_user'], settings['login_pass'])


def test_case_19_application_structure(settings):
    uri = settings["url"]+UserData.domain+UserData.post_domain_url
    mw = ReportsMethods(settings)
    mw.download_report(uri, settings['login_user'], settings['login_pass'])
