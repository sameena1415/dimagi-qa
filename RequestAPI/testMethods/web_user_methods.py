from RequestAPI.testMethods.base import Base
import jsonpath
import json

from RequestAPI.userInputs.generate_random_string import fetch_random_string, fetch_phone_number
from RequestAPI.userInputs.user_inputs import UserData


class WebUserMethods(Base):
    def __init__(self, settings):
        self.filepath = UserData.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                      'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}


    def web_user_creation(self, uri, input_file, login_user, login_pass):
        URL = uri+'web-user/'
        file = open(self.filepath+input_file, "r")
        request_input = json.loads(file.read())
        request_input["password"] = self.password
        request_input["first_name"] = "Web_"+fetch_random_string()


        print(request_input, URL)
        result = self.post_api(URL, request_input, login_user, login_pass, self.headers)
        json_response = json.loads(result)
        print((jsonpath.jsonpath(json_response,"id"))[0])
        return (jsonpath.jsonpath(json_response,"id"))[0]


    def web_user_edit(self, uri,mobile_user_id, input_file, login_user, login_pass):
        URL = uri+'web-user/'+mobile_user_id+'/'
        file = open(self.filepath+input_file, "r")
        request_input = json.loads(file.read())
        request_input["first_name"] = "Web_"+fetch_random_string()
        request_input["password"] = self.password
        request_input["phone_numbers"] = fetch_phone_number()
        print(request_input, URL)
        self.put_api(URL, request_input, login_user, login_pass, self.headers)


    def web_user_get(self, uri, login_user, login_pass):
        URL = uri+'web-user/'
        self.get_api(URL, login_user, login_pass, self.headers)