*** Settings ***
Documentation     Testing the workflow to reopen a patient record that was
...               previously closed to resume interview/monitoring activities.
Library  SeleniumLibrary        timeout=200s
Suite Setup    Driver Launch
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/close the patient record form.robot
Resource    ../Contact Tracing (CT)/Forms/close the contact record form.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Suite Teardown  Close Browser

*** Test Cases ***

Reopen_Case_and_Contact_1
    [Documentation]    Closed case does not reopen, then reopens (closed patient record form)
    Sleep   200s
    HQ Login
    Log in as ci_user
    Register New Case
    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Close Patient record - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Verify Close Status      ${case_name}
    Select Created Case    ${case_created}
    Reopen Patient record - No
    Open All Cases
    Search in the case list     ${case_name}
    Verify Close Status     ${case_name}
    Select Created Case    ${case_created}
    Reopen Patient record - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Verify Open Status     ${case_name}


Reopen_Case_and_Contact_2
    [Documentation]    Closed case reopens (case investigation form)
    Open App Home Screen
    Log in as ci_user
    Register New Case
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Activity for case complete - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Verify Close Status      ${case_name}
    Select Created Case    ${case_created}
    Open Form    ${Case Investigation Form}
    Activity for case complete - No
    Open All Cases
    Search in the case list     ${case_name}
    Verify Open Status     ${case_name}
    Verify Final Disposition Blank     ${case_name}



Reopen_Case_and_Contact_3
    [Documentation]    Closed contact does not reopen, then reopens (close contact record form)
    Open App Home Screen
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts
    Search in the case list     ${contact_name}
    Select Created Case    ${contact_created}
    Close Contact record - Yes
    Open All Contacts
    Search in the case list     ${contact_name}
    Select Created Case    ${contact_created}
    Reopen Contact record - No
    Open All Contacts
    Search in the case list     ${contact_name}
    Verify Contact Close Status     ${contact_name}
    Select Created Case    ${contact_created}
    Reopen Contact record - Yes
    Open All Contacts
    Search in the case list     ${contact_name}
    Verify Contact Open Status     ${contact_name}
