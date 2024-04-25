import logging

import formplayer
from locust.exception import StopUser
import pydantic


class UserDetails(pydantic.BaseModel):
    username: str
    password: str
    login_as: str | None = None

    def __str__(self):
        if self.login_as:
            return f"{self.username} as {self.login_as}"
        return self.username


class AppDetails(pydantic.BaseModel):
    domain: str
    app_id: str
    build_id: str

    @property
    def id(self):
        return self.build_id or self.app_id


class HQUser:

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
        logging.info("User logged in: " + self.user_details.username)

    def navigate_start(self, user, expected_title=None):
        validation = None
        if expected_title:
            validation = formplayer.ValidationCriteria(key_value_pairs={"title": expected_title})
        return self.post_formplayer(
            "navigate_menu_start",
            user,
            name="Home Screen",
            validation=validation
        )

    def navigate(self, name, user, data, expected_title=None):
        validation = None
        if expected_title:
            validation = formplayer.ValidationCriteria(key_value_pairs={"title": expected_title})
        return self.post_formplayer(
            "navigate_menu", user, data, name=name, validation=validation
        )

    def answer(self, name, user, data):
        return self.post_formplayer("answer", user, data, name=name)

    def submit_all(self, name, user, data, expected_response_message=None):
        validation = None
        if expected_response_message:
            validation = formplayer.ValidationCriteria(key_value_pairs={
                "submitResponseMessage": expected_response_message
            })
        return self.post_formplayer(
            "submit-all", user, data, name=name, validation=validation
        )

    def post_formplayer(self, command, user, extra_json=None, name=None, validation=None):
        logging.info(f"User: {self.user_details}; Request: {command}")
        try:
            return formplayer.post(
                command, user.client, user.app_details, self.user_details, extra_json, name, validation
            )
        except Exception as e:
            logging.error("user: %s; request: %s; exception: %s", self.user_details, command, str(e))
