import os
import pytest

from configparser import ConfigParser
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from AppSprintPerformanceTests.CICT.UserInputs.ny_cict_user_inputs import NYUserData
from AppSprintPerformanceTests.CICT.UserInputs.co_cict_user_inputs import COUserData
from common_utilities.hq_login.login_page import LoginPage

""""This file provides fixture functions for driver initialization"""

global driver


@pytest.fixture(scope="session", autouse=True)
def environment_settings1(appsite):
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_LOGIN_USERNAME
                DIMAGIQA_LOGIN_PASSWORD

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["login_username", "login_password"]:
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
def settings1(environment_settings1, appsite):
    if os.environ.get("CI") == "true":
        settings = environment_settings1
        settings["CI"] = "true"
        if any(x not in settings for x in ["url", "login_username", "login_password"]):
            lines = environment_settings1.__doc__.splitlines()
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

    ## updates the url with the project domain while testing in local
    if appsite == "CO":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{COUserData.project_space}/cloudcare/apps/v2/"
    elif appsite == "NY":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{NYUserData.project_space}/cloudcare/apps/v2/"
    return settings["default"]


@pytest.fixture(scope="module", autouse=True)
def driver(settings1, browser, appsite):
    web_driver = None
    chrome_options = webdriver.ChromeOptions()
    firefox_options = webdriver.FirefoxOptions()
    if settings1.get("CI") == "true":
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
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True})
        elif browser == "firefox":
            firefox_options.add_argument("--headless")
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
    if browser == "chrome":
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        print("Chrome version:", web_driver.capabilities['browserVersion'])
    elif browser == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
    else:
        print("Provide valid browser")
    login = LoginPage(web_driver, settings1["url"])
    login.login(settings1["login_username"], settings1["login_password"])
    yield web_driver
    web_driver.quit()


def pytest_addoption(parser):
    """CLI args which can be used to run the tests with specified values."""
    parser.addoption("--browser", action="store", default='chrome', choices=['chrome', 'firefox'],
                     help='Your choice of browser to run tests.')
    parser.addoption("--appsite", action="store", choices=['CO', 'NY'],
                     help='Your choice of app site.')


@pytest.fixture(scope="module")
def browser(request):
    """Pytest fixture for browser"""
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def appsite(pytestconfig):
    """Pytest fixture for app site"""
    return pytestconfig.getoption("--appsite")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call" or report.when == "teardown":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("reports skipped or failed")
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot(item.funcargs["driver"])
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(web_driver):
    return web_driver.get_screenshot_as_base64()
