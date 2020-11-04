# Import the libraries and packages we will need and create a Unit Test Class that will have
# a setup, a teardown and our first test method (or test case).
import unittest
from CommcareHQ.Pages.exportDataPage import ExportDataPage
from CommcareHQ.TestBase.environmentSetupPage import EnvironmentSetup
import time


class ExportTests(EnvironmentSetup):

    def test_exports(self):
        driver = self.driver
        export = ExportDataPage(driver)
        try:
            export.data_tab()
            time.sleep(2)
            export.add_form_exports()
            time.sleep(2)
            export.form_exports()
            time.sleep(2)
            export.validate_downloaded_form_exports()
            time.sleep(2)
            ##export.del_form_exports() #to be called only if not running DSE
            time.sleep(2)
            export.add_case_exports()
            time.sleep(2)
            export.case_exports()
            time.sleep(2)
            export.validate_downloaded_case_exports()
            time.sleep(2)
            ##export.del_case_exports() #to be called only if not running DSE
            time.sleep(2)
            export.sms_exports()
            time.sleep(2)
            export.daily_saved_exports_form()
            time.sleep(2)
            export.deletion()
            time.sleep(2)
            export.daily_saved_exports_case()
            time.sleep(2)
            export.deletion()
            time.sleep(2)
            export.excel_dashboard_integration_form()
            time.sleep(2)
            export.deletion()
            time.sleep(2)
            export.excel_dashboard_integration_case()
            time.sleep(2)
            export.deletion()
            time.sleep(2)
            export.powerBI_tableau_integration_form()
            time.sleep(2)
            export.bi_tab_deletion()
            time.sleep(2)
            export.powerBI_tableau_integration_case()
            time.sleep(2)
            export.bi_tab_deletion()
            time.sleep(2)
            export.manage_forms()

        except Exception as e:
            print(e)
        finally:
            print("We are in!")
            time.sleep(2)


if __name__ == '__main__':
    unittest.main()
