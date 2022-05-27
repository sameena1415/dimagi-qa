from RequestAPI.testMethods.base import Base
import json

from RequestAPI.userInputs.user_inputs import UserData


class FormsMethods(Base):
    def __init__(self, settings):
        self.filepath = UserData.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                      'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}


    def get_all_forms_list(self, uri, login_user, login_pass):
        URL = uri+'form/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        print(result.status_code)
        # print(json_response['objects'][0]['id'])
        # return json_response['objects'][0]['id']

    def get_form_data(self, uri, login_user, login_pass):
        URL = uri+'form/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)

    def post_form_data_export(self, uri, input_file,login_user, login_pass):
        URL = uri+'a/ccqa2-2/reports/export/'
        file = open(self.filepath + input_file, "r")
        request_input = json.loads(file.read())
        response = self.post_api(URL, request_input, login_user, login_pass, self.headers,"json")
        print(response.status_code)