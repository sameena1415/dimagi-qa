from HQSmokeTests.testPages.home.home_page import HomePage
from HQSmokeTests.testPages.benchmark.benchmark_page import BenchmarkPage
from HQSmokeTests.userInputs.test_data import TestData

def test_case_benchmaark(driver):
    col_list = ['caseid', 'name']  # declaring an empty list for the randomly generated case names
    value_list = ['', 'value']
    data_dict = {'caseid': '', 'name': 'value'}

    menu = HomePage(driver)
    menu.data_menu()
    bench = BenchmarkPage(driver)
    filename = bench.create_excel(TestData.col_start, TestData.col_end, TestData.output_path, data_dict)
    bench.excel_upload(TestData.output_path, filename)
    # caseid = bench.excel_download()
    load_time = bench.wait_for_page_load_completion(TestData.col_end,)
    bench.write_time_to_output(TestData.col_start, TestData.col_end,TestData.output_csv,load_time)

