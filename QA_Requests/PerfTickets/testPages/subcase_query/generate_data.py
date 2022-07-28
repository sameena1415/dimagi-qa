import csv
import os
import random
import pandas as pd

from QA_Requests.PerfTickets.testPages.subcase_query.import_generated_data import post_import_cases_from_excel


def location_assign():
    loc_values = ['46.748107 8.0473685', '47.0468839 8.2179933']
    return random.choice(loc_values)


def subcase_data_generation(sub_cases, data_load, child_output_csv, child_col_list):
    counter = 0
    print(data_load, sub_cases)
    part_load = int(data_load / sub_cases)
    ranges = []
    for i in range(0, data_load, part_load):
        data_range = [i, i + part_load]
        ranges.append(data_range)
        col_start = data_range[0]
        col_end = data_range[1]
        print(data_range, col_start, col_end)
        with open(child_output_csv, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=child_col_list)
            writer.writeheader()
            for cases in range(col_start, col_end):
                number_data = str(cases)
                name_data = 'Anywhoop' + ' ' + str(cases)
                location_data = '46.8224307689092 8.223983999999996 0.0 0.0'
                multi_data = 'a b c'
                receive_geopoint_data = location_assign()
                parent_type_data = 'song_perf_' + str(sub_cases) + '_' + str(sub_cases) + '_' + str(data_load)
                parent_external_id_data = 'PERF_' + str(data_load) + '_' + str(sub_cases) + '_' + str(cases)

                writer.writerow({'number': number_data, 'caseid': '', 'name': name_data,
                                 'location': location_data, 'multi_data_1': multi_data,
                                 'receive_geopoint_1': receive_geopoint_data,
                                 'parent_external_id': parent_external_id_data,
                                 'parent_type': parent_type_data,
                                 'hundred': '100k',
                                 'two_hundred': '200k',
                                 'three_hundred': '300k',
                                 'four_hundred': '400k',
                                 'five_hundred': '500k',
                                 })
        file = read_write_excel(child_output_csv, f'Child_records_{col_start}_{col_end}.xlsx')
        counter = counter + 1
        case_type = 'show_perf_' + str(counter) + '_' + str(sub_cases) + '_' + str(data_load)
        print(counter, case_type)
        post_import_cases_from_excel(file, case_type)


def read_write_excel(child_output_csv, file_name):
    df_new = pd.read_csv(child_output_csv)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file = os.path.abspath(os.path.join(BASE_DIR, "../../testCases/OutputFiles/" + file_name))
    GFG = pd.ExcelWriter(file)
    df_new.to_excel(GFG, index=False)
    GFG.save()
    return file


def generate_path(output_path):
    if not os.path.isdir(output_path):
        print('Path not present')
        os.mkdir(output_path)


def data_generation(sub_cases, data_load, output_csv, col_list, child_output_csv, child_col_list):
    part_load = int(data_load / sub_cases)
    ranges = []
    for i in range(0, data_load, part_load):
        data_range = [i, i + part_load]
        ranges.append(data_range)
        col_start = data_range[0]
        col_end = data_range[1]
        print(data_range, col_start, col_end)
        with open(output_csv, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=col_list)
            writer.writeheader()
            for cases in range(col_start, col_end):
                number_data = str(cases)
                name_data = 'Weezers' + ' ' + str(cases)
                show_name_data = 'Anywhoop' + ' ' + str(cases)
                external_id_data = 'PERF_' + str(data_load) + '_' + str(sub_cases) + '_' + str(cases)

                writer.writerow({'number': number_data, 'external_id': external_id_data,
                                 'name': name_data, 'show_name': show_name_data
                                 })
        file = read_write_excel(output_csv, f'Parent_records_{col_start}_{col_end}.xlsx')
        case_type = 'song_perf_' + str(sub_cases) + '_' + str(data_load)
        post_import_cases_from_excel(file, case_type)


def subcase_data_generation_common(sub_cases, data_load, child_output_csv, child_col_list):
    counter = 0
    print(data_load, sub_cases)
    part_load = int(data_load / sub_cases)
    ranges = []
    for i in range(0, data_load, part_load):
        data_range = [i, i + part_load]
        ranges.append(data_range)
        col_start = data_range[0]
        col_end = data_range[1]
        print(data_range, col_start, col_end)
        with open(child_output_csv, 'w', newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=child_col_list)
            writer.writeheader()
            for cases in range(col_start, col_end):
                number_data = str(cases)
                name_data = 'Anywhoop' + ' ' + str(cases)
                location_data = '46.8224307689092 8.223983999999996 0.0 0.0'
                multi_data = 'a b c'
                receive_geopoint_data = location_assign()
                parent_type_data = 'song_perf_' + str(sub_cases) + '_' + str(sub_cases) + '_' + str(data_load)
                parent_external_id_data = 'PERF_' + str(data_load) + '_' + str(sub_cases) + '_' + str(cases)
                writer.writerow({'number': number_data, 'caseid': '', 'name': name_data,
                                 'location': location_data, 'multi_data_1': multi_data,
                                 'receive_geopoint_1': receive_geopoint_data,
                                 'parent_external_id': parent_external_id_data,
                                 'parent_type': parent_type_data,
                                 'hundred': '100k',
                                 'two_hundred': '200k',
                                 'three_hundred': '300k',
                                 'four_hundred': '400k',
                                 'five_hundred': '500k',
                                 })
        file = read_write_excel(child_output_csv, f'Child_records_{col_start}_{col_end}.xlsx')
        counter = counter + 1
        case_type = 'show_perf_' + str(counter) + '_' + str(sub_cases) + '_' + str(data_load)
        print(counter, case_type)
        post_import_cases_from_excel(file, case_type)
