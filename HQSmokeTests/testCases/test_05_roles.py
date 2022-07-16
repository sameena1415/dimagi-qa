import pytest

from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.roles_permissions_page import RolesPermissionPage
from HQSmokeTests.testPages.users.webapps_permission_page import WebAppPermissionPage

""""Contains test cases related to the User's Roles and Permissions module"""


def test_case_06_add_role(driver):

    menu = HomePage(driver)
    menu.users_menu()
    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    print("Opened Roles and Permissions Page")
    role = RolesPermissionPage(driver)
    role.add_role()
    print("New Role Added")

def test_case_06_edit_role(driver):

    menu = HomePage(driver)
    menu.users_menu()
    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    role = RolesPermissionPage(driver)
    role.edit_role()
    print("Role Edited Successfully")


def test_case_12_toggle_option_webapp_permission(driver):

    menu = HomePage(driver)
    menu.users_menu()
    role = RolesPermissionPage(driver)
    role.roles_menu_click()
    web = WebAppPermissionPage(driver)
    web.webapp_permission_option_toggle()


def test_cleanup_items_in_role_menu(driver):

    menu = HomePage(driver)
    menu.users_menu()
    clean3 = RolesPermissionPage(driver)
    clean3.roles_menu_click()
    clean3.delete_test_roles()
    print("Deleted the role")