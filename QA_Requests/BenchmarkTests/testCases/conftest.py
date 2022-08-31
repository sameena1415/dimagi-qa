from configparser import ConfigParser
from pathlib import Path
from common_utilities.fixtures import *

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
        "download.default_directory": str(PathSettings.DOWNLOAD_PATH),
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True})
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    print("Chrome version:", driver.capabilities['browserVersion'])
    login = LoginPage(driver, load_settings["url"])
    login.login(load_settings["login_username"], load_settings["login_password"])
    yield driver
    driver.quit()