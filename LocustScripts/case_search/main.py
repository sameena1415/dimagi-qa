import logging
import random
from collections import defaultdict
from functools import cached_property
from pathlib import Path
from typing import Self

import pydantic
from locust import HttpUser, constant, events, task
from locust.exception import InterruptTaskSet, StopUser

from common.utils import RandomItems, load_json_data, load_yaml_data


def file_path(value):
    path = Path(value)
    if not (path.exists() and path.is_file()):
        raise ValueError(f"File not found: {path}")
    return path


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--domain", help="CommCare domain", required=True, env_var="COMMCARE_DOMAIN")
    parser.add_argument("--app-id", help="CommCare app id", required=True, env_var="COMMCARE_APP_ID")
    parser.add_argument("--queries", help="Path to queries YAML file", required=True)
    parser.add_argument("--user-details", help="Path to user details file", required=True)


class Query(pydantic.BaseModel):
    name: str
    case_types: list[str]
    value_set_key: str
    query_params: dict[str, str]

    def get_query_params_for_request(self, value_set):
        return {
            "case_type": self.case_types,
            **{key: value.format(**value_set) for key, value in self.query_params.items()}
        }


class ValueSet(pydantic.BaseModel):
    name: str
    keys: list[str]
    values: dict[str, str | int | float | bool]


class QueryData(pydantic.BaseModel):
    queries: list[Query]
    value_sets: list[ValueSet]

    @cached_property
    def value_sets_by_key(self):
        by_key = defaultdict(list)
        for value_set in self.value_sets:
            for key in value_set.keys:
                by_key[key].append(value_set)
        return by_key

    @pydantic.model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        for query in self.queries:
            if query.value_set_key not in self.value_sets_by_key:
                raise ValueError(f"Value set not found: {query.value_set_key}")
        return self

    def get_random_query(self):
        query = random.choice(self.queries)
        value_set = random.choice(self.value_sets_by_key[query.value_set_key])
        name = f"{query.name}:{value_set.name}"
        return name, query.get_query_params_for_request(value_set.values)


class UserDetails(pydantic.BaseModel):
    username: str
    password: str
    login_as: str | None = None


QUERY_DATA = []
USERS = RandomItems()


def get_random_query():
    return QUERY_DATA[-1].get_random_query()


@events.init.add_listener
def _(environment, **kw):
    try:
        queries = file_path(environment.parsed_options.queries)
        QUERY_DATA.append(load_yaml_data(queries, QueryData))
        logging.info("Loaded %s queries and %s value sets", len(QUERY_DATA[0].queries), len(QUERY_DATA[0].value_sets))
    except Exception as e:
        logging.error("Error loading queries: %s", e)
        raise InterruptTaskSet from e

    try:
        user_path = file_path(environment.parsed_options.user_details)
        user_data = load_json_data(user_path)["user"]
        USERS.set([UserDetails(**user) for user in user_data])
        logging.info("Loaded %s users", len(USERS.items))
    except Exception as e:
        logging.error("Error loading users: %s", e)
        raise InterruptTaskSet from e


class CaseSearchUser(HttpUser):
    wait_time = constant(1)

    def on_start(self):
        self.user_details = USERS.get()
        self.login()

    def login(self):
        login_url = f"/a/{self.environment.parsed_options.domain}/login/"
        self.client.get(login_url)  # get CSRF token
        response = self.client.post(
            login_url,
            {
                "auth-username": self.user_details.username,
                "auth-password": self.user_details.password,
                "cloud_care_login_view-current_step": ['auth'],  # fake out two_factor ManagementForm
            },
            headers={
                "X-CSRFToken": self.client.cookies.get('csrftoken'),
                "REFERER": f"{self.environment.parsed_options.host}{login_url}",  # csrf requires this
            },
        )
        if not response.status_code == 200:
            raise StopUser(f"Login failed for user {self.user_details.username}: {response.status_code}")
        if 'Sign In' in response.text:
            raise StopUser(f"Login failed for user {self.user_details.username}: Sign In failed")

    @task
    def search_case(self):
        url = f"/a/{self.environment.parsed_options.domain}/phone/search/{self.environment.parsed_options.app_id}/"
        name, query = get_random_query()
        self.client.post(
            url,
            data=query,
            name=f"Search cases: {name}"
        )
