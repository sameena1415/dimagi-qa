# Installation and setup
pip install -r requirements.txt

A CommCareHQ web user who is a member of the test domain is required. This user's username and password should be specified as the environment variables LOCUST_USERNAME and LOCUST_PASSWORD.

Domain and application, both required, are specified in config.yaml. Username to login as may also be included.

# Configuring and running
Copy user_credentials_sample.json to user_credentials.json and populate user_credentials.json for the user  you want to test.

Basic usage, for a single test user:

env LOCUST_USERNAME=$LOCUST_USERNAME env LOCUST_PASSWORD=$LOCUST_PASSWORD locust -f commcarehq-bed-track.py --headless -u 1 -r 1

Leave off --headless to view results in the Locust web UI. See docs for options to set number of users, run time, etc.
