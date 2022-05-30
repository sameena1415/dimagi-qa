*** Settings ***
Documentation     Testing the workflow to close a patient record and record the case's final disposition.
Library  SeleniumLibrary
Suite Setup    HQ Login
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/close the patient record form.robot
Resource    ../Case Investigation (CI)/Forms/close the patient record form.robot
Suite Teardown  Close Browser

*** Test Cases ***

Close_Case_and_Contact_1
    [Documentation]    Patient record does not close, then does close (close record form)
    Log in as ci_user
    Register New Case
    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Close Patient record - No
    Open All Cases
    Search in the case list     ${case_name}
    Verify Open Status      ${case_name}
    Select Created Case    ${case_created}
    Close Patient record - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Verify Close Status     ${case_name}


Close_Case_and_Contact_2
    [Documentation]    Patient record does not close, then does close (case investigation form)
    Open App Home Screen
    Log in as ci_user
    Register New Case
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Activity for case complete - No
    Open All Cases
    Search in the case list     ${case_name}
    Verify Open Status      ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Activity for case complete - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Verify Close Status     ${case_name}
