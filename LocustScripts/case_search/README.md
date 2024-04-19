# Case Search Locust Scripts

This load test script performs continuous case search request per user with a constant wait time of 1s between requests.

The query data for each request is selected by randomizing the data in the query YAML configuration file.

Run from `LocustScripts` directory:

```shell
locust -f case_search/main.py --headless -u 1 -r 1 \
  --host http://localhost:8000 \
  --domain skelly-1 \
  --app-id b62974969e57051ad70160a798ed79e8  \
  --queries case_search/queries_example.yml \
  --user-details case_search/user_credentials_example.json
```

## Options

- `--host` - URL of the application
- `--domain` - Domain of the application
- `--app-id` - Application ID
- `--queries` - Path to the queries file
- `--user-details` - Path to the user credentials file

## Request generation

1. Select a random query.
2. Select a random value set for the query using the `query.value_set_key` field and match it against
   the `value_set.keys` field.
3. Fill in the query parameters with values from the value set.
4. Send the request.

## Queries file

This file contains request data that will be used by the locust scripts to perform case search requests.

See `queries_example.yml` for an example.

### Queries ("queries" key)
A list of parameterized queries. Each request will select one query at random and fill in the
parameters with values from a random value set.

Query fields:
- `name`: The name of the query (used for logging)
- `case_types`: A list of case types to pass via the 'case_type' query parameter (required)
- `value_set_key`: The value set type key to use to select a value set for the query at runtime (optional)
- `query_params`: A dictionary of query parameters to pass in the request. They query values may contain
  variable references using the '{name}' syntax which will be filled by values from the value set. The values
  of the dictionary may be a string or a list.

```yaml
queries:
  - name: test
    case_types: [client]
    value_set_key: client
    query_params:
      case_name: {case_name}
      _xpath_query:
        - first_name='{first_name}' and last_name='{last_name}'
        - subcase-exists('parent', @case_type = 'alias' and first_name='{first_name}' and last_name='{last_name}')
```

### Value Sets ("value_sets" key)
A list of parameter values which are used to format the queries.

Value set fields:
- `name`: The name of the value set (used for logging)
- `keys`: A list of keys which indicate which query sets this value set may be used for. A query set with
  a key matching `query.value_set_key` will be selected at runtime.
- `values`: A dictionary of values which are used to format the query at runtime. The keys in this dictionary are used
  to replace the variable references in the query parameters.

```yaml
value_sets:
  - name: bob
    keys: [client, alias]  # can be used for client or alias queries
    values:
      first_name: bob
      last_name: smith
      alias: bobby
```
