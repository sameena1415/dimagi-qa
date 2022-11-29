import openpyxl
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook


class ExcelManager(object):

    def __init__(self, path):
        self.path = path
        print("Path", self.path)

    def create_workbook(self):
        wb = Workbook()
        filepath = self.path
        wb.save(filepath)

    def create_sheet(self, sheet_name):
        wb = load_workbook(self.path)
        wb.create_sheet(sheet_name)
        wb.save(self.path)


    def sheet_new(self,sheet_name):
        wb = Workbook()
        ws1 = wb.create_sheet("Sheet_A")
        ws1.title = "Title_A"
        ws2 = wb.create_sheet("Sheet_B", 0)
        ws2.title = "Title_B"
        wb.save(filename='sample_book.xlsx')

    def delete_sheet(self, sheet_name):
        wb = openpyxl.load_workbook(self.path)
        sheetdelete = wb[sheet_name]
        wb.remove(sheetdelete)
        print(wb.sheetnames)
        wb.save(self.path)

    def update_sheet(self, sheet_name):
        wb = load_workbook(self.path)
        sheet = wb.active
        sheet.title = sheet_name
        wb.save(self.path)

    def write_data(self, sheet_name, list_data):
        from openpyxl import load_workbook
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        for i in list_data:
            sheet.append(i)
        wb.save(self.path)

    def read_excel(self, sheet_name):
        global data
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        row_count = sheet.max_row
        column_count = sheet.max_column
        for i in range(1, row_count + 1):
            for j in range(1, column_count + 1):
                data = sheet.cell(row=i, column=j).value
        return data

    def get_cell_data(self, sheet_name, column_name, row_num):
        global data, column_num
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        column_count = sheet.max_column
        for i in range(1, column_count + 1):
            if sheet.cell(row=1, column=i).value == column_name:
                column_num = i
        data = sheet.cell(row=row_num, column=column_num).value
        return data

    def write_excel_data(self, sheet_name, row_num, column_num, value):
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        sheet.cell(row=row_num, column=column_num).value = value
        wb.save(self.path)

    def delete_column(self, sheet_name, column_number):
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        sheet.delete_cols(column_number)
        wb.save(self.path)

    def delete_row(self, sheet_name, row_number):
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        sheet.delete_rows(row_number)
        wb.save(self.path)

    def row_size(self, sheet_name):
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        row_count = sheet.max_row
        return row_count

    def col_size(self, sheet_name):
        wb = load_workbook(self.path)
        sheet = wb[sheet_name]
        column_count = sheet.max_column
        return column_count

    def upload_to_path(self, table_id, data_list):
        col = self.col_size(table_id)
        self.write_excel_data(table_id, 1, col + 1, "user 1")
        row = self.row_size(table_id)
        self.write_data(table_id, data_list)

    def upload_data_typesSheet(self, type_data_list):
        self.write_data('types', type_data_list)


