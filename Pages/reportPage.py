import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ReportPage:

    def __init__(self, driver):
        self.driver = driver

        # Mobile Worker Reports
        self.worker_activity_rep = "Worker Activity"
        self.daily_form_activity_rep = "Daily Form Activity"
        self.submissions_by_form_rep = "Submissions By Form"
        self.form_completion_rep = "Form Completion Time"
        self.case_activity_rep = "Case Activity"
        self.completion_vs_submission_rep = "Form Completion vs. Submission Trends"
        self.worker_activity_times_rep = "Worker Activity Times"
        self.project_performance_rep = "Project Performance"

        # Inspect Data Reports
        self.submit_history_rep = "Submit History"
        self.case_list_rep = "Case List"

        # Manage Deployments Reports
        self.application_status_rep = "Application Status"
        self.agg_user_status_rep = "Aggregate User Status"
        self.raw_forms_rep = "Raw Forms, Errors & Duplicates"
        self.device_log_rep = "Device Log Details"
        self.app_error_rep = "Application Error Report"

        # Messaging Reports
        self.sms_usage_rep = "SMS Usage"
        self.messaging_history_rep = "Messaging History"
        self.message_log_rep = "Message Log"
        self.sms_opt_out_rep = "SMS Opt Out Report"
        self.scheduled_messaging_rep = "Scheduled Messaging Events"

        # Report Elements
        self.apply_id = "apply-filters"
        self.report_content_id = "report-content"

    def wait_to_click(self, *locator, timeout=10):
        try:
            clickable = ec.element_to_be_clickable(locator)
            WebDriverWait(self.driver, timeout).until(clickable).click()
        except NoSuchElementException:
            print(NoSuchElementException)

    def check_if_report_loaded(self):
        try:
            self.wait_to_click(By.ID, self.apply_id)
        except (TimeoutException,NoSuchElementException):
            print("Button Disabled")
        assert True == WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((
            By.ID, self.report_content_id))).is_displayed()
        print("Report loaded successfully!")

    def worker_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.worker_activity_rep)
        self.check_if_report_loaded()

    def daily_form_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.daily_form_activity_rep)
        self.check_if_report_loaded()

    def submissions_by_form_report(self):
        self.wait_to_click(By.LINK_TEXT, self.submissions_by_form_rep)
        self.check_if_report_loaded()

    def form_completion_report(self):
        self.wait_to_click(By.LINK_TEXT, self.form_completion_rep)
        self.check_if_report_loaded()

    def case_activity_report(self):
        self.wait_to_click(By.LINK_TEXT, self.case_activity_rep)
        self.check_if_report_loaded()

    def completion_vs_submission_report(self):
        self.wait_to_click(By.LINK_TEXT, self.completion_vs_submission_rep)
        self.check_if_report_loaded()

    def worker_activity_times_report(self):
        self.wait_to_click(By.LINK_TEXT, self.worker_activity_times_rep)
        self.check_if_report_loaded()

    def project_performance_report(self):
        self.wait_to_click(By.LINK_TEXT, self.project_performance_rep)
        self.check_if_report_loaded()

    def submit_history_report(self):
        self.wait_to_click(By.LINK_TEXT, self.submit_history_rep)
        self.check_if_report_loaded()

    def case_list_report(self):
        self.wait_to_click(By.LINK_TEXT, self.case_list_rep)
        self.check_if_report_loaded()

    def sms_usage_report(self):
        self.wait_to_click(By.LINK_TEXT, self.sms_usage_rep)
        self.check_if_report_loaded()

    def messaging_history_report(self):
        self.wait_to_click(By.LINK_TEXT, self.messaging_history_rep)
        self.check_if_report_loaded()

    def message_log_report(self):
        self.wait_to_click(By.LINK_TEXT, self.message_log_rep)
        self.check_if_report_loaded()

    def sms_opt_out_report(self):
        self.wait_to_click(By.LINK_TEXT, self.sms_opt_out_rep)
        self.check_if_report_loaded()

    def scheduled_messaging_report(self):
        self.wait_to_click(By.LINK_TEXT, self.scheduled_messaging_rep)
        self.check_if_report_loaded()
