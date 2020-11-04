import csv
import random
import string


def generate_random_string():
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    random_string = str(res)
    my_data = ['random_string', random_string]
    my_file = open('generatedUserInputs.csv', 'a+', newline='\n')
    with my_file:
        writer = csv.writer(my_file)
        writer.writerow(my_data)
        my_file.close()
        print("Random string generated")


def fetch_random_string():
    with open('generatedUserInputs.csv') as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
    return data[-1][1]


class GenerateUserInputs:
    generate_random_string()
    fetch_random_string()
