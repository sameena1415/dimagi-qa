*** Settings ***
Documentation     Workflow to test Patient and Contact Good Path
Suite Setup    Driver Launch
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/assign or reassign form.robot

Resource    ../Contact Tracing (CT)/Menu/menu.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
Resource    ../Contact Tracing (CT)/Forms/assign or reaasign contact.robot
Suite Teardown  Close Browser

*** Test Cases ***

Patient_Good_1
    [Documentation]    Register New Case
    HQ Login
    Log in as ci_user
    Register New Case
    Open All Cases: Incomplete Demographic Information Menu 
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}   
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}   
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Set Global Variable    ${case_name}
    Set Global Variable    ${case_created}
    

Patient_Good_2
    [Documentation]    All Cases: Incomplete Demographic Information
    Open All Cases: Incomplete Demographic Information Menu
    Sleep    20s
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Case Search    ${case_name}
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Fill up and Submit Case Investigation Form
    ## Landed on Incomplete Demographic page
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Open All Cases: Unassigned & Open
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}


Patient_Good_3
    [Documentation]    All Cases: Assigned & Open
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Permanently Assign to Self
    ## Lands on Unassigned and open
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}
    Open All Cases: Assigned & Open
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}


Patient_Good_4
    [Documentation]    All Cases: Unassigned & Open
    Open All Cases: Assigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Unassign from Self
    ## Lands on Assigned and open
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}
    Open All Cases: Unassigned & Open
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec  Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}

Patient_Good_5
    [Documentation]    My Cases
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Permanently Assign to Self
    ## Lands on Unassigned and open
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}
    Open My Cases
    Search in the case list     ${case_name}
    Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}


Patient_Good_6
    [Documentation]    All Cases: Unable to Reach
    Open My Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Unable to reach
    All Cases: Unable to Reach
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}

Patient_Good_7
    [Documentation]    All Closed Cases
    Open All Cases
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list      ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Activity for case complete
    Open All Closed Cases
    Search in the case list     ${case_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${case_created}
    Open All Open Cases
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}


Contact_Good_1
    [Documentation]    All Contacts: Incomplete Contact Information
    Log in as ct_user
    Log    ${case_name}+"and"+${case_created}
    Register contact without phone number    ${case_name}    ${case_created}
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Contacts: Incomplete Contact Information
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

Contact_Good_2
    [Documentation]    All Contacts: Unable to Reach

    Open All Contacts: Incomplete Contact Information
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Case Search    ${contact_name}
    Search in the case list      ${contact_name}
    Element Should Be Visible    ${contact_created}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Unable to reach (CM)

    Open All Contacts: Incomplete Contact Information
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open All Contacts: Unable to Reach
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}


Contact_Good_3
    [Documentation]    All Contacts: Unassigned & Open

    Open All Contacts: Unable to Reach
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Reached and Agreed to Call (CM)

    Open All Contacts: Unable to Reach
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

Contact_Good_4
    [Documentation]    All Contacts: Assigned & Open

    Open All Contacts Unassigned & Open menu
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Permanently Assign to Self (CM)

    ## Lands on Unassigned and open
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open All Contacts: Assigned & Open
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Element Should Be Visible    ${contact_created}

Contact_Good_5
    [Documentation]    All Contacts: Require Follow-up

    Open All Contacts: Assigned & Open
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Requires Follow-up (CM)

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open All Contacts
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}


Contact_Good_6
    [Documentation]    All Contacts: SMS

    Open All Contacts: Require Follow-Up
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Receive SMS (CM)

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Contacts
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}



Contact_Good_7
    [Documentation]    All Contacts

    Open All Contacts
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Partial Interview Complete (CM)

    ## PAUSE UNTIL THE NEXT DAY!! [Check if required and if so how?]
    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

Contact_Good_8
    [Documentation]    My Contacts: Require Follow-Up

    Open My Contacts: Require Follow-Up
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Unassign from Self (CM)

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}

Contact_Good_9
    [Documentation]   All Closed Contacts

    Open All Contacts
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Interview Complete (CM)

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

    Open All Closed Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  5 sec   Element Should Be Visible    ${contact_created}