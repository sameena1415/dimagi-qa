from DummyDataGenerationTaks.testPages.home.home_page import HomePage
from DummyDataGenerationTaks.testPages.dummy_data.dummy_data_generation import FileInputOutput, DummyDataGenerationPage
from DummyDataGenerationTaks.userInputs.test_data import TestData

def test_case_dummy_data(driver):
    col_list = ['number','caseid', 'name', 'full_name','date_of_birth','address','gender','locaton','disease']  # declaring an empty list for the randomly generated case names

    menu = HomePage(driver)
    menu.data_menu()
    data = FileInputOutput()
    data.generate_path( TestData.output_path)
    data.data_generation(TestData.col_start, TestData.col_end, TestData.output_csv,TestData.output_xlsx, col_list)
    data.add_disease_values(TestData.col_end, TestData.output_xlsx)
    data.add_duplicate_rows(TestData.output_xlsx)
    upload=DummyDataGenerationPage(driver)
    upload.excel_upload(TestData.output_path, TestData.file_name)
    upload.excel_download()

