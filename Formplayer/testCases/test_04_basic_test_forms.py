from Formplayer.testPages.app_preview.app_preview_basics import AppPreviewBasics
from Formplayer.testPages.app_preview.login_as_app_preview_page import LoginAsAppPreviewPage
from Formplayer.testPages.basic_test_app.basic_test_app_preview import BasicTestAppPreview
from Formplayer.testPages.basic_test_app.basic_test_web_apps import BasicTestWebApps
from Formplayer.testPages.webapps.login_as_page import LoginAsPage
from Formplayer.testPages.webapps.webapps_basics import WebAppsBasics
from Formplayer.userInputs.user_inputs import UserData

def test_case_16_incomplete_form_app_preview(driver):
    app_preview = LoginAsAppPreviewPage(driver)
    basic = BasicTestAppPreview(driver)
    login = LoginAsAppPreviewPage(driver)
    app_preview.open_view_app_preview(UserData.basic_tests_app['tests_app'])
    login.login_as_user(UserData.app_preview_mobile_worker)
    basic.delete_all_incomplete_forms()
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input1)
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input2)
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input3)
    basic.verify_number_of_forms(3)
    basic.delete_first_form()
    basic.verify_saved_form_and_submit_unchanged(basic.name_input2)
    basic.verify_submit_history(basic.name_input2, UserData.app_preview_mobile_worker)
    app_preview.open_view_app_preview(UserData.basic_tests_app['tests_app'])
    basic.verify_saved_form_and_submit_changed(basic.name_input1)
    basic.verify_submit_history(basic.changed_name_input, UserData.app_preview_mobile_worker)

def test_case_17_incomplete_form_web_apps(driver):
    login = LoginAsPage(driver)
    login.open_webapps_menu()
    login.login_as_user(UserData.app_preview_mobile_worker)
    basic = BasicTestWebApps(driver)
    basic.delete_all_incomplete_forms()
    login.open_basic_tests_app(UserData.basic_tests_app['tests_app'])
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input1)
    login.open_basic_tests_app(UserData.basic_tests_app['tests_app'])
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input2)
    login.open_basic_tests_app(UserData.basic_tests_app['tests_app'])
    basic.open_form(UserData.basic_tests_app['case_list'], UserData.basic_tests_app['form_name'])
    basic.save_incomplete_form(basic.name_input3)
    basic.verify_number_of_forms(3)
    basic.delete_first_form()
    basic.verify_saved_form_and_submit_unchanged(basic.name_input2)
    basic.verify_submit_history(basic.name_input2, UserData.app_preview_mobile_worker)
    login.open_webapps_menu()
    basic.verify_saved_form_and_submit_changed(basic.name_input1)
    basic.verify_submit_history(basic.changed_name_input, UserData.app_preview_mobile_worker)



