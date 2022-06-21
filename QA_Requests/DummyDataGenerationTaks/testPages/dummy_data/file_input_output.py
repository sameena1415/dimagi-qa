import csv
import os
from random import choice, shuffle
import datetime
import random
import string
import re
import uuid
import pandas as pd

from DummyDataGenerationTaks.userInputs.generate_random_string import fetch_random_string


class FileInputOutput():

#function to randomly generate form values
    def instance_id_generator(total_case_counts):
        id_set=set() #declaring an empty set to store the unique household names

        for i in range(total_case_counts): #loop to generate the household names
            # generating 5 charaters long alphanumeric household  names
            ids=str(uuid.uuid4())

            #adding prefix to the random string: HH_ for household and CL_ for person
            id_set.add(ids)
        return id_set

    def birth_date_generator(self):
        start_date = datetime.date(1980, 1, 1)
        end_date = datetime.date(2000, 9, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    def location_selection(self):
        location_range = ['san_francisco','boston','seattle','los_angeles','new_york']
        return random.choice(location_range)

    def disease_selection_female(self,female_count, df_female):
        disease_range = ['allergies','colds_and_flu','pink_eye','diarrhea','headaches','mononucleosis','stomach_aches']
        disease = random.choices(disease_range, weights=[90, 2, 2, 1, 1, 3, 1], k=female_count)
        # print(disease)
        df_female['disease'] = disease
        return df_female

    def disease_selection_male(self, male_count, df_male):

        disease_range = ['allergies', 'colds_and_flu', 'diarrhea', 'headaches', 'mononucleosis',
                     'stomach_aches']
        disease = random.choices(disease_range, k=male_count)
        # print(disease)
        df_male['disease'] = disease
        for index, row in df_male.iterrows():
            if df_male['locaton'][index] == 'boston':
                df_male['disease'][index] = 'pink_eye'
        return df_male

    def gender_selection(self):
        gender_range = ['f','m']
        return random.choice(gender_range)

    def add_remaining_columns(self,owner_list, output_path):
        # response_list = pd.read_csv(output_path + '/JSON_Response_filtered.csv')
        final_df=pd.DataFrame()
        add_se_injection_site_swell(owner_list, output_path)
        add_se_fever(owner_list, output_path)
        add_se_nausea(owner_list, output_path)
        add_se_diarrhea(owner_list, output_path)
        add_se_loss_of_taste(owner_list, output_path)
        add_se_breathing_difficulty(owner_list, output_path)
        add_se_other(owner_list, output_path)

        populated_response_list=pd.read_csv(output_path + '/List_with_other.csv')
        populated_response_list=populated_response_list.drop(populated_response_list.columns[[0, 1, 2,3,4,5]],
                           axis = 1)
        populated_response_list.to_csv(output_path + '/JSON_Response_filtered_populated.csv', index=False)

    def data_generation(self,col_start, col_end, output_csv, output_xlsx, col_list):

        with open(output_csv, 'w', newline="") as csvfile:  # creating the output files
            # defining the headers
            writer = csv.DictWriter(csvfile, fieldnames=col_list)
            # writing the header to the files
            writer.writeheader()
            # loop to write data for each owner
            for cases in range(col_end):
                number_data = str(cases)
                name_data = 'test_' + fetch_random_string() + '_' + str(cases)
                full_name_data = 'test_' + fetch_random_string() + '_' + str(cases)
                date_of_birth_data = self.birth_date_generator()
                address_data = 'address ' + fetch_random_string() + ' ' + str(cases)
                gender_data = self.gender_selection()
                locaton_data = self.location_selection()

                # writing all the values generated to the file
                writer.writerow({'number':number_data,'caseid': '', 'name': name_data,
                                 'full_name': full_name_data,
                                 'date_of_birth': date_of_birth_data, 'address': address_data,
                                 'gender': gender_data, 'locaton': locaton_data
                                 })
        df_new = pd.read_csv(output_csv)
        # saving xlsx file
        GFG = pd.ExcelWriter(output_xlsx)
        df_new.to_excel(GFG, index=False)
        GFG.save()

    def generate_path(self, output_path):
        if not os.path.isdir(output_path):
            print('Path not present')
            os.mkdir(output_path)

    def add_disease_values(self,col_end, output_xls):
        df = pd.read_excel(output_xls)
        df_female= self.add_female_disease(df, output_xls)
        df_male=self.add_male_disease(df, output_xls)
        frames = [df_female, df_male]
        result = pd.concat(frames)
        result = result.sort_values(by='number')
        new = pd.ExcelWriter(output_xls)
        result.to_excel(new, index=False)
        new.save()

    def add_female_disease(self,df, output_xls):
        df_female = df[df['gender'] == 'f']
        female_count = df_female.shape[0]
        df_female = self.disease_selection_female(female_count, df_female)
        return df_female

    def add_male_disease(self,df, output_xls):
        df_male = df[df['gender'] == 'm']
        male_count = df_male.shape[0]
        df_male = self.disease_selection_male(male_count, df_male)
        return df_male

    def add_duplicate_rows(self,output_xlsx):
        df = pd.read_excel(output_xlsx)
        df_elements = df.sample(n=50)
        frames = [df, df_elements]
        result = pd.concat(frames)
        result.drop('number', axis=1, inplace=True)
        new = pd.ExcelWriter(output_xlsx)
        result.to_excel(new, index=False)
        new.save()