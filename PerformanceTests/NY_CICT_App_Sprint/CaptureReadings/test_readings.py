import os
import time
import pytest

from PerformanceTests.NY_CICT_App_Sprint.WorkflowActions.workflows.excel_actions import write_to_excel
from PerformanceTests.NY_CICT_App_Sprint.WorkflowActions.base.decorators import first_dump_filename
from PerformanceTests.NY_CICT_App_Sprint.WorkflowActions.workflows.hq_actions import HomePage
from PerformanceTests.NY_CICT_App_Sprint.UserInputs.user_inputs import UserData

"""Runs all workflows and captures the readings for the app versions before and after releases for two preconfigured users"""


@pytest.mark.parametrize("user", [UserData.ci_ct_user1, UserData.ci_ct_user2])
@pytest.mark.parametrize("application", [UserData.application_before_release, UserData.application_after_release])
@pytest.mark.repeat(UserData.repeat_count)
def test_app_workflows(driver, user, application, settings):
    """Repeat Count"""

    test_app_workflows.counter += 1

    """General workflows"""

    visible = HomePage(driver)
    visible.login_as_ci_ct_user(user, settings["url"])
    time.sleep(5)
    visible.break_locks_and_clear_user_data()
    time.sleep(5)
    visible.sync_application(username=user, application_name=application)
    time.sleep(10)
    visible.open_application(username=user, application_name=application)

    """CI workflows"""

    visible.all_cases_menu_load(username=user, application_name=application)
    visible.search_case_in_test(username=user, application_name=application)
    visible.open_case_detail(username=user, application_name=application)
    visible.case_menu_display(username=user, application_name=application)
    visible.open_case_investigation_form(username=user, application_name=application)
    visible.ci_form_answer_question(username=user, application_name=application)
    visible.ci_form_submission(username=user, application_name=application)

    """CM workflows"""

    visible.app_home_screen(application)
    visible.all_contacts_menu_load(username=user, application_name=application)
    visible.search_contact_in_test(username=user, application_name=application)
    visible.open_contact_detail(username=user, application_name=application)
    visible.contact_menu_display(username=user, application_name=application)
    visible.open_contact_monitoring_form(username=user, application_name=application)
    visible.cm_form_answer_question(username=user, application_name=application)
    visible.cm_form_submission(username=user, application_name=application)

    """Back to webapps workflows"""

    visible.back_to_webapps_home()

    """Write to excel"""

    write_to_excel(username=user, application_name=application)
    if os.path.isfile(first_dump_filename) and test_app_workflows.counter == UserData.repeat_count:
        os.remove(first_dump_filename)
        test_app_workflows.counter = 0


test_app_workflows.counter = 0
