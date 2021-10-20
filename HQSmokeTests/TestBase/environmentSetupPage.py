import os
import unittest
from configparser import ConfigParser
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from HQSmokeTests.Pages.loginPage import LoginPage
from selenium.webdriver.chrome.options import Options
from HQSmokeTests.UserInputs.userInputsData import UserInputsData


class EnvironmentSetup(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        settings = load_settings()
        chrome_options = Options()
        if os.environ.get("CI") == "true":
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('disable-extensions')
            chrome_options.add_argument('--safebrowsing-disable-download-protection')
            chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('window-size=1024,768')
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": str(UserInputsData.download_path),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True})
        else:
            chrome_options.add_argument('--safebrowsing-disable-download-protection')
            chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
            chrome_options.add_experimental_option("prefs", {
                "download.prompt_for_download": False,
                "safebrowsing.enabled": True})
        driver_path = ChromeDriverManager().install()
        cls.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        try:
            cls.driver.implicitly_wait(2)
            cls.driver.get(settings["url"])
            login = LoginPage(cls.driver)
            login.enter_username(settings["login_username"])
            login.click_continue()
            login.enter_password(settings["login_password"])
            login.click_submit()
            login.accept_alert()
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
    if os.environ.get("CI") == "true":
        settings = load_settings_from_environment()
        if any(x not in settings for x in ["url", "login_username", "login_password"]):
            raise RuntimeError(
                f"Environment variables not set:\n"
                "  DIMAGIQA_URL\n"
                "  DIMAGIQA_LOGIN_USERNAME\n"
                "  DIMAGIQA_LOGIN_PASSWORD\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )
        return settings
    path = Path(__file__).parent.parent / "settings.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    return settings["default"]


def load_settings_from_environment():
    """Load settings from os.environ

    Names of environment variables:
        DIMAGIQA_URL - required unless DIMAGIQA_ENV is set
        DIMAGIQA_ENV - required if DIMAGIQA_URL is not set
        DIMAGIQA_LOGIN_USERNAME - required
        DIMAGIQA_LOGIN_PASSWORD - required

    See https://docs.github.com/en/actions/reference/encrypted-secrets
    for instructions on how to set them.
    """
    settings = {}
    for name in ["url", "login_username", "login_password"]:
        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    if "url" not in settings:
        env = os.environ["DIMAGIQA_ENV"]
        subdomain = "www" if env == "production" else env
        settings["url"] = f"https://{subdomain}.commcarehq.org/"
    return settings
