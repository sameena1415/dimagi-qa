from Pages.applicationPage import ApplicationPage
from TestBase.environmentSetupPage import EnvironmentSetup


class ApplicationTests(EnvironmentSetup):

    def test_01_create_new_app(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.create_new_application()

    def test_02_form_builder_explore(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.form_builder_exploration()

    def test_05_delete_app(self):
        driver = self.driver
        load = ApplicationPage(driver)
        load.delete_application()
