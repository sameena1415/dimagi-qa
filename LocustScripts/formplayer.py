from dataclasses import dataclass, field
from typing import List, Dict, Optional

def post(command, client, app_details, user_details, extra_json=None, name=None, validation=None):
    formplayer_host = "/formplayer"
    json = {
        "app_id": app_details.build_id,
        "domain": app_details.domain,
        "locale": "en",
        "restoreAs": user_details.login_as,
        "username": user_details.username,
    }
    if extra_json:
        json.update(extra_json)
    name = name or command

    if 'XSRF-TOKEN' not in client.cookies:
        response = client.get(f"{formplayer_host}/serverup")
        response.raise_for_status()

    xsrf_token = client.cookies['XSRF-TOKEN']
    headers = {'X-XSRF-TOKEN': xsrf_token}
    client.headers.update(headers)
    with client.post(f"{formplayer_host}/{command}/", json=json, name=name,
                            catch_response=True) as response:
        if validation:
            validate_response(response, validation)
        return response.json()

@dataclass
class ValidationCriteria:
    keys: Optional[List[str]] = None
    key_value_pairs: Optional[Dict[str, Optional[str]]] = field(default_factory=dict)
    length_check: Optional[Dict[str, int]] = field(default_factory=dict)

def validate_response(response, validation: ValidationCriteria):
    data = response.json()
    for checkKey in validation.keys:
        checkValue = validation.key_value_pairs.get(checkKey, None)
        checkLen = validation.length_check.get(checkKey, None)
        if "notification" in data and data["notification"]:
            if data["notification"]["type"] == "error":
                msg = "ERROR::-" + data["notification"]["message"]
                response.failure(msg)
                raise FormplayerResponseError("ERROR::-" + data["notification"]["message"])
        if "exception" in data:
            msg = "ERROR::exception error--" + data['exception']
            response.failure(msg) 
            raise FormplayerResponseError(msg)
        elif checkKey and checkKey not in data:
            msg = "error::" + checkKey + " not in data"
            response.failure(msg)
            raise FormplayerResponseError(msg)
        elif checkKey and checkLen:
            if len(data[checkKey]) != checkLen:
                msg = "ERROR::len(data['" + checkKey + "']) != " + checkLen
                response.failure(msg)
                raise FormplayerResponseError(msg)
        elif checkKey and checkValue:
            if data[checkKey] != checkValue:
                msg = "ERROR::data['" + checkKey + "'], " + data[checkKey] + " != " + checkValue
                response.failure(msg)
                raise FormplayerResponseError(msg)

class FormplayerResponseError(Exception):
    pass
