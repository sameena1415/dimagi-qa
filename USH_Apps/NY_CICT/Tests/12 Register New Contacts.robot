*** Settings ***
Library    Collections
Documentation     Workflow to test Register New Contacts
Suite Setup    HQ Login
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/register new contacts form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
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
    ${contact_name}     Generate Contact New Names     1
    ${contact_details_1}    Register New Contacts for Case having address and phone number  1  generated_names=${contact_name}    phone=${phone}
    Set Global Variable    ${contact_details_1}

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
    Log in as ci_user
    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Check Already Registered Contacts   1    ${contact_details_1}

    ${phone}    Generate Mobile Number
    ${contact_name}     Generate Contact New Names     1
    ${contact_details_2}      Register New Contacts for Case having address and phone number  1  generated_names=${contact_name}    phone=${phone}    existing_count=1
    @{new_contact_details}=      Create List
    FOR  ${first_list}    ${second_list}    IN ZIP     ${contact_details_1}     ${contact_details_2}
         ${final}=  Combine Lists    ${first_list}    ${second_list}
         Collections.Append To List      ${new_contact_details}    ${final}
    END
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Check Already Registered Contacts   2    ${new_contact_details}

Register New Contact 3
    [Documentation]    contact number incrementer (index case has MPI ID)
    Log in as ci_user
    ${mpi_random}    Generate Mobile Number
    Set Global Variable    ${mpi_random}
    Register New Case   ${null}    ${mpi_random}
    Fill up and Submit Case Investigation Form

    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}

    ${phone}    Generate Mobile Number
    ${contact_names}     Generate Contact New Names     2
    ${contact_details_mp}  Register New Contacts for Case having address and phone number   2  generated_names=${contact_names}    phone=${phone}   mpi_id=${mpi_random}

    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Check Already Registered Contacts   2    ${contact_details_mp}

Register New Contact 4
    [Documentation]    register a single contact without a phone number
    Log in as ct_user
    Open Register New Contacts Menu
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Case Search     ${case_name}
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    ${contact_names}     Generate Contact New Names     1
    ${contact_details_4}   Register New Contacts for Case having address and phone number   1  generated_names=${contact_names}   phone=${EMPTY}   existing_count= 2    mpi_id=${mpi_random}

    Open All Contacts: Incomplete Contact Information
    Search and Select the contact created      ${contact_names}
    Check Registered Contact Details on Contact Monitoring    ${contact_details_4}


Register New Contact 5
    [Documentation]    register a single contact with a new complete address
    Log in as ct_user
    Open Register New Contacts Menu
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Case Search     ${case_name}
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    ${contact_names}     Generate Contact New Names     1
    ${contact_details_5}   Register New Contacts for Case having address and phone number   1  generated_names=${contact_names}   phone=${EMPTY}    existing_count=3     address_reset=yes  mpi_id=${mpi_random}

    #Open All Contacts Unassigned & Open menu
    Open All Contacts
    Search and Select the contact created      ${contact_names}
    Open Contact Monitoring Form
    Verify Address  address=present


Register New Contact 6
    [Documentation]    register a single contact without an address
    Log in as ct_user
    Open Register New Contacts Menu
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Case Search     ${case_name}
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    ${contact_names}     Generate Contact New Names     1
    ${contact_details_5}   Register New Contacts for Case having address and phone number   1  generated_names=${contact_names}   phone=${EMPTY}    existing_count=4     address_reset=blank    mpi_id=${mpi_random}

    #Open All Contacts Unassigned & Open menu
    Open All Contacts
    Search and Select the contact created      ${contact_names}
    Open Contact Monitoring Form
    Verify Address

Register New Contact 7
    [Documentation]    all contacts: require followup
    Log in as ct_user
    Open Register New Contacts Menu
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Case Search     ${case_name}
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    ${contact_names}     Generate Contact New Names     1
    ${contact_details_5}   Register New Contacts for Case having address and phone number   1  generated_names=${contact_names}   phone=${EMPTY}    existing_count=5    symptomatic=yes     mpi_id=${mpi_random}

    Open All Contacts: Require Follow-Up
    ${contact_created}  Search and Select the contact created      ${contact_names}
    Element Should Be Visible    ${contact_created}

