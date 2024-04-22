import formplayer
from locust.exception import StopUser
import pydantic

class UserDetails(pydantic.BaseModel):
    username: str
    password: str
    login_as: str | None = None

class AppDetails(pydantic.BaseModel):
    domain: str
    app_id: str
    build_id: str

class HQUser():

    def __init__(self, user_details):
        self.user_details = user_details

    def login(self, domain, host, client):
        login_url = f"/a/{domain}/login/"
        client.get(login_url)  # get CSRF token
        response = client.post(
            login_url,
            {
                "auth-username": self.user_details.username,
                "auth-password": self.user_details.password,
                "cloud_care_login_view-current_step": ['auth'],  # fake out two_factor ManagementForm
            },
            headers={
                "X-CSRFToken": client.cookies.get('csrftoken'),
                "REFERER": f"{host}{login_url}",  # csrf requires this
            },
        )
        if not response.status_code == 200:
            raise StopUser(f"Login failed for user {self.user_details.username}: {response.status_code}")
        if 'Sign In' in response.text:
            raise StopUser(f"Login failed for user {self.user_details.username}: Sign In failed")

    def post_formplayer(self, command, client, app_details, extra_json=None, name=None, validation=None):
        return formplayer.post(command, client, app_details, self.user_details, extra_json, name, validation)
