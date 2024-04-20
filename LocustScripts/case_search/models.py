import random
from collections import defaultdict
from functools import cached_property
from typing import Self

import pydantic


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

