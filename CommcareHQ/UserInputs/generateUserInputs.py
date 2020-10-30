import csv
import random
import string


def generate_random_string():
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    random_string = str(res)
    myData = ['random_string', random_string]
    myFile = open('UserInputs.csv', 'a+', newline='\n')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerow(myData)
        myFile.close()
        print("Random string generated")


def fetch_random_string():
    with open('UserInputs.csv') as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
    return data[-1][1]


class GenerateUserInputs:
    generate_random_string()
    fetch_random_string()

