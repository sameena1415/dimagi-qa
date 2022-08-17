import os
import pandas as pd
from openpyxl import load_workbook

from AppSprintPerformanceTests.CICT.WorkflowActions.workflows.dataframe_actions import write_readings_for
from AppSprintPerformanceTests.CICT.UserInputs.ny_cict_user_inputs import UserData
from common_utilities.path_settings import PathSettings

"""Create dataframe and write to excel"""


def write_to_excel(username,  application_name):
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

    df = pd.DataFrame(columns=columns)
    for workflow in workflows:
        temporary_df = pd.DataFrame([write_readings_for(workflow, application_name, username)], columns=columns)
        df = pd.concat([df, temporary_df])
        file = os.path.abspath(os.path.join(PathSettings.NY_ROOT, 'NY_final_reading.xlsx'))
        file_exists = os.path.isfile(file)
        if UserData.application_before_release in application_name:
            prefix = 'before'
        else:
            prefix = 'after'
        if not file_exists:
            df.to_excel(file, sheet_name=prefix + "-" + username, index=False)
        else:
            book = load_workbook(file)
            with pd.ExcelWriter(file, engine='openpyxl') as writer:
                writer.book = book
                writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
                df.to_excel(writer, sheet_name=prefix + "-" + username, index=False)