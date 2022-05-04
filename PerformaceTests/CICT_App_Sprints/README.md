# Automated Performance Scripts for USH NY CICT

Setup test environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requires.txt

```

Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for
the environment you want to test.


Run tests

```sh
# command to execute the scripts with 1 rerun
pytest -v  
```
A file with readings will be generated in the folder `CaptureReadings` after the scripts run sucessfully.
