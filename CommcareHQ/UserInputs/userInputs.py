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

    #AV inputs
    form_export_name = "CCHQ Smoke Tests Form Export"
    case_export_name = "CCHQ Smoke Tests Case Export"
    dashboard_feed_form = "CCHQ Smoke Tests Dashboard Form feed"
    dashboard_feed_case = "CCHQ Smoke Tests Dashboard Case feed"
    odata_feed_form = "CCHQ Smoke Tests Odata Form feed"
    odata_feed_case = "CCHQ Smoke Tests Odata Case feed"
    download_path = "C:\\Users\\dsi-user\\Downloads"