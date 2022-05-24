from webdriver_manager.chrome import ChromeDriverManager

def get_driver_path():
    driver_path = ChromeDriverManager().install()
    return driver_path