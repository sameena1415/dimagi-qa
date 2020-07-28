import csv
from pathlib import Path
import string
import random


def generate_location():
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    location = "location " + str(res)
    myData = ['location', location]
    myFile = open('UserInputs.csv', 'a+', newline='\n')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(myData)
        myFile.close()
        print("file created")


def fetch_location():
    with open('UserInputs.csv') as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
    return data[-1][1]


class UserInputs:

    # inputs for login page
    driver_path = Path(str(Path.home())+"\AutomationProjects\SeleniumCCHQ\Drivers\chromedriver.exe")
    url = "https://staging.commcarehq.org/accounts/login/"
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
    group_rename = "ABC2"

    # inputs for roles and permissions
    role_name = "Bogus"
    role_rename = "Bogus2"


