import csv
import os.path
import time

from Config.config import TestData
from Tests.APITests import write_person_data
from Tests.DataFileCreation import create_household_data, create_person_data, create_parent_external_id_list
from Tests.FileReadWrite import *
from Tests.FormCreation import create_forms, create_adverse_events_forms, create_vaccine_stock_forms
from Tests.RandomFormValueGenerator import *
from Tests.RandomStringGenerator import household_name_genrator


class DataCreation:
    case_name_list = list()  # declaring an empty list for the randomly generated case names
    person_case_name_list = list()
    original_case_names_household = list()

    def household_data_creation(input_file_path, output_path):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        # reading the data from the input file as a dictionary
        owner_household_dict = read_owner_id(input_file_path)

        # counting total rows of owners in the input sheet
        total_owners = len(owner_household_dict)
        print("Total Owners in the list: ", total_owners)

        # storing the dictionary keys in a list and creating a list of all owner IDs
        owner_list = owner_household_dict.keys()

        # calculating the total sum of the household cases
        total_case_counts = sum(owner_household_dict.values())
        print(total_case_counts)

        # converting the set of all the randomly generated household names to a list

        prefix_text = "HH_"
        case_name_list = list(household_name_genrator(prefix_text, total_case_counts))

        # original_case_names_household=case_name_list

        # loop to generate the test outputs
        for owner in owner_list:
            # taking the household counts for the owner to pass as an argument later
            household_counts = owner_household_dict[owner]
            print("Total Household counts for owner:" + owner + " is :", household_counts)

            # calling the function to create the output files
            create_household_data(output_path, owner, household_counts, case_name_list)

    def person_data_creation(input_file_path, output_path, household_output_path1):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        # reading the data from the input file as a dictionary
        owner_household_dict = read_owner_id(input_file_path)

        # counting total rows of owners in the input sheet
        total_owners = len(owner_household_dict)
        print("Total Owners in the list: ", total_owners)

        # storing the dictionary keys in a list and creating a list of all owner IDs
        owner_list = owner_household_dict.keys()

        # calculating the total sum of the household cases
        total_case_counts = sum(owner_household_dict.values())
        print(total_case_counts)

        # converting the set of all the randomly generated household names to a list
        prefix_text = "CL_"
        person_case_name_list = list(household_name_genrator(prefix_text, total_case_counts))

        # loop to generate the test outputs
        for owner in owner_list:
            # taking the household counts for the owner to pass as an argument later
            person_case_counts = owner_household_dict[owner]
            print("Total Person cases counts for owner:" + owner + " is :", person_case_counts)
            parent_id_list = create_parent_external_id_list(household_output_path1, owner, person_case_counts)
            # calling the function to create the output files
            create_person_data(output_path, owner, person_case_counts, person_case_name_list, parent_id_list)

    def cc_form_creation(input_file, input_xml, output_path):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        # reading the data from the input file as a dictionary
        owner_form_dict = read_owner_id(input_file)

        # counting total rows of owners in the input sheet
        total_owners = len(owner_form_dict)
        print("Total Owners in the list: ", total_owners)

        # storing the dictionary keys in a list and creating a list of all owner IDs
        owner_list = owner_form_dict.keys()

        # calculating the total sum of the household cases
        total_case_counts = sum(owner_form_dict.values())
        print(total_case_counts)

        instance_id_list = list(instance_id_generator(total_case_counts))
        write_ids_to_csv(instance_id_list, output_path)
        # print(instance_id_list)
        # loop to generate the test outputs
        for owner in owner_list:
            form_counts = owner_form_dict[owner]
            # if not os.path.isdir(output_path + '/' + owner):
            #     os.mkdir(output_path + '/' + owner)
            # calling the function to create the output files
            create_forms(output_path, input_xml, owner, form_counts, instance_id_list)
        print("All forms submitted successfully.")

    def ae_form_creation(input_file, input_xml, output_path):
        if not os.path.isdir(output_path):
            os.mkdir(output_path)

        # reading the data from the input file as a dictionary
        owner_dict = read_owner_id(input_file)

        # counting total rows of owners in the input sheet
        total_owners = len(owner_dict)
        print("Total Owners in the list: ", total_owners)

        # storing the dictionary keys in a list and creating a list of all owner IDs
        owner_list = owner_dict.keys()

        with open(output_path + '/JSON_Response.csv', 'w', newline='') as csvfile:  # creating the output files
            # defining the headers
            fieldnames = ['owner_id', 'case_id', 'all_conditional_vaccines', 'dob', 'vaccines_completed',
                          'date_of_registration']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writing the header to the files
            writer.writeheader()
        with open(output_path + '/Responses.csv', 'w', newline='') as csvfile:  # creating the output files
            # defining the headers
            fieldnames = ['owner_id', 'instance_id','status_code']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writing the header to the files
            writer.writeheader()

        write_person_data(TestData.AE_API_GET_URL, owner_list, output_path)

        delete_empty_vaccine_rows(output_path)
        group_by_owners(owner_list, output_path)

        #add_remaining_columns(owner_list, output_path)
        add_side_effects(owner_list, output_path)
        input_list = pd.read_csv(output_path + '/JSON_Response_filtered.csv')
        input_list.reset_index(drop=True)
        total_case_counts=len(input_list)

        instance_id_list = list(instance_id_generator(total_case_counts))
        write_ids_to_csv(instance_id_list,output_path,'JSON_Response_filtered')
        #print(instance_id_list)
        # loop to generate the test outputs
        #for case in range(total_case_counts):
            # if not os.path.isdir(output_path + '/' + owner):
            #     os.mkdir(output_path + '/' + owner)
            # calling the function to create the output files
        create_adverse_events_forms(output_path, input_xml)
        print("All forms submitted successfully.")

    def vsm_form_creation(input_file, input_xml_path, output_path):
        if not os.path.isdir(output_path):
                os.mkdir(output_path)

            # reading the data from the input file as a dictionary
        owner_dict = read_owner_id(input_file)

        #counting total rows of owners in the input sheet
        total_owners = len(owner_dict)
        print("Total Owners in the list: ", total_owners)

        owner_list = owner_dict.keys()

        # storing the dictionary keys in a list and creating a list of all owner IDs
        owner_list = owner_dict.keys()

        filename=add_owners_to_csv(owner_dict, owner_list, output_path)

        input_list = pd.read_csv(output_path + '/'+filename+'.csv')
        input_list.reset_index(drop=True)
        total_case_counts = len(input_list)

        add_stockout_check_to_csv(output_path,filename)
        instance_id_list = list(instance_id_generator(total_case_counts))
        write_ids_to_csv(instance_id_list, output_path,filename)

        with open(output_path + '/Responses.csv', 'w', newline='') as csvfile:  # creating the output files
            # defining the headers
            fieldnames = ['owner_id', 'instance_id','status_code']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # writing the header to the files
            writer.writeheader()

        create_vaccine_stock_forms(output_path, input_xml_path, filename)

    if __name__ == '__main__':
        start_time = time.time()
        # calling the function to generate Household files
        if TestData.scenario_type == "CommunityCounsellingForm":
            cc_form_creation(TestData.input_file_path, TestData.input_xml_path, TestData.output_path)
        elif TestData.scenario_type == "AdverseEventsForm":
            ae_form_creation(TestData.input_file_path, TestData.input_xml_path, TestData.output_path)
        elif TestData.scenario_type == "VaccineStockManagement":
            vsm_form_creation(TestData.input_file_path, TestData.input_xml_path, TestData.output_path)
        else:
            if TestData.scenario_type == "household":
                household_data_creation(TestData.input_file_path1, TestData.output_path1)
            elif TestData.scenario_type == "person":
                person_data_creation(TestData.input_file_path2, TestData.output_path2, TestData.output_path1)
            elif TestData.scenario_type == "household_and_person":
                household_data_creation(TestData.input_file_path1, TestData.output_path1)
                person_data_creation(TestData.input_file_path2, TestData.output_path2, TestData.output_path1)
            else:
                print("Scenario Type is not provided in the config file")

        end_time = time.time()
        print("Total time taken to execute the code: ", end_time - start_time)
        # create_household1()
