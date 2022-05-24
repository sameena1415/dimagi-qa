## New York CICT Regression using Robot Framework

Script for NY USH App Regression workflows. 

## Execution of Scripts

##### Install Robot Framework and SeleniumLibrary along with its dependencies using pip package manager. 
```
pip install -r requirements.txt
```
##### Copy file  ```/Utilities/user_input-sample.robot``` and save it as ```user_input.robot```. Add the required credentials in to the file.


##### The test cases are located in the Tests directory. They can be executed using the robot command:
```
webdrivermanager chrome
robot Tests
```