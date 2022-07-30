import csv
import os
import names
import pandas as pd

from QA_Requests.MultiSelectPerf.import_data_using_api import post_import_cases_from_excel


def generate_path(output_path):
    if not os.path.isdir(output_path):
        print('Path not present')
        os.mkdir(output_path)


def generate_import_file(case_load_per_case_type, case_type_name, num_prop):
    generate_path("./OutputFiles")
    output_csv = "./OutputFiles/Records.csv"
    col_list = ["caseid", "name"] + ['prop{}'.format(i) for i in range(0, num_prop)]
    with open(output_csv, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=col_list)
        writer.writeheader()
        for cases in range(0, int(case_load_per_case_type)):
            value_list = ["", names.get_full_name()] + ['val{}'.format(i) for i in range(0, num_prop)]
            dic = dict(zip(col_list, value_list))
            writer.writerow(dic)
        df_new = pd.read_csv(output_csv)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file = os.path.abspath(
            os.path.join(BASE_DIR, "OutputFiles/" + f'{str(case_type_name)}.xlsx'))
        GFG = pd.ExcelWriter(file)
        df_new.to_excel(GFG, index=False)
        GFG.save()
        return file


def multi():
    domain_case_load = 100
    case_types_and_properties = {"case1": 50, "case2": 100, "case3": 200}
    case_load_per_case_type = domain_case_load / len(case_types_and_properties)
    case_properities_passed_into_form = [10, 50, 100]

    for key, value in case_types_and_properties.items():
        print("Create app with case list " + str(key))  ##TODO
        # print("Generate data of load " + str(round(case_load_per_case_type)) + " for " + str(key))  ##DONE
        # print("Add " + str(value) + " properties")  ##DONE
        file = generate_import_file(case_load_per_case_type, key, value)
        #print("Import Data Using API")  ##DONE
        post_import_cases_from_excel(file, key)
        for case_property_passed in case_properities_passed_into_form:
            print("Pass " + str(case_property_passed) + " properties to case list of " + str(key))  ##TODO
            print("Capture Readings for " + str(case_property_passed), str(key) + " workflow1")  ##TODO
            print("Capture Readings for " + str(case_property_passed), str(key) + " workflow2")  ##TODO


multi()
