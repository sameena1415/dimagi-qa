import random
import time

import pytest

from HQSmokeTests.testPages.users.group_page import GroupPage
from HQSmokeTests.userInputs.user_inputs import UserData
from common_utilities.generate_random_string import fetch_random_string
from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.users.mobile_workers_page import MobileWorkerPage


""""Contains test cases related to the User's Mobile Worker module"""

group_id = dict()
group_id["user_new"] = None


@pytest.mark.user
@pytest.mark.mobileWorker
@pytest.mark.user_profiles
@pytest.mark.user_fields
@pytest.mark.user_organization
@pytest.mark.p1p2EscapeDefect
def test_case_54_add_custom_user_data_profile_to_mobile_worker(driver, settings, rerun_count):
    create = MobileWorkerPage(driver)
    menu = HomePage(driver, settings)
    field = f"field_{rerun_count}{fetch_random_string()}"
    username = f"username_{fetch_random_string()}{rerun_count}_new"
    profile_name_text = f"test_profile_{fetch_random_string()}{rerun_count}"

    menu.users_menu()
    create.mobile_worker_menu()
    create.create_new_mobile_worker(username)
    create.create_new_user_fields(field)
    create.click_profile()
    create.add_profile(profile_name_text, field)
    create.save_field()
    create.select_user_and_update_fields(username, field)
    create.add_phone_number()
    create.select_profile(profile_name_text)
    create.update_information()
    create.select_location()
    
    menu.users_menu()
    newest_file = create.download_mobile_worker()
    create.edit_profile_in_downloaded_file(newest_file, username)
    menu.users_menu()
    create.upload_mobile_worker()
    menu.users_menu()
    create.select_mobile_worker_created(username)
    create.verify_profile_change(UserData.p1p2_profile)
    create.mobile_worker_menu()
    create.delete_bulk_users()
    menu.users_menu()
    create.mobile_worker_menu()
    create.edit_user_field()
    create.click_profile()
    create.remove_profile(profile_name_text, field)
    create.save_field()
    create.click_fields()
    create.remove_user_field()
    create.save_field()


@pytest.mark.user
@pytest.mark.groups
@pytest.mark.user_profiles
@pytest.mark.user_fields
@pytest.mark.mobileWorker
def test_aftertest_cleanup_items_in_users_menu(driver, settings):
    clean = MobileWorkerPage(driver)
    clean2 = GroupPage(driver)

    menu = HomePage(driver, settings)
    menu.users_menu()
    clean.delete_bulk_users()

    menu.users_menu()
    clean.mobile_worker_menu()
    clean.edit_user_field()
    clean.click_profile()
    clean.delete_profile()
    print("Removed all test profiles")

    menu.users_menu()
    clean.mobile_worker_menu()
    clean.edit_user_field()
    clean.delete_test_user_field()
    print("Deleted the user field")

    clean.mobile_worker_menu()
    clean2.click_group_menu()
    clean2.delete_test_groups()
    print("Deleted the group")
