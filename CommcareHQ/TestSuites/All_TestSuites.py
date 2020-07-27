from unittest import TestLoader, TestSuite
import HtmlTestRunner
from SeleniumCCHQ.CommcareHQ.TestScripts.menuVisibility import MenuVisibilityTests
from SeleniumCCHQ.CommcareHQ.TestScripts.mobileWorkers import MobileWorkerTests
from SeleniumCCHQ.CommcareHQ.TestScripts.groups import GroupsTests
from SeleniumCCHQ.CommcareHQ.TestScripts.rolesPermissions import RolesPermissionPage

if __name__ == "__main__":
    loader = TestLoader()
    SmokeTestSuite = TestSuite((
        loader.loadTestsFromTestCase(MenuVisibilityTests),
        loader.loadTestsFromTestCase(MobileWorkerTests),
        loader.loadTestsFromTestCase(GroupsTests),
        loader.loadTestsFromTestCase(RolesPermissionPage)
    ))

    testRunner = HtmlTestRunner.HTMLTestRunner(output='Reports', report_name="Test_Result_Report",
                                               report_title='CCHQ Smoke Tests', verbosity=2, combine_reports=True)
    testRunner.run(SmokeTestSuite)
