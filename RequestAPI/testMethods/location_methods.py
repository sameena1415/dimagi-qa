from RequestAPI.testMethods.base import Base
from common_utilities.path_settings import PathSettings


class LocationMethods(Base):
    def __init__(self, settings):
        self.filepath = PathSettings.ROOT + "/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'ApiKey ' + settings['login_user'] + ':' + settings['api_key']}

    def get_location_list(self, uri, login_user, login_pass):
        URL = uri + 'location/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        # print(json_response['objects'][0]['id'])
        # return json_response['objects'][0]['id']

    def get_location_data(self, uri, login_user, login_pass):
        URL = uri + 'location/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)

    def get_location_type_list(self, uri, login_user, login_pass):
        URL = uri + 'location_type/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        # print(json_response['objects'][0]['id'])
        # return json_response['objects'][0]['id']

    def get_location_type_data(self, uri, login_user, login_pass):
        URL = uri + 'location_type/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)
