from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from HQSmokeTests.testPages.data.manage_forms_page import ManageFormsPage
from HQSmokeTests.testPages.data.import_cases_page import ImportCasesPage
from HQSmokeTests.testPages.data.reassign_cases_page import ReassignCasesPage
from HQSmokeTests.testPages.data.auto_case_update_page import AutoCaseUpdatePage
from HQSmokeTests.testPages.data.lookup_table_page import LookUpTablePage

""""Contains test cases related to the Data module"""


def test_case_29_import_cases(driver):

    export = ExportDataPage(driver)
    imp = ImportCasesPage(driver)
    export.data_tab()
    imp.replace_property_and_upload()


def test_case_30_reassign_cases(driver):

    export = ExportDataPage(driver)
    reassign = ReassignCasesPage(driver)
    export.data_tab()
    reassign.get_cases()
    reassign.reassign_case()


def test_case_31_manage_forms(driver):

    export = ExportDataPage(driver)
    manage = ManageFormsPage(driver)
    export.data_tab()
    manage.get_normal_forms()
    manage.view_normal_form()
    manage.archive_forms()
    manage.get_archived_forms()
    manage.view_archived_forms()
    manage.restore_forms()


def test_case_32_auto_case_update(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    data = AutoCaseUpdatePage(driver)
    data.open_auto_case_update_page()
    data.add_new_rule()
    data.remove_rule()


def test_case_33_create_lookup_table(driver):

    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.create_lookup_table()


def test_case_34_view_lookup_table(driver):

    data = LookUpTablePage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.view_lookup_table()
    data.delete_lookup_table()
