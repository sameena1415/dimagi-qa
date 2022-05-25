import json
import requests
from requests.auth import HTTPBasicAuth


class Base:
    def post_api(self, URL, input_payload, login_user, login_pass, header, type="json"):
        if type == "json":
            response = requests.post(URL, json=input_payload, headers=header,
                       auth=HTTPBasicAuth(login_user, login_pass))
            # print(response.json())
        else:
            response = requests.post(URL, data=input_payload, headers=header,
                                     auth=HTTPBasicAuth(login_user, login_pass))
        print(response.status_code)
        # print(response.headers)

        assert response.status_code == 201
        return response

    def get_api(self, URL, login_user, login_pass, header=None):
        if header == None:
            response = requests.get(URL, auth=HTTPBasicAuth(login_user, login_pass))
        else:
            response = requests.get(URL, auth=HTTPBasicAuth(login_user, login_pass), headers=header)
            print(response.text)
            assert response.status_code == 200
        return response

    def put_api(self, URL, input_payload, login_user, login_pass, header):
        response = requests.put(URL, json=input_payload,
                                 auth=HTTPBasicAuth(login_user, login_pass))
        print(response.status_code)
        assert response.status_code == 200

    def delete_api(self, URL, login_user, login_pass, header):
        response = requests.delete(URL, headers=header,
                                 auth=HTTPBasicAuth(login_user, login_pass))
        print(response.status_code)
        assert response.status_code == 204

    def patch_api(self, URL, input_payload, login_user, login_pass, header):
        response = requests.put(URL, json=input_payload,headers=header,
                                 auth=HTTPBasicAuth(login_user, login_pass))
        print(response.status_code)
        assert response.status_code == 201

    def post_api_file_upload(self, URL, data, login_user, login_pass, file):
        response = requests.request("POST", URL, data=data, files=file,
                         auth=HTTPBasicAuth(login_user, login_pass))
        print(response.status_code)
        # print(response.headers)
        return response
