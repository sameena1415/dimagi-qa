import os
from pathlib import Path
import pathlib


class UserInputs:
    # inputs for login page
    driver_path = Path(str(Path.home()) + "\Documents\Automation\CCHQ\Drivers\chromedriver.exe")
    #x=pathlib.Path().absolute()
    url = "https://staging.commcarehq.org/accounts/login/"
    login_username = "automation.user.commcarehq@gmail.com"
    login_password = "pass@123"
    domain = "another-upstream"

