## Automated Performance Scripts for USH NY CICT

Captures load time for various actions performed in NY CICT app. The apps, users and the number of reruns are configurable and can be configured in [**user_inputs.py**](https://github.com/dimagi/dimagi-qa/blob/kt/ny_sprint_perf/NYperformance/UserInputs/user_inputs.py).


### The script can be run in two ways: 

<img align="right" width="350" src="https://user-images.githubusercontent.com/67914792/168422283-846b01c2-b422-4995-b243-7c8af84937c7.PNG" alt="clone this repository" />

#### 1. Manual Trigger on Gitaction

To manually trigger the script,
  - Go to [NY Sprint Performance action](https://github.com/dimagi/dimagi-qa/actions/workflows/ny-app-perf.yml)
  - Run workflow
  - Use workflow from ```kt/ny_sprint_perf```
  - Run!


You should be able to find the zipped results in the **Artifacts** section, of the corresponding run (after it's complete). 

<img align="right" width="350" src="https://user-images.githubusercontent.com/67914792/168422399-e76b1dcd-fd01-4d6b-b5f3-812268fc6386.PNG" alt="clone this repository" />

If you want to receive emails for the result of the run, please reach out to the QA team.


#### 2. Run on Local Machine
After you've added the scripts to your system,

- Setup test environment

```sh
# create and activate a virtualenv using your preferred method. Example:
python -m venv venv
source venv/bin/activate

# install requirements
pip install -r requires.txt

```

- Copy `settings-sample.cfg` to `settings.cfg` and populate `settings.cfg` for the environment and credentails you want to test.

- Make the necessary changes in [**user_inputs.py**](https://github.com/dimagi/dimagi-qa/blob/kt/ny_sprint_perf/NYperformance/UserInputs/user_inputs.py) as per your requirement.

- Run tests

```sh
# command to execute the scripts with 1 rerun
pytest -v  
```
- A file with readings will be generated in the folder **CaptureReadings** after the scripts run sucessfully.

