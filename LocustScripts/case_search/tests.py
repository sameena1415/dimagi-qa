import pytest

from case_search.models import Query, QueryData, ValueSet


@pytest.mark.parametrize("query_data", [
    pytest.param(
        {"name": "query1", "case_types": ["case1"], "query_params": {"param1": ["value1"]}, "value_set_keys": "key1"},
        id="value_set_keys to list",
    ),
    pytest.param(
        {"name": "query1", "case_types": ["case1"], "query_params": {"param1": "value1"}, "value_set_keys": ["key1"]},
        id="param values to list",
    ),
])
def test_query_model_values_to_list(query_data):
    query = Query(**query_data)
    assert query == Query(
        name="query1",
        case_types=["case1"],
        query_params={"param1": ["value1"]},
        value_set_keys=["key1"],
    )


def test_query_model_values_none():
    query = Query(name="query1", case_types=["case1"], query_params={})
    assert query == Query(
        name="query1",
        case_types=["case1"],
        query_params={},
        value_set_keys=[],
    )


def test_get_query_params_for_request():
    query = Query(name="query1", case_types=["case1"], query_params={
        "param1": ["{value1}"],
        "param2": ["{value1}={value2}", "{value2}"],
    })

    assert query.get_query_params_for_request({"value1": "value1", "value2": "value2"}) == {
        "case_type": ["case1"],
        "param1": ["value1"],
        "param2": ["value1=value2", "value2"],
    }


@pytest.mark.parametrize(("query", "value_sets", "expected_name", "expected_data"), [
    pytest.param(
        Query(name="query1", case_types=["case1"], query_params={"param1": ["value1"]}),
        [],
        "query1",
        {"case_type": ["case1"], "param1": ["value1"]},
        id="no_value_set",
    ),
    pytest.param(
        Query(name="query1", case_types=["case1"], query_params={"param1": ["{value_key1}"]}, value_set_keys=["key1"]),
        [ValueSet(name="value_set1", keys=["key1"], values={"value_key1": "value1"})],
        "query1:value_set1",
        {"case_type": ["case1"], "param1": ["value1"]},
        id="single_value_set",
    ),
    pytest.param(
        Query(
            name="query3",
            case_types=["case2"],
            query_params={"param2": ["{value_key1}", "{value_key2}"]},
            value_set_keys=["key1", "key2"],
        ),
        [
            ValueSet(name="value_set1", keys=["key1"], values={"value_key1": "value1"}),
            ValueSet(name="value_set2", keys=["key2"], values={"value_key2": "value2"}),
        ],
        "query3:value_set1:value_set2",
        {"case_type": ["case2"], "param2": ["value1", "value2"]},
        id="multiple_value_sets",
    ),
])
def test_get_query_name_and_data(query, value_sets, expected_name, expected_data):
    data = QueryData(queries=[query], value_sets=value_sets)
    name, request_data = data._get_query_name_and_data(query)
    assert name == expected_name
    assert request_data == expected_data
