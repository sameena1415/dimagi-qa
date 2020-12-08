import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage
from UserInputs.loginCredentials import LoginCredentials


class EnvironmentSetup(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.get(LoginCredentials.url)
        login = LoginPage(cls.driver)
        login.enter_username(LoginCredentials.login_username)
        login.enter_password(LoginCredentials.login_password)
        login.click_submit()
        login.accept_alert()
        print("Successfully logged in")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
