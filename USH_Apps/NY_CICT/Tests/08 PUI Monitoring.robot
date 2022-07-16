*** Settings ***
Documentation     Testing the workflow to deduplicate a suspected case (PUI) record against a confirmed case record with one attached lab results and one attached contact
Suite Setup    Driver Launch
Library  SeleniumLibrary        timeout=300s
Resource    ../Contact Tracing (CT)/Menu/menu.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Resource    ../Contact Tracing (CT)/Forms/change to pui status form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Suite Teardown  Close Browser

*** Test Cases ***

Pui_Monitoring_1
    [Documentation]    PUI with a positive test result
    Sleep   240s
    HQ Login
    Log in as ctsup_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Open Contacts menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Convert Contact to a Suspected Case (PUI) Form
    PUI form submission
    Log in as ci_user
    Sleep    60s
    Search Case in All Suspected Cases (PUIs) menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Case Investigation Form
    Add new follow up log       success
    Fill up PUI Category for Positive test
    Open All Suspected Cases (PUIs) menu
    Search in the case list    ${contact_name}
    Verify results received     ${contact_name}

Pui_Monitoring_2
    [Documentation]    PUI with a negative test result
    Log in as ctsup_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Open Contacts menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Convert Contact to a Suspected Case (PUI) Form
    PUI form submission
    Log in as ci_user
    Sleep    90s
    Search Case in All Suspected Cases (PUIs) menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Case Investigation Form
    Add new follow up log       success
    Fill up PUI Category for Negative test
    Open All Suspected Cases (PUIs) menu
    Search in the case list    ${contact_name}
    Verify results received     ${contact_name}
