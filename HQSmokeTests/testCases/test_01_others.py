from HQSmokeTests.testPages.home.home_page import HomePage


def test_case_01_menu_visibility(driver):

    visible = HomePage(driver)
    visible.reports_menu()
    visible.dashboard_menu()
    visible.data_menu()
    visible.users_menu()
    visible.applications_menu()
    visible.messaging_menu()
    visible.web_apps_menu()


def test_case_53_rage_clicks(driver):

    visible = HomePage(driver)
    visible.rage_clicks()


