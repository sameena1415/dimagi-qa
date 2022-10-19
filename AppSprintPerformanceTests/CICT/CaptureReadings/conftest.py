import os
import pytest

from configparser import ConfigParser
from pathlib import Path
from common_utilities.fixtures import *

from AppSprintPerformanceTests.CICT.UserInputs.ny_cict_user_inputs import NYUserData
from AppSprintPerformanceTests.CICT.UserInputs.co_cict_user_inputs import COUserData

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

""""This file provides fixture functions for driver initialization"""

global driver


@pytest.fixture(scope="module", autouse=True)
def driver(settings, browser):
    web_driver = None
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()
    if settings.get("CI") == "true":
        if browser == "chrome":
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('disable-extensions')
            chrome_options.add_argument('--safebrowsing-disable-download-protection')
            chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
            chrome_options.add_argument('window-size=1920,1080')
            chrome_options.add_argument("--disable-setuid-sandbox")
            chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": str(PathSettings.DOWNLOAD_PATH),
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True})
        elif browser == "firefox":
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('disable-extensions')
            firefox_options.add_argument('--safebrowsing-disable-download-protection')
            firefox_options.add_argument('--safebrowsing-disable-extension-blacklist')
            firefox_options.add_argument('window-size=1920,1080')
            firefox_options.add_argument("--disable-setuid-sandbox")
            firefox_options.add_argument('--start-maximized')
            firefox_options.add_argument('--disable-dev-shm-usage')
            firefox_options.add_argument('--headless')
            firefox_options.add_argument("--disable-notifications")
            firefox_options.set_preference("browser.download.dir", str(PathSettings.DOWNLOAD_PATH))
    if browser == "chrome":
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        print("Chrome version:", web_driver.capabilities['browserVersion'])
    elif browser == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
    else:
        print("Provide valid browser")
    login = LoginPage(web_driver, settings["url"])
    login.login(settings["ush_login_username"], settings["ush_login_password"], settings["ush_user_prod_auth_key"])
    yield web_driver
    web_driver.quit()


@pytest.fixture(scope="session", autouse=True)
def environment_settings_for_cicit_perf(appsite):
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_USH_LOGIN_USERNAME
                DIMAGIQA_USH_LOGIN_PASSWORD
                DIMAGIQA_USH_USER_PROD_AUTH_KEY

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["ush_login_username", "ush_login_password", "ush_user_prod_auth_key"]:
        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    if "url" not in settings:
        if appsite == "CO":
            settings["url"] = f"https://www.commcarehq.org/a/{COUserData.project_space}/cloudcare/apps/v2/"
        elif appsite == "NY":
            settings["url"] = f"https://www.commcarehq.org/a/{NYUserData.project_space}/cloudcare/apps/v2/"
    return settings


@pytest.fixture(scope="session", autouse=True)
def settings(environment_settings_for_cicit_perf, appsite):
    if os.environ.get("CI") == "true":
        settings = environment_settings_for_cicit_perf
        settings["CI"] = "true"
        if any(x not in settings for x in
               ["url", "ush_login_username", "ush_login_password", "ush_user_prod_auth_key"]):
            lines = environment_settings_for_cicit_perf.__doc__.splitlines()
            vars_ = "\n  ".join(line.strip() for line in lines if "DIMAGIQA_" in line)
            raise RuntimeError(
                f"Environment variables not set:\n  {vars_}\n\n"
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

    # updates the url with the project domain while testing in local
    if appsite == "CO":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{COUserData.project_space}/cloudcare/apps/v2/"
    elif appsite == "NY":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{NYUserData.project_space}/cloudcare/apps/v2/"
    return settings["default"]
