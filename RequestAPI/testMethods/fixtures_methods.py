from RequestAPI.testMethods.base import Base
from common_utilities.path_settings import PathSettings


class FixturesMethods(Base):
    def __init__(self, settings):
        self.filepath = PathSettings.ROOT+"/RequestAPI/Payloads/"
        self.password = settings["password"]
        self.headers={'Content-Type':'application/json',
                      'Authorization': 'ApiKey '+settings['login_user']+':'+settings['api_key']}


    def get_list_of_fixture_type_api_all_lookup_table(self, uri, login_user, login_pass):
        URL = uri+'fixture/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        # print(json_response['objects'][0]['id'])
        # return json_response['objects'][0]['id']

    def get_specific_fixture_type_api_single_fixture_item(self, uri, login_user, login_pass):
        URL = uri+'fixture/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)

    def get_specific_fixture_type_api_specific_fixture_table(self, uri, login_user, login_pass):
        URL = uri+'fixture/?fixture_type=case_search_choices'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        json_response = result.json()
        # print(json_response['objects'][0]['id'])
        # return json_response['objects'][0]['id']

    def get_location_type_data(self, uri, login_user, login_pass):
        URL = uri+'location_type/'
        result = self.get_api(URL, login_user, login_pass, self.headers)
        print(result.status_code)
