# QA Automation scripts

Setup test environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

```

Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for
the environment you want to test.


Run tests

```sh
command to execute the scripts with 2 reruns
pytest -v --reruns 2 --capture=tee-sys --html=report.html --self-contained-html  --tb=short

command to execute the scripts with 2 reruns and in parallel
pytest -v -n auto --dist=loadfile --reruns 2 --capture=tee-sys --html=report.html --self-contained-html  --tb=short

command to execute individual test module or test case
pytest -v -k <complete or partial test module name/complete or partial test case name> --capture=tee-sys --html=report.html --self-contained-html  --tb=short
Example: pytest -v -k test_01/test_case_1 --capture=tee-sys --html=report.html --self-contained-html  --tb=short
```
