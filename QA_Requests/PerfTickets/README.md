## Performance Tickets

QA Tickets: 
- [Performance testing Subcase Querying](https://dimagi-dev.atlassian.net/browse/QA-4273)
- [Performance testing CLE](https://dimagi-dev.atlassian.net/browse/QA-4296)

### Setting up and Running tests

- Setup Environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requires.txt

```

- Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` and the credentials you want to run it with.

- Run tests

```sh
command to execute the scripts
pytest -v /path/to/test_capture_cle.py
python  /path/to/test_generate_upload_subquery_data.py
```
