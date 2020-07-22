from unittest import TestLoader, TestSuite, TextTestRunner
from SeleniumCCHQ.CommcareHQ.TestScripts.menuVisibility import MenuVisibilityTests
from SeleniumCCHQ.CommcareHQ.TestScripts.mobileWorkers import MobileWorkerTests

if __name__ == "__main__":
    loader = TestLoader()
    SmokeTestSuite = TestSuite((
        loader.loadTestsFromTestCase(MenuVisibilityTests),
        loader.loadTestsFromTestCase(MobileWorkerTests)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(SmokeTestSuite)


