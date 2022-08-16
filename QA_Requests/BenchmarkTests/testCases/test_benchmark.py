from HQSmokeTests.testPages.home.home_page import HomePage
from QA_Requests.BenchmarkTests.testPages.benchmark.benchmark_page import BenchmarkPage
from QA_Requests.BenchmarkTests.userInputs.test_data import TestData


def test_case_benchmaark(driver):
    col_list = ['caseid', 'name']  # declaring an empty list for the randomly generated case names
    value_list = ['', 'value']
    data_dict = {'caseid': '', 'name': 'value'}

    menu = HomePage(driver)
    menu.data_menu()
    bench = BenchmarkPage(driver)
    filename = bench.create_excel(TestData.col_start, TestData.col_end, TestData.output_path, data_dict)
    bench.excel_upload(TestData.output_path, filename)
    # load_time = bench.wait_for_export_page_load_completion(TestData.col_end,)
    bench.add_case_export(TestData.col_end )
    load_time = bench.edit_case_exports(TestData.col_end)
    bench.write_time_to_output(TestData.col_start, TestData.col_end,TestData.output_csv,load_time)

