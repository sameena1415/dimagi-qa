from RequestAPI.testMethods.base import Base
import jsonpath
import json

from RequestAPI.userInputs.generate_random_string import fetch_random_string, fetch_phone_number, fetch_random_boolean
from RequestAPI.userInputs.user_inputs import UserData


class GroupsMethods(Base):
    def __init__(self, settings):
        self.filepath = UserData.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                      'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}

    def get_group_list(self, uri,  login_user, login_pass):
        URL = uri + 'group/'
        response = self.get_api(URL, login_user, login_pass, self.headers)
        print(response.status_code)

    def get_individual_api_group(self, uri, mobile_id, login_user, login_pass):
        URL = uri + 'group/' + mobile_id + '/'
        response = self.get_api(URL, login_user, login_pass, self.headers)
        print(response.status_code)

    def bulk_api_create_group(self, uri, input_file, login_user, login_pass):
        URL = uri+'group/'
        file = open(self.filepath+input_file, "r")
        request_input = json.loads(file.read())
        request_input["case_sharing"] = fetch_random_boolean()
        request_input["name"] = "Group_"+fetch_random_string()
        request_input["reporting"] = fetch_random_boolean()

        print(request_input, URL)
        result = self.post_api(URL, request_input, login_user, login_pass, self.headers)
        json_response = json.loads(result.text)
        # print(json_response)
        print((jsonpath.jsonpath(json_response,"id"))[0])
        return (jsonpath.jsonpath(json_response,"id"))[0]


    def bulk_api_create_multiple_group(self, uri, input_file, login_user, login_pass):
        URL = uri+'group/'
        file = open(self.filepath+input_file, "r")
        request_input = json.loads(file.read())
        print(request_input, URL)
        self.patch_api(URL, request_input, login_user, login_pass, self.headers)


    def individual_api_edit_group(self, uri,mobile_id, input_file, login_user, login_pass):
        URL = uri+'group/'+mobile_id+'/'
        file = open(self.filepath+input_file, "r")
        request_input = json.loads(file.read())
        request_input["case_sharing"] = fetch_random_boolean()
        request_input["name"] = "Updated_Group_"+fetch_random_string()
        request_input["reporting"] = fetch_random_boolean()
        print(request_input, URL)
        self.put_api(URL, request_input, login_user, login_pass, self.headers)

    def delete_individual_api_group(self, uri, mobile_id, login_user, login_pass):
        URL = uri + 'group/' + mobile_id + '/'
        self.delete_api(URL, login_user, login_pass, self.headers)
