from RequestAPI.testMethods.base import Base
from RequestAPI.userInputs.user_inputs import UserData


class CurlMethods(Base):
    def __init__(self, settings):
        self.filepath = UserData.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/xml'}


    def submission_api(self, uri, input_file, login_user, login_pass):
        URL = uri+'receiver/'
        file = open(self.filepath + input_file, "r")
        request_input = file.read()
        print(request_input, URL)
        self.post_api(URL, request_input, login_user, login_pass, self.headers,"xml")


    def get_restore_ota(self, uri, login_user, login_pass):
        URL = uri+'phone/restore/?version=2.0'
        result = self.get_api(URL, login_user, login_pass)
        print(result.status_code)
        assert result.status_code == 200

    def post_lookup_table_upload(self, uri, input_file, login_user, login_pass):
        URL = uri+'a/myproject/fixtures/fixapi/'
        data = {'replace': 'true'}
        file = [
            ('file-to-upload', ('case search.xlsx', open(self.filepath + input_file, 'rb'),
                                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))]
        result = self.post_api_file_upload(URL, data, login_user, login_pass, file)
        assert result.status_code == 200

    def post_import_cases_from_excel(self, uri, input_file, login_user, login_pass):
        URL = uri+'a/samveg-quick/importer/excel/bulk_upload_api/'
        data = {'case_type': 'household',
                'search_field': 'external_id',
                'search_column': 'household_id',
                'create_new_cases': 'on'}
        file = [
            ('file', ('case search.xlsx', open(self.filepath + input_file, 'rb'),
                                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))]
        result = self.post_api_file_upload(URL, data, login_user, login_pass, file)
        assert result.status_code == 200