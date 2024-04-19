import random
from collections import defaultdict
from functools import cached_property
from typing import Self

import pydantic


class Query(pydantic.BaseModel):
    name: str
    case_types: list[str]
    query_params: dict[str, str | list[str]]
    value_set_key: str | None = None

    def get_query_params_for_request(self, value_set=None):
        def _format_value(value):
            if not value_set:
                return value

            if isinstance(value, list):
                return [v.format(**value_set) for v in value]
            return value.format(**value_set)

        return {
            "case_type": self.case_types,
            **{key: _format_value(value) for key, value in self.query_params.items()}
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
        if not query.value_set_key:
            name = query.name
            data = query.get_query_params_for_request()
        else:
            value_set = random.choice(self.value_sets_by_key[query.value_set_key])
            name = f"{query.name}:{value_set.name}"
            data = query.get_query_params_for_request(value_set.values)
        return name, data


class UserDetails(pydantic.BaseModel):
    username: str
    password: str
    login_as: str | None = None
