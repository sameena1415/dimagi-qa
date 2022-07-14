*** Settings ***
Documentation     Workflow to test Hub criteria and display in queues
Suite Setup    Driver Launch
Library  SeleniumLibrary        timeout=200s
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/hub cases.robot

Suite Teardown  Close Browser

*** Test Cases ***

Hub_Cases_1
    [Documentation]    Mark a Case eligible for a Healthcare Hub
    Sleep   320s
    HQ Login
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name} ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Fill up Healthcare section
    Open Hub Healthcare Cases
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    Pending
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Hub Status       In Progress
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    In Progress
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Hub Status       Complete
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}

Hub_Cases_2
    [Documentation]    Mark a Case eligible for a Congregate Settings Hub
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name} ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Fill up Congregate section
    Open Hub Congregate Settings Cases
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    Pending
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Hub Status       In Progress
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    In Progress
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Hub Status       Complete
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}

Hub_Cases_3
    [Documentation]    Mark a Case eligible for Clusters Hub
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Fill up Cluster section
    Open Hub Clusters Cases
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    Pending
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Cluster Hub Status       In Progress
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    In Progress
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Cluster Hub Status       Complete
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}

Hub_Cases_4
    [Documentation]    Mark a Case eligible for Clusters Hub
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Fill up CSS section
    Open Hub Community Support Specialist Cases
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    Pending
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Cluster Hub Status       In Progress
    Search in the case list     ${case_name}
    Verify Hub Status       ${case_name}    In Progress
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Cluster Hub Status       Complete
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}


Hub_Cases_5
    [Documentation]    Mark a Case eligible for a School Hub
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    ${school}       ${date}=    Fill up School section
    Open Hub School Cases
    Search in the case list     ${case_name}
    Verify School Name and Date     ${case_name}    ${school}   ${date}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Update Cluster Hub Status       Complete
    Search in the case list     ${case_name}
    Element Should Not Be Visible    ${case_created}

Hub_Cases_6
    [Documentation]    Enter information in Childcare/School/College Details section to appear in the School Hub
    Log in as ci_user
    Register New Case
    Simple Form Fill up
    Open All Cases: Unassigned & Open
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Search in the case list     ${case_name} ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Enter Information in School College Details section
    Open Hub School Cases
    Search in the case list     ${case_name}
    Page Should Contain Element    ${case_created}

