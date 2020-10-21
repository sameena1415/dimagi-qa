# Import the libraries and packages we will need and create a Unit Test Class that will have
# a setup, a teardown and our first test method (or test case).
import unittest
from pageobjects.export_data import Export_Data
from pageobjects.login import Login
from webdriver import Driver
from values import inputs
import time


class TestCCHQ(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(inputs.base_url)
        login_page = Login(self.driver)
        time.sleep(5)
        login_page.accept_cookies()
        login_page.enter_username(inputs.login_username)
        login_page.enter_password(inputs.login_password)
        login_page.click_submit()


    def test_exports(self):
        driver = self.driver
        export = Export_Data(driver)
        try:
            export.data_tab()
            time.sleep(2)
            export.del_form_exports()
            time.sleep(2)
            #export.add_form_exports()
            time.sleep(2)
            #export.form_exports()
            time.sleep(2)
            #export.validate_downloaded_form_exports()
            time.sleep(2)
            #export.add_case_exports()
            time.sleep(2)
            #export.case_exports()
            time.sleep(2)
            #export.validate_downloaded_case_exports()
            time.sleep(2)
            #export.sms_exports()
            time.sleep(2)
            #export.daily_saved_exports()
            time.sleep(2)
            #export.excel_dashboard_integration_form()
            time.sleep(2)
            #export.excel_dashboard_integration_case()
            time.sleep(2)
            #export.powerBI_tableau_integration_form()
            time.sleep(2)
            #export.powerBI_tableau_integration_case()
            time.sleep(2)
            #export.manage_forms()

        #except Exception as e:
        #    print(e)
        finally:
            print("We are in!")
            time.sleep(2)


    # def tearDown(self):
    # self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
