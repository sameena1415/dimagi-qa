from RequestAPI.testMethods.base import Base
import json

from RequestAPI.userInputs.user_inputs import UserData


class MiscellaneousMethods(Base):
    def __init__(self, settings):
        self.filepath = UserData.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                    'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}

    def sso_api_post(self, uri, input_file, login_user, login_pass):
        URL = uri + 'sso/'
        file = open(self.filepath + input_file, "r")
        request_input = json.loads(file.read())
        request_input['username']=login_user
        print(request_input, URL)
        self.post_api(URL, request_input, login_user, login_pass, self.headers)

    def get_list_data_forwarding_api(self, uri, login_user, login_pass):
        URL = uri+'data-forwarding/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)

    def get_user_identity_api(self, uri, login_user, login_pass):
        URL = uri+'identity/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)

    def get_user_domain_list_api(self, uri, login_user, login_pass):
        URL = uri+'user_domains'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)
