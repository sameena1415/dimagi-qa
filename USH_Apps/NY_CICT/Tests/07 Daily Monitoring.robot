*** Settings ***
Documentation     Workflow to test Patient Good Path
Suite Setup    HQ Login
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/assign or reassign form.robot
#Suite Teardown  Close Browser

*** Test Cases ***

Daily_Monitoring_1
    [Documentation]    Daily monitoring not selected, then selected
    Log in as ci_user
    Register New Case
    ${case_interview}=  Set variable    Yes
    ${daily_monitoring}=    Set variable    No
    ${activity_complete}=   Set variable    No
    Complete full interview     ${case_interview}   ${daily_monitoring}     ${activity_complete}
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Open All Open Cases
    Search in the case list     ${case_name}
    Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Daily Monitoring - Yes
#    Open All Open Cases
#    Search in the case list     ${case_name}
#    Select Created Case    ${case_created}
#    Verify Daily Monitoring Status    ${case_name}      Yes
#    Verify Daily Monitoring Section
