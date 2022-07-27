from QA_Requests.PerfTickets.testPages.subcase_query.generate_data import generate_path, data_generation, \
    subcase_data_generation
from QA_Requests.PerfTickets.userInputs.test_data import TestData


def test_case_dummy_data(driver):
    col_list = ['number', 'external_id', 'name', 'show_name']
    child_col_list = ['number', 'caseid', 'name', 'location', 'multi_data_1', 'receive_geopoint_1',
                      'parent_external_id', 'parent_type',
                      'hundred', 'two_hundred', 'three_hundred', 'four_hundred', 'five_hundred']
    global load, subcase
    load = 1000000
    subcase = 1
    generate_path(TestData.output_path)
    data_generation(subcase, load, TestData.output_csv, col_list, TestData.child_output_csv, col_list, driver)
    subcase_data_generation(subcase, load, TestData.child_output_csv, child_col_list, driver)
    print("Successful!")
