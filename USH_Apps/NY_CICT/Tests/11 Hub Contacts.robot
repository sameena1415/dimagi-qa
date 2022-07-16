*** Settings ***
Documentation     Workflow to test Patient Good Path
Suite Setup    Driver Launch
Library  SeleniumLibrary        timeout=300s
Resource    ../Contact Tracing (CT)/Menu/menu.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
Resource    ../Contact Tracing (CT)/Forms/hub contacts.robot

Suite Teardown  Close Browser

*** Test Cases ***

Hub_Contacts_1
    [Documentation]    Mark a Contact eligible for a Healthcare Hub
    Sleep   360s
    HQ Login
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Contact Fill up Healthcare section
    Open Hub Healthcare Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    Pending
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       In Progress
    Open Hub Healthcare Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    In Progress
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       Complete
    Open Hub Healthcare Contacts
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

Hub_Contacts_2
    [Documentation]    Mark a Case eligible for a Congregate Settings Hub
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Contacts Fill up Congregate section
    Open Hub Congregate Settings Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    Pending
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       In Progress
    Open Hub Congregate Settings Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    In Progress
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       Complete
    Open Hub Congregate Settings Contacts
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

Hub_Contacts_3
    [Documentation]    Mark a Contact eligible for Clusters Hub
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Contacts Fill up Cluster section
    Open Hub Clusters Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    Pending
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       In Progress
    Open Hub Clusters Contacts
    Search in the case list     ${contact_name}
    Verify Hub Status Contacts       ${contact_name}    In Progress
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update Hub Status Contacts       Complete
    Open Hub Clusters Contacts
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

Hub_Contacts_5
    [Documentation]    Mark a Contact eligible for a School Hub
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    ${school}       ${date}      ${end_date}=    Contacts Fill up School section
    Open Hub School Contacts
    Search in the case list     ${contact_name}
    Verify School Name and Date Contacts     ${contact_name}    ${school}    ${end_date}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Update School Hub Status Contacts       Complete
    Open Hub School Contacts
    Search in the case list     ${contact_name}
    Element Should Not Be Visible    ${contact_created}

Hub_Contacts_6
    [Documentation]    Enter information in Childcare/School/College Details section to appear in the School Hub
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts Unassigned & Open menu
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Enter Information in School College Details section Contacts
    Open Hub School Contacts
    Search in the case list     ${contact_name}
    Page Should Contain Element    ${contact_created}

