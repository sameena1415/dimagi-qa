import time

import pytest

from HQSmokeTests.testPages.applications.app_preview import AppPreviewPage
from HQSmokeTests.testPages.applications.application_page import ApplicationPage
from HQSmokeTests.testPages.email.email_verification import EmailVerification
from HQSmokeTests.testPages.users.mobile_workers_page import MobileWorkerPage
from HQSmokeTests.testPages.users.roles_permissions_page import RolesPermissionPage
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.reports.report_page import ReportPage
from HQSmokeTests.testPages.users.web_user_page import WebUsersPage
from HQSmokeTests.userInputs.user_inputs import UserData
from common_utilities.generate_random_string import fetch_random_string
from common_utilities.hq_login.login_page import LoginPage

results = dict()

@pytest.mark.report
@pytest.mark.reportCaseList
@pytest.mark.p1p2EscapeDefect
def test_case_70_case_owner_list(driver, settings):
    report = HomePage(driver, settings)
    report.reports_menu()
    load = ReportPage(driver)
    load.check_for_case_list_owner(settings['url'])


@pytest.mark.report
@pytest.mark.reportCaseList
@pytest.mark.p1p2EscapeDefect
def test_case_71_case_owner_list_explorer(driver, settings):
    report = HomePage(driver, settings)
    report.reports_menu()
    load = ReportPage(driver)
    load.check_for_case_list_explorer_owner(settings['url'])

@pytest.mark.user
@pytest.mark.groups
@pytest.mark.rolesPermission
@pytest.mark.p1p2EscapeDefect
@pytest.mark.bulkUpload
@pytest.mark.bulkDelete
def test_case_73_non_admin_role_permission(driver, settings):
    menu = HomePage(driver, settings)
    menu.users_menu()
    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    print("Opened Roles and Permissions Page")
    role = RolesPermissionPage(driver)
    rolename = role.add_non_admin_role()
    webuser = WebUsersPage(driver)
    menu.users_menu()
    webuser.edit_user_permission(rolename)
    login = LoginPage(driver, settings["url"])
    login.logout()
    login.login(UserData.p1p2_user, settings["login_password"])
    load = ReportPage(driver)
    load.verify_only_permitted_report(UserData.report_for_p1p2)
    mobile = MobileWorkerPage(driver)
    mobile.bulk_upload_mobile_worker()
    mobile.delete_bulk_users()
    login.logout()
    login.login(settings["login_username"], settings["login_password"])
    menu.users_menu()
    webuser.edit_user_permission("Admin")
    results['role'] = rolename
    return results['role']

@pytest.mark.user
@pytest.mark.mobileWorker
@pytest.mark.groups
@pytest.mark.userImport
@pytest.mark.userExport
@pytest.mark.p1p2EscapeDefect
def test_case_74_delete_role_column(driver, settings):
    username = "username_p1p2_"+fetch_random_string()
    user = MobileWorkerPage(driver)
    home = HomePage(driver, settings)
    home.users_menu()
    user.delete_bulk_users()
    user.mobile_worker_menu()
    user.create_mobile_worker()
    user.mobile_worker_enter_username(username)
    user.mobile_worker_enter_password(fetch_random_string())
    user.click_create(username)
    user.mobile_worker_menu()
    user.select_mobile_worker_created(username)
    user.update_role_for_mobile_worker(results['role'])
    newest_file = user.download_mobile_worker()
    user.remove_role_in_downloaded_file(newest_file, results['role'])
    home.users_menu()
    user.upload_mobile_worker()
    time.sleep(5)
    user.mobile_worker_menu()
    user.select_mobile_worker_created(username)
    user.verify_role_for_mobile_worker(results['role'])
    home.users_menu()
    user.delete_bulk_users()
    home.users_menu()
    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    role.delete_test_roles()

@pytest.mark.report
@pytest.mark.p1p2EscapeDefect
def test_case_75_daily_form_activity(driver, settings):
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    report.daily_form_activity_report()
    web_data = report.export_daily_form_activity_to_excel()
    email = EmailVerification(settings)
    link = email.get_hyperlink_from_latest_email(UserData.daily_form_activity)
    report.compare_web_with_email(link, web_data)

@pytest.mark.report
@pytest.mark.p1p2EscapeDefect
def test_case_76_application_status(driver, settings):
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    web_data = report.export_app_status_to_excel()
    email = EmailVerification(settings)
    link = email.get_hyperlink_from_latest_email(UserData.app_status)
    report.compare_app_status_web_with_email(link, web_data)


@pytest.mark.application
@pytest.mark.appBuilder
@pytest.mark.p1p2EscapeDefect
def test_case_77_create_new_app(driver, settings):
    load = ApplicationPage(driver)
    app_name = load.create_application_with_verifications()
    app = AppPreviewPage(driver)
    lat, lon = app.submit_form_with_loc()
    home = HomePage(driver, settings)
    home.reports_menu()
    report = ReportPage(driver)
    report.verify_form_in_submit_history(app_name, lat, lon)
    load.delete_p1p2_application(app_name)
