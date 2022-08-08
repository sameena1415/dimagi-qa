from configparser import ConfigParser
from pathlib import Path

import pytest
from HQSmokeTests.userInputs.user_inputs import UserData
from HQSmokeTests.testPages.base.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

global driver


@pytest.fixture(scope="session")
def load_settings():
    path = Path(__file__).parent / "settings.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    return settings["default"]


@pytest.fixture(scope="module")
def driver(load_settings):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--safebrowsing-disable-download-protection')
    chrome_options.add_argument('--safebrowsing-disable-extension-blacklist')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": str(UserData.DOWNLOAD_PATH),
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    print("Chrome version:", driver.capabilities['browserVersion'])
    login = LoginPage(driver, load_settings["url"])
    login.login(load_settings["login_username"], load_settings["login_password"])
    yield driver
    driver.quit()


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


def _capture_screenshot(driver):
    return driver.get_screenshot_as_base64()
