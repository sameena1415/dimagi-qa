from robot.api.deco import keyword
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@keyword("Get Chromedriver Path")
def get_chromedriver_path():
    chrome_options = webdriver.ChromeOptions()
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

    driver_path = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    print(driver_path)
    return driver_path
