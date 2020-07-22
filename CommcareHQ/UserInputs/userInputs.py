from pathlib import Path


class UserInputs:

    # inputs for login page
    driver_path = Path(str(Path.home())+"\AutomationProjects\SeleniumCCHQ\Drivers\chromedriver.exe")
    url = "https://www.commcarehq.org/accounts/login/"
    login_username = "automation.user.commcarehq@gmail.com"
    login_password = "pass@123"

    # inputs for mobile worker page
    mobile_worker_username = "user89"
    mobile_worker_password = "1234"

    # inputs for edit user field menu
    user_property = "zz"
    label = "zz"
    choice = "zz"

    # inputs for group menu
    group_name = "ABC"

