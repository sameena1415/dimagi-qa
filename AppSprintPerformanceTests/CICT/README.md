## Automated Performance Scripts for USH CICT Apps

Captures load time for various actions performed in CICT apps.

The apps, users and the number of reruns are configurable and can be configured in UserInputs file of the corresponding site


### The script can be run in two ways: 

<img align="right" width="350" src="https://user-images.githubusercontent.com/67914792/187366529-c60517a5-186f-405c-8c9c-a1d27dd4893c.png" alt="clone this repository" />



#### 1. Manual Trigger on Gitaction

To manually trigger the script,
  - Go to [Sprint Performance action](https://github.com/dimagi/dimagi-qa/actions/workflows/sprint-app-perf.yml)
  - Run workflow
  - Use workflow from ```master```
  - Select the site
    - CO - Colorado
    - NY - New York
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
pip install -r AppSprintPerformanceTests/CICT/requires.txt

```

- Run tests

```sh
# command to execute the scripts with 1 rerun where site name can be passed against argument --appsite. 

# If want to run for NY scripts , use the following:
 pytest -v --rootdir= AppSprintPerformanceTests/CICT/CaptureReadings/NY_test_readings.py --repeat-scope=function --appsite=NY
 
 #If want to run for CO scripts , use the following:
 pytest -v --rootdir= AppSprintPerformanceTests/CICT/CaptureReadings/CO_test_readings.py --repeat-scope=function --appsite=CO
 
```
- A file with readings will be generated in the folder **common_utilities/OutputFiles** after the scripts run sucessfully.

