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
    return data[-2][1]


def generate_location_field():
    res = ''.join(random.choices(string.digits, k=5))
    location_field = "location_field_" + str(res)
    myData = ['location_field', location_field]
    myFile = open('UserInputs.csv', 'a+', newline='\n')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(myData)
        myFile.close()
        print("file created")

# def generate_user_field_property ():
#     res = ''.join(random.choices(string.digits, k=4))
#     user_field = "user_field" + str(res)
#     myData = ['mobile_worker', user_field]
#     myFile = open('UserInputs.csv', 'a+', newline='\n')
#     with myFile:
#         writer = csv.writer(myFile)
#         writer.writerow(myData)
#         myFile.close()
#         print("file created")


def fetch_location_field():
    with open('UserInputs.csv') as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
    return data[-1][1]


class UserInputs:

    # inputs for login page
    driver_path = Path(str(Path.home())+"\AutomationProjects\SeleniumCCHQ\Drivers\chromedriver.exe")
    url = ""
    login_username = ""
    login_password = ""

    # inputs for mobile worker page
    mobile_worker_username = "user00588"
    mobile_worker_password = "1234"

    # inputs for edit user field menu
    user_property = "pp00588"
    label = "pp00588"
    choice = "pp00588"

    # inputs for group menu
    group_name = "ABC5"
    group_rename = "ABC6"

    # inputs for roles and permissions
    role_name = "Boguss"
    role_rename = "Boguss2"

    # inputs for org structure
    loc_level = "ab"



