import unittest
from configparser import ConfigParser
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.loginPage import LoginPage


class EnvironmentSetup(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        settings = load_settings()["default"]
        driver_path = ChromeDriverManager().install()
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        try:
            cls.driver.maximize_window()
            cls.driver.get(settings["url"])
            login = LoginPage(cls.driver)
            login.enter_username(settings["login_username"])
            login.enter_password(settings["login_password"])
            login.click_submit()
        except Exception:
            cls.tearDownClass()
            raise
        print("Successfully logged in")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


def load_settings():
    path = Path(__file__).parent.parent / "settings.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    return settings
