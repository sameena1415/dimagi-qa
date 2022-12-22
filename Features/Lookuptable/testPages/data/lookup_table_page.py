import time
import glob
import os.path
from pathlib import Path

from selenium.webdriver.common.by import By
from common_utilities.Excel.excel_manage import ExcelManager
from common_utilities.generate_random_string import fetch_random_string, fetch_string_with_special_chars
from common_utilities.selenium.base_page import BasePage
from Features.Lookuptable.userInputs.user_inputs import UserData

""""Contains test page elements and functions related to the Lookup Table module"""


class LookUpTablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.table_id_name = "lookuptable_" + str(fetch_random_string())
        self.dummyid = str(fetch_string_with_special_chars)
        self.table_id_fields = "(//label[.='Table ID'][@class='control-label col-sm-2']//following-sibling::div/input[@type='text' and @class = 'form-control'])"
        self.description_fields = "(//label[.='Description'][@class='control-label col-sm-2']//following-sibling::div/input[@type='text' and @class = 'form-control'])"
        self.table_created = "(//td/span[text()='" + self.table_id_name + "'])[1]"
        self.Data = (By.XPATH, "/html/body/div[1]/div[1]/div/nav/ul/li[3]/a")
        self.view_all = (By.LINK_TEXT, "View All")
        self.manage_tables_link = (By.LINK_TEXT, "Manage Tables")
        self.upload_table = (By.ID, "bulk_upload_file")
        self.upload = (By.XPATH, "(//*[@id='uploadForm']/div/div/button)")
        self.successmsg = (By.XPATH, "(//*[@class='alert alert-success']/p)")
        self.errorUploadmsg = (By.XPATH, "//*[@id='hq-messages-container']/div/div/div[1]")
        self.errormsg = (By.XPATH, "//*[@id='FailText']/p")
        self.all = (By.LINK_TEXT, "all")
        self.none = (By.LINK_TEXT, "none")
        self.edit = (By.XPATH, "(//tr[td[span[text()='upload_1']]]//button)[1]")
        self.edit_field = (
            By.XPATH, "//div[div[h4[span[text()='upload_1']]]]//input[contains(@data-bind,'description')]")
        self.new_field = (By.XPATH, "//div[div[h4[span[text()='upload_1']]]]//button[@data-bind='click: addField']")
        self.new_value = (By.XPATH,
                          "//div[div[h4[span[text()='upload_1']]]]/div[@class='modal-body form-horizontal']/div/table[@class='table table-striped table-bordered']/tbody/tr[2]/td[1]/input[@type='text']")
        self.edit_save = (By.XPATH, "//div[div[h4[span[text()='upload_1']]]]//button[@data-bind='click: saveEdit']")
        self.edit_tableid = (By.XPATH, "//div[div[h4[span[text()='upload_1']]]]//input[contains(@data-bind,'tag')][1]")
        self.fail_text = (By.XPATH, "//*[@id='editFailure']")
        self.add_table = (By.XPATH, "//button[@data-bind='click: $root.addDataType']")
        self.table_id = (By.XPATH, self.table_id_fields + "[last()]")
        self.table_id_description = (By.XPATH, self.description_fields + "[last()]")
        self.add_field = (By.XPATH, "(//button[@data-bind='click: addField'])[last()]")
        self.field_name = (By.XPATH, "(//input[contains(@data-bind,'value: tag, valueUpdate: ')])[last()]")
        self.save_table = (By.XPATH, "(//button[contains(text(),'Save')][@data-bind='click: saveEdit'])[last()]")
        self.table_created_path = (By.XPATH, self.table_created)
        self.view_tables_link = (By.LINK_TEXT, "View Tables")
        self.select_table = (By.XPATH, "//select[@id='report_filter_table_id']")
        self.select_table_drop_down = (By.ID, "select2-report_filter_table_id-container")
        self.select_table_from_dropdown = (By.XPATH, "//li[contains(.,'" + self.table_id_name + "')]")
        self.view_table = (By.ID, "apply-btn")
        self.column_name = (By.XPATH, "(//div[contains(i/following-sibling::text(), '" + self.table_id_name + "')])[1]")
        self.delete_table = (
            By.XPATH, self.table_created + "//following::button[@data-bind='click: $root.removeDataType'][1]")
        self.select_checkbox = (By.XPATH, "//*[text() = '" + self.table_id_name + "'][1] /../../ td / label / input")
        self.select_hypertensioncheckbox = (By.XPATH, "//*[text() = 'hypertension'][1] /../../ td / label / input")
        self.click_download = (By.XPATH, "//*[@id='fixtures-ui']/div[1]/p/a")
        self.download_file = (By.XPATH, "//*[@id='download-progress']/div/form/a")
        self.closedownloadpopup = (By.XPATH, "//*[@id='download-progress']/../../div/button[@class='close']")
        self.erroralert_msg=(By.XPATH,"//*[@class='alert alert-danger']/h3")
        self.replace_table=(By.ID,"replace")
        self.rowcount = (By.XPATH,"//*[@id='report_table_view_lookup_tables_info']")

    def create_lookup_table(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.add_table)
        self.send_keys(self.table_id, self.table_id_name)
        self.send_keys(self.table_id_description, self.table_id_name)
        self.wait_to_click(self.add_field)
        self.send_keys(self.field_name, self.table_id_name)
        self.wait_to_click(self.save_table)
        time.sleep(2)
        assert self.is_present_and_displayed(self.table_created_path)
        print("LookUp Table created successfully!")
        return self.table_id_name

    def create_download_lookup_table_without_field(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.add_table)
        self.send_keys(self.table_id, self.table_id_name)
        self.send_keys(self.table_id_description, self.table_id_name)
        self.wait_to_click(self.save_table)
        time.sleep(2)
        assert self.is_present_and_displayed(self.table_created_path)
        print("LookUp Table created successfully!")
        self.download1()
        return self.table_id_name

    def view_lookup_table(self,table_id_name):
        self.wait_to_click(self.view_tables_link)
        self.wait_to_click(self.select_table_drop_down)
        self.select_by_text(self.select_table, self.table_id_name)
        self.js_click(self.view_table)
        #assert self.is_present_and_displayed(self.column_name)
        print("LookUp Table can be viewed successfully!")

    def delete_lookup_table(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.delete_table)
        obj = self.driver.switch_to.alert
        obj.accept()
        print("LookUp Table deleted successfully!")

    def upload_1(self, filepath, TableCount):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_clear_and_send_keys(self.upload_table, filepath)
        self.scroll_to_bottom()
        self.wait_to_click(self.upload)
        self.wait_for_element(self.successmsg, 10)
        success = self.get_text(self.successmsg)
        successmsg = "Successfully uploaded "+ TableCount + " tables."
        assert success == successmsg
        self.wait_to_click(self.manage_tables_link)

    def err_upload(self, filepath):
        self.wait_to_click(self.Data)
        self.wait_to_click(self.view_all)
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_clear_and_send_keys(self.upload_table, filepath)
        self.wait_to_click(self.upload)
        time.sleep(20)

    def invalid_data_assert(self):
        invalid_data = self.get_text(self.erroralert_msg)
        assert invalid_data == UserData.invalid_data_assert

    def missing_data_assert(self):
        missing_data = self.get_text(self.errorUploadmsg)
        new = missing_data.split(':')[0]
        assert  UserData.missing_data_assert in missing_data

    def selects_deselects(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.all)
        self.wait_to_click(self.none)

    def edit_table(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.edit)
        self.wait_to_clear_and_send_keys(self.edit_field, 'testing')
        self.wait_to_click(self.edit_save)
        self.wait_to_click(self.edit)
        self.wait_to_click(self.edit_save)

    def create_dummyid(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.add_table)
        self.send_keys(self.table_id, self.dummyid)
        self.send_keys(self.table_id_description, self.dummyid)
        self.wait_to_click(self.add_field)
        self.send_keys(self.field_name, self.dummyid)
        self.wait_to_click(self.save_table)
        fail = self.get_text(self.errormsg)
        assert fail == "Could not update table because field names were not correctly formatted"
        print("error message displayed")
        self.wait_to_click(self.manage_tables_link)

    def edit_dummy_data(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.edit)
        self.wait_to_click(self.new_field)
        self.send_keys(self.new_value, '@!@$#%$^%&^*')
        self.wait_to_click(self.edit_save)
        fail = self.get_text(self.errormsg)
        assert fail == "Could not update table because field names were not correctly formatted"
        print("error message displayed")
        self.wait_to_click(self.manage_tables_link)

    def download1(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.select_checkbox)
        self.wait_to_click(self.click_download)
        self.wait_to_click(self.download_file)
        time.sleep(3)
        self.wait_to_click(self.closedownloadpopup)

    def download1_specificTable(self):
        self.wait_to_click(self.manage_tables_link)
        self.wait_to_click(self.select_hypertensioncheckbox)
        self.wait_to_click(self.click_download)
        self.wait_to_click(self.download_file)
        time.sleep(3)
        self.wait_to_click(self.closedownloadpopup)

    def latest_download_file(self):
        Location_path = str(Path.home() / "Downloads")
        file_type = r'\*xlsx'
        files = glob.glob(Location_path + file_type)
        max_file = max(files, key=os.path.getctime)
        return max_file

    def create_download_lookuptable(self):
        self.create_lookup_table()
        self.download1()
        return self.table_id_name

    def write_data_excel(self,table_id, path):
        excel = ExcelManager(path)
        for x in UserData.col_headers:
            for i in range(1, 2):
                col = excel.col_size(table_id)
                excel.write_excel_data(table_id, 1, col + i, x)
            excel.write_data(table_id, UserData.data_list1)
            excel.write_data(table_id, UserData.data_list2)

    def update_excel_user_value(self,table_id,path):
        excel = ExcelManager(path)
        col = excel.col_size(table_id)
        excel.write_excel_data(table_id, 1, col + 1, "user 1")
        excel.upload_to_path(table_id, UserData.data_list)

    def update_excel_group_value(self,table_id,path):
        excel = ExcelManager(path)
        col = excel.col_size(table_id)
        excel.write_excel_data(table_id, 1, col + 1, "group 1")
        excel.upload_to_path(table_id, UserData.data_list)

    def compare_excel(self,df1,df2,compareflag):
        if(compareflag ==0):
            assert df1 == df2
            print("Data is same")
        else:
            assert df1 != df2
            print("Data is different in both excels")

    def download_update_7(self, tableid, path):
        excel = ExcelManager(path)
        df1 = excel.read_excel(tableid)
        self.err_upload(path)
        df2 = excel.read_excel(tableid)
        return df1, df2

    def download_update_8(self,path,table_id):
        excel = ExcelManager(path)
        col = excel.col_size(table_id)
        excel.write_excel_data(table_id, 1, col + 1, "user 1")
        excel.write_excel_data(table_id, 1, col + 2, "group 1")
        excel.write_data(table_id, UserData.data_list1)
        self.err_upload(path)
        d1 = excel.read_excel(table_id)
        print("data1", d1)
        excel.write_excel_data(table_id, 2, 4, 'kiran')
        excel.write_excel_data(table_id, 2, 5, '123')
        self.err_upload(path)
        d2 = excel.read_excel(table_id)
        print("data2", d2)
        return d1, d2

    def replace_existing_table(self, filepath):
        self.wait_to_click(self.manage_tables_link)
        self.send_keys(self.upload_table, filepath)
        self.scroll_to_bottom()
        self.wait_to_click(self.replace_table)
        self.wait_to_click(self.upload)
        self.wait_to_click(self.manage_tables_link)
    def delete_row_from_table(self, downloadpath, tablename):
        download_path = self.latest_download_file()
        excel = ExcelManager(download_path)
        excel.write_data(tablename, UserData.data_list1)
        self.err_upload(download_path)
        self.download1()
        self.view_lookup_table(tablename)
        row_count_before = self.rowCount_table()
        download_path_1 = self.latest_download_file()
        excel = ExcelManager(download_path_1)
        excel.delete_row(tablename, 2)
        self.replace_existing_table(download_path_1)
        self.view_lookup_table(tablename)
        row_count_after = self.rowCount_table()
        assert row_count_before > row_count_after
        print("Row got successfully Deleted")

    def rowCount_table(self):
        text = self.get_text(self.rowcount)
        rowcount = text[18:20].strip()
        return rowcount

    def update_delete_field(self,download_path,tablename):
        excel = ExcelManager(download_path)
        excel.upload_to_path(tablename, UserData.data_list)
        self.err_upload(download_path)
        self.view_lookup_table(tablename)
        row_count_before = self.rowCount_table()
        download_path_1 = self.latest_download_file()
        excel = ExcelManager(download_path_1)
        excel.write_excel_data(tablename, 3, 2, 'Y')
        self.replace_existing_table(download_path_1)
        self.view_lookup_table(tablename)
        row_count_after = self.rowCount_table()
        assert row_count_before > row_count_after
        print("Row got successfully Deleted")

    def attribute_2(self,download_path,tablename):
        download_path = self.latest_download_file()
        excel = ExcelManager(download_path)
        excel.write_excel_data("types", 1, 4, 'field 1')
        excel.write_excel_data("types", 2, 4, 'C1')
        excel.write_excel_data("types", 1, 5, 'field 2')
        excel.write_excel_data("types", 2, 5, 'C2')
        excel.write_excel_data(tablename, 1, 3, 'field:C1')
        excel.write_excel_data(tablename, 1, 4, 'field:C2')
        excel.write_data(tablename, UserData.new_datalist)
        self.err_upload(download_path)
        self.view_lookup_table(tablename)
        UIrows = self.rowCount_table()
        self.download1()
        excelrows = excel.row_size(tablename)
        assert int(UIrows) == (excelrows - 1)

    def delete_field_columns(self,downloadpath,tablename):
        downloadpath = self.latest_download_file()
        excel = ExcelManager(downloadpath)
        col_TypeSheet_before = excel.col_size("types")
        col1 = excel.col_size(tablename)
        excel.delete_column('types',4)
        excel.delete_column(tablename,3)
        self.err_upload(downloadpath)
        self.view_lookup_table(tablename)
        col_TypeSheet = excel.col_size("types")
        col2 = excel.col_size(tablename)
        assert col_TypeSheet_before > col_TypeSheet
        assert col1>col2
        print("Fields got deleted")
