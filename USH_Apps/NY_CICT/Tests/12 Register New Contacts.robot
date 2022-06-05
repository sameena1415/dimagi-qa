*** Settings ***
Documentation     Workflow to test Register New Contacts
Suite Setup    HQ Login
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/register new contacts form.robot

Suite Teardown  Close Browser

*** Test Cases ***

Register New Contact 1
    [Documentation]    register a single contact with a phone number and the case's address
    Log in as ci_user
    Register New Case
    Fill up and Submit Case Investigation Form

    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}

    ${phone}    Generate Mobile Number
    Generate Random Contact Name
    ${name_random}    Get Variable Value    ${name_random}
    Register New Contacts to Case having address  1  ${name_random}   ${phone}

    Log in as ctsup_user
    Open All Contacts Unassigned & Open menu
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list     ${contact_name}
    Element Should Be Visible    ${contact_created}
    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Element Should Be Visible    ${contact_created}

Register New Contact 2
    [Documentation]    contact number incrementer (no MPI ID on index case)






