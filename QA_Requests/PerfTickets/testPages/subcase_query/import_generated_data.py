import configparser
import requests


def post_api(URL, input_payload, login_user, login_pass, header, type="json"):
    if type == "json":
        response = requests.post(URL, json=input_payload, headers=header)
    else:
        response = requests.post(URL, data=input_payload, headers=header)
    assert response.status_code == 200
    return response


def post_api_file_upload(URL, data, login_user, login_pass, file, header):
    response = requests.request("POST", URL, data=data, files=file, headers=header)
    print(response.status_code)
    print(response.headers)
    return response


def post_import_cases_from_excel(file_path, case):
    config = configparser.ConfigParser()
    config.read('../settings.cfg')
    login_user = config.get('default', 'login_username')
    login_pass = config.get('default', 'login_password')
    api_key = config.get('default', 'api_key')
    uri = config.get('default', 'url')

    URL = uri + "importer/excel/bulk_upload_api/"
    data = {'case_type': case,
            'search_field': 'case_id',
            'search_column': 'caseid',
            'create_new_cases': 'on'}
    file = [
        ('file', (file_path, open(file_path, 'rb'),
                  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))]

    headers = {'Authorization': 'ApiKey ' + login_user + ':' + api_key}
    result = post_api_file_upload(URL, data, login_user, login_pass, file, headers)
    assert result.status_code == 200