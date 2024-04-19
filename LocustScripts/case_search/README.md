# Case Search Locust Scripts

Run from `LocustScripts` directory:

```shell
locust -f case_search/main.py --headless -u 1 -r 1 \
  --host http://localhost:8000 \
  --domain skelly-1 \
  --app-id b62974969e57051ad70160a798ed79e8  \
  --queries case_search/queries_example.yml \
  --user-details case_search/user_credentials_example.json
```
