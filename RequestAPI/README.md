# Automated API Python Requests

## Setting up test environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

```

## Running Tests

- Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for
the environment you want to test.


- Run tests

```sh
## command to execute the scripts 
pytest -v 

## command to execute the scripts with 2 reruns and in parallel with limited traceback
pytest -v -n auto --dist=loadfile --reruns 2 --capture=tee-sys  --tb=short

## command to execute individual test module or test case
# Example: pytest -v -k <complete or partial test module name/complete or partial test case name> 
pytest -v -k test_01/test_case_1 

```
- Similarly, you could pass the following arguments:
  - `-n auto --dist=loadfile` - This will run the tests parallelly; it'll automatically choose the number of instances . The number of reruns is configurable.
  - `--reruns 1` - This will re-run the tests once in case of failures.The number of reruns is configurable too.
  - `--capture=tee-sys` - This disables all capturing and replaces sys.stdout/stderr with in-mem files
  - `--tb=short` - This enables shorter traceback format
