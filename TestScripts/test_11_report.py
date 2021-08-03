from Pages.homePage import HomePage
from Pages.reportPage import ReportPage
from TestBase.environmentSetupPage import EnvironmentSetup


class ExportTests(EnvironmentSetup):

    def test_01_report_loading(self):
        driver = self.driver
        report = HomePage(driver)
        report.reports_menu()
        load = ReportPage(driver)
        load.worker_activity_report()
        load.daily_form_activity_report()
        load.submissions_by_form_report()
        load.form_completion_report()
        load.case_activity_report()
        load.completion_vs_submission_report()
        load.worker_activity_times_report()
        load.project_performance_report()
        load.submit_history_report()
        load.case_list_report()
        load.sms_usage_report()
        load.messaging_history_report()
        load.message_log_report()
        load.sms_opt_out_report()
        load.scheduled_messaging_report()



