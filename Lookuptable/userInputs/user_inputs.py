""""Contains test data that are used as user inputs across various areasn in CCHQ"""
import os

from common_utilities.generate_random_string import fetch_random_string
from common_utilities.path_settings import PathSettings


class UserData:
    """User Test Data"""
    user_input_base_dir = os.path.dirname(os.path.abspath(__file__))
    # Pre-setup application and case names
    field_val = 'table'+ str(fetch_random_string())
    data_list = [(1, 'N', '1', 'RWS%DTUYIG*&^%'), (2, 'N', '2', '!#@$%#$RFGH:')]
    data_list_delete = [(1, 'Y', '1', 'RWS%DTUYIG*&^%'), (2, 'N', '2', '!#@$%#$RFGH:')]
    data_list1 = [(1, 'N', '1',"appiumtest"),(2, 'N', '2',"") ]
    data_list2 = [(3, 'N', '3','',"123"),(4, 'N', '4','',"group2") ]
    edit_data = [(1, 'N', '1', 'kiran'), (2, 'N', '2', 'henry')]
    type_data_list = [('N', field_val, 'yes',field_val)]
    type_sheet_headers = [('UID', 'Delete(Y/N)', 'field: '+ field_val)]
    data_upload_path = PathSettings.ROOT + "\\userinputs\\upload_1.xlsx"
    hypertension_upload_path = PathSettings.ROOT + "\\userinputs\\Hypertension.xlsx"
    malformed_document_upload_path = PathSettings.ROOT + "\\userinputs\\MalformedDocument.xlsx"
    invalid_data_assert = "However, we ran into the following problems:"
    missing_data_assert = "Please fix the following formatting issues in your Excel file"
    col_headers = ["user 1", "group 1"]


