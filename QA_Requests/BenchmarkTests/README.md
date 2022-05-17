## Benchmark case export config page performance

QA Ticket: [QA-3939](https://dimagi-dev.atlassian.net/browse/QA-3939)

### Setting up and Running tests

- Setup Environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requires.txt

```

- Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for
the environment you want to test.

- Provide the start value of case properties and end value in `userInput -> test_data` sheet for `col_start` and `col_end`.

- Run tests

```sh
command to execute the scripts
pytest -v 
```
