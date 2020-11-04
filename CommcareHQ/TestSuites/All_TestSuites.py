from unittest import TestSuite
from unittest.loader import TestLoader

import HtmlTestRunner

from CommcareHQ.TestScripts.cleanup import CleanUps
from CommcareHQ.TestScripts.exportData import ExportTests
from CommcareHQ.TestScripts.groups import GroupsTests
from CommcareHQ.TestScripts.menuVisibility import MenuVisibilityTests
from CommcareHQ.TestScripts.mobileWorkers import MobileWorkerTests
from CommcareHQ.TestScripts.organisationStructure import OrganisationStructureTests
from CommcareHQ.TestScripts.rolesPermissions import RolesPermissionsTests
from CommcareHQ.TestScripts.webappsPermission import WebAppPermissionsTests
from CommcareHQ.UserInputs.generateUserInputs import GenerateUserInputs

if __name__ == "__main__":
    loader: TestLoader = TestLoader()
    # noinspection PyTypeChecker
    SmokeTestSuite = TestSuite((
        loader.loadTestsFromTestCase(MenuVisibilityTests),
        loader.loadTestsFromTestCase(GenerateUserInputs),
        loader.loadTestsFromTestCase(MobileWorkerTests),
        loader.loadTestsFromTestCase(GroupsTests),
        loader.loadTestsFromTestCase(RolesPermissionsTests),
        loader.loadTestsFromTestCase(OrganisationStructureTests),
        loader.loadTestsFromTestCase(WebAppPermissionsTests),
        loader.loadTestsFromTestCase(CleanUps),
        loader.loadTestsFromTestCase(ExportTests)

    ))

    testRunner = HtmlTestRunner.HTMLTestRunner(output='Reports', report_name="CCHQ_Test_Result_Report",
                                               report_title='CCHQ Smoke Tests', verbosity=2, combine_reports=True)
        # 0 (quiet): you just get the total numbers of tests executed and the global result
        #1 (default): you get the same plus a dot for every successful test or a F for every failure
        #2 (verbose): you get the help string of every test and the result
    testRunner.run(SmokeTestSuite)
