from HQSmokeTests.testPages.data.data_page import DataPage
from HQSmokeTests.testPages.data.export_data_page import ExportDataPage
from HQSmokeTests.testPages.data.manage_forms_page import ManageFormsPage
from HQSmokeTests.testPages.data.import_cases_page import ImportCasesPage
from HQSmokeTests.testPages.data.reassign_cases_page import ReassignCasesPage


def test_TC_29_import_cases(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    imp = ImportCasesPage(driver)
    imp.replace_property_and_upload()


def test_TC_30_reassign_cases(driver):
    export = ExportDataPage(driver)
    export.data_tab()
    reassign = ReassignCasesPage(driver)
    reassign.get_cases()
    reassign.reassign_case()


def test_TC_31_manage_forms(driver):

    export = ExportDataPage(driver)
    export.data_tab()
    manage = ManageFormsPage(driver)
    manage.get_normal_forms()
    manage.view_normal_form()
    manage.achieve_forms()
    manage.get_archieved_forms()
    manage.view_archieved_forms()
    manage.restore_forms()


def test_TC_32_auto_case_update(driver):

    data = DataPage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.open_auto_case_update_page()
    data.add_new_rule()
    data.remove_rule()


def test_TC_33_create_lookup_table(driver):

    data = DataPage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.create_lookup_table()


def test_TC_34_view_lookup_table(driver):

    data = DataPage(driver)
    export = ExportDataPage(driver)
    export.data_tab()
    data.view_lookup_table()


def test_cleanup_lookuptable(driver):

    data = DataPage(driver)
    data.delete_lookup_table()

