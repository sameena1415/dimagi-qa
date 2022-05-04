import os
import time
import pytest
import pandas as pd
from openpyxl import load_workbook

from PerformanceTests.CICT_App_Sprints.NYperformance.WorkflowActions.base.decorators import first_dump_filename
from PerformanceTests.CICT_App_Sprints.NYperformance.WorkflowActions.workflows.dataframe_actions import write_readings_for
from PerformanceTests.CICT_App_Sprints.NYperformance.WorkflowActions.workflows.hq_actions import HomePage
from NYperformance.UserInputs.user_inputs import UserData

""""Runs all workflows and captures the readings for the app version AFTER release"""


@pytest.mark.repeat(UserData.no_of_repeat)
def test_app_workflows(driver):

    """General workflows"""
    visible = HomePage(driver)
    visible.break_locks_and_clear_user_data()
    time.sleep(5)
    visible.login_as_ci_ct_user()
    time.sleep(5)
    visible.sync_application()
    time.sleep(5)
    visible.open_application(UserData.application_after_release)

    """"CI workflows"""

    visible.all_cases_menu_load()
    visible.search_case_in_test()
    visible.open_case_detail()
    visible.case_menu_display()
    visible.open_case_investigation_form()
    visible.ci_form_answer_question()
    visible.ci_form_submission()

    """"CM workflows"""

    visible.app_home_screen(UserData.application_before_release)
    visible.all_contacts_menu_load()
    visible.search_contact_in_test()
    visible.open_contact_detail()
    visible.contact_menu_display()
    visible.open_contact_monitoring_form()
    visible.cm_form_answer_question()
    visible.cm_form_submission()

    """"Back to webapps workflows"""

    visible.back_to_webapps_home()


def test_write_readings_to_excel():

    """Create dataframe and write to excel"""

    workflows = ["sync_application",
                 "open_application",
                 "all_cases_menu_load",
                 "open_case_detail",
                 "case_menu_display",
                 "open_case_investigation_form",
                 "ci_form_answer_question",
                 "ci_form_submission",
                 "all_contacts_menu_load",
                 "open_contact_detail",
                 "contact_menu_display",
                 "open_contact_monitoring_form",
                 "cm_form_answer_question",
                 "cm_form_submission"]
    columns = ['workflow',
               'round_one (in secs)',
               'round_two (in secs)',
               'round_three (in secs)',
               'load_time_avg (in secs)']

    df2 = pd.DataFrame(columns=columns)
    for workflow in workflows:
        temporary_df = pd.DataFrame([write_readings_for(workflow)], columns=columns)
        # df2 = df2.append(temporary_df, ignore_index=True)
        df2 = pd.concat([df2, temporary_df])
        file = os.path.abspath(os.path.join(UserData.ROOT, 'NY_final_reading.xlsx'))
        book = load_workbook(file)
        with pd.ExcelWriter(file, engine='openpyxl') as writer:
            writer.book = book
            writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
            df2.to_excel(writer, sheet_name="after_release", index=False)
    os.remove(first_dump_filename)
