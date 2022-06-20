*** Settings ***
Library    Collections
Documentation     Testing workflow to create contacts that have no confirmed exposures or index patient cases in the system.
Suite Setup    Driver Launch
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/register new contacts form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
Suite Teardown  Close Browser

*** Test Cases ***


Register New Contact No Index 1
    [Documentation]   register a single contact with a phone number
    Sleep   440s
    HQ Login
    Log in as ci_user
    ${contact_names}     Generate Contact New Names     1
    ${phone}    Generate Mobile Number
    Register New Contacts for Case having address and phone number    1    generated_names=${contact_names}    phone=${phone}    contact_type=international_travel  without_index=yes

    Log in as ct_user
    Sleep    60s
    Open All Contacts Unassigned & Open menu
    ${contact_created}  Search the contact created  ${contact_names}
    Element Should Be Visible    ${contact_created}


Register New Contact No Index 2
    [Documentation]    register multiple contacts with phone numbers
    Log in as ci_user
    ${contact_names}     Generate Contact New Names     2
    ${phone}    Generate Mobile Number
    Register New Contacts for Case having address and phone number    2    generated_names=${contact_names}    phone=${phone}    contact_type=visitor_traveling   without_index=yes

    Log in as ct_user
    Open All Contacts
    Search and Select the contact created  ${contact_names}
    Check Registered Contact Details on Contact Monitoring      check=without_index_traveler
    Open All Contacts
    Search and Select the contact created  ${contact_names}  1
    Check Registered Contact Details on Contact Monitoring     check=without_index_traveler


Register New Contact No Index 3
    [Documentation]    register a single contact without a phone number
    Log in as ct_user
    ${contact_names}     Generate Contact New Names     1
    ${contact_deatils_3}    Register New Contacts for Case having address and phone number    1    generated_names=${contact_names}     phone=${EMPTY}    contact_type=ooj_case    without_index=yes

    Open All Contacts: Incomplete Contact Information
    Search and Select the contact created  ${contact_names}
    Check Registered Contact Details on Contact Monitoring  ${contact_deatils_3}


Register New Contact No Index 4
    [Documentation]    all contacts: require followup
    Log in as ct_user
    ${contact_names}     Generate Contact New Names     1
    ${phone}    Generate Mobile Number
    Register New Contacts for Case having address and phone number    1    generated_names=${contact_names}    phone=${phone}    contact_type=ooj_case   symptomatic=yes   without_index=yes

    Open All Contacts: Require Follow-Up
    Sleep    60s
    ${contact_created}  Search the contact created  ${contact_names}
    Element Should Be Visible    ${contact_created}


