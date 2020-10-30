from pathlib import Path


class UserInputs:
    # inputs for login page
    driver_path = Path(str(Path.home()) + "\AutomationProjects\SeleniumCCHQ\Drivers\chromedriver.exe")
    url = ""
    login_username = ""
    login_password = ""
    domain = "another-upstream"

