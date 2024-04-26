# Installation and setup

You will need python 3.11+ to run these tests - 

pip install -r requirements.txt

A CommCareHQ web user who is a member of the test domain is required. This user's username and password should be specified as the environment variables LOCUST_USERNAME and LOCUST_PASSWORD.

Domain and application, both required, are specified in config.yaml.

# Configuring and running
Basic usage, for a single test user:

```shell
locust -f commcarehq-bed-track.py --headless -u 1 -r 1 --test-config project-config/co-carecoordination-perf/config.yaml
```

### Tags:

* home_screen
* search_for_beds_menu
* non_facet_search
* facet_search

Run a facet search test use:

```shell
# Non-facet search test:
--exclude-tags facet_search

# Facet search test
--exclude-tags non_facet_search
```

Note that `search_for_beds_menu` will also perform 1 non-facet search.

Leave off --headless to view results in the Locust web UI. See docs for options to set number of users, run time, etc.

## Running with a step load

```shell
locust -f commcarehq-bed-track.py,step_load.py
```

This will spawn users in batches of 50 with a 5 minute wait between each batch. The max users is 300 and the default
max runtime is 30 minutes.
