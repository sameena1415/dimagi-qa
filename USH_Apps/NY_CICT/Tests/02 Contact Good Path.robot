*** Settings ***
Documentation     Workflow to test Patient and Contact Good Path
Suite Setup    Driver Launch
Library  SeleniumLibrary        timeout=200s
Library  DependencyLibrary
Resource    ../Contact Tracing (CT)/Menu/menu.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
Resource    ../Contact Tracing (CT)/Forms/assign or reaasign contact.robot
Suite Teardown  Close Browser

*** Test Cases ***


Contact_Good_1
    [Documentation]    All Contacts: Incomplete Contact Information
    Sleep   40s
    HQ Login
    Log in as ci_user
    Register New Case
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Log in as ct_user
    Log    ${case_name}+"and"+${case_created}
    Register contact without phone number    ${case_name}    ${case_created}
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Contacts: Incomplete Contact Information
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

Contact_Good_2
    [Documentation]    All Contacts: Unable to Reach
    Depends on test     Contact_Good_1

    Open All Contacts: Incomplete Contact Information
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Case Search    ${contact_name}
    Search in the case list      ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}
    Select Created Case    ${contact_created}
    Open Form    ${contact_monitoring_form}
    Unable to reach (CM)

    Open All Contacts: Incomplete Contact Information
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open All Contacts: Unable to Reach
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}


Contact_Good_3
    [Documentation]    All Contacts: Unassigned & Open
    Depends on test     Contact_Good_2

    Open All Contacts: Unable to Reach
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Form    ${contact_monitoring_form}
    Reached and Agreed to Call (CM)

    Open All Contacts: Unable to Reach
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Contacts Unassigned & Open menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

Contact_Good_4
    [Documentation]    All Contacts: Assigned & Open
    Depends on test     Contact_Good_3

    Open All Contacts Unassigned & Open menu
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Permanently Assign to Self (CM)

    ## Lands on Unassigned and open
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open All Contacts: Assigned & Open
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

Contact_Good_5
    [Documentation]    All Contacts: Require Follow-up
    Depends on test     Contact_Good_4

    Open All Contacts: Assigned & Open
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Form    ${contact_monitoring_form}
    Requires Follow-up (CM)

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open All Contacts
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}


Contact_Good_6
    [Documentation]    All Contacts: SMS
    Depends on test     Contact_Good_5

    Open All Contacts: Require Follow-Up
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Form    ${contact_monitoring_form}
    Receive SMS (CM)

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Contacts
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}



Contact_Good_7
    [Documentation]    All Contacts
    Depends on test     Contact_Good_6

    Open All Contacts
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Form    ${contact_monitoring_form}
    Partial Interview Complete (CM)

    ## PAUSE UNTIL THE NEXT DAY!! [Check if required and if so how?]
    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

Contact_Good_8
    [Documentation]    My Contacts: Require Follow-Up
    Depends on test     Contact_Good_7

    Open My Contacts: Require Follow-Up
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Unassign from Self (CM)

    Open My Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Contacts: Require Follow-Up
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}

Contact_Good_9
    [Documentation]   All Closed Contacts
    Depends on test     Contact_Good_8

    Open All Contacts
    ${contact_name}    Get Contact Name
    ${contact_created}   Set Contact Name
    Search in the case list      ${contact_name}
    Select Created Case    ${contact_created}
    Open Form       ${contact_monitoring_form}
    Interview Complete (CM)

    Open All Open Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Not Be Visible    ${contact_created}

    Open All Closed Contacts menu
    Search in the case list     ${contact_name}
    Wait Until Keyword Succeeds  2 min  20 sec      Element Should Be Visible    ${contact_created}