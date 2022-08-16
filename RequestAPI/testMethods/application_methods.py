from RequestAPI.testMethods.base import Base
from common_utilities.path_settings import PathSettings


class ApplicationMethods(Base):
    def __init__(self, settings):
        self.filepath = PathSettings.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                      'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}


    def get_application_list(self, uri, login_user, login_pass):
        URL = uri+'application/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        print(json_response['objects'][0]['id'])
        return json_response['objects'][0]['id']

    def get_application_structure(self, uri,mobile_user_id, login_user, login_pass):
        URL = uri+'application/'+mobile_user_id+'/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)
