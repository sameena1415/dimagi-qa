*** Settings ***
Documentation     Workflow to test Patient Good Path
Suite Setup    HQ Login
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Case Investigation (CI)/Forms/assign or reassign form.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Suite Teardown  Close Browser

*** Test Cases ***

Daily_Monitoring_1
    [Documentation]    Daily monitoring not selected, then selected
    Log in as ci_user
    Register New Case
    ${case_interview}=  Set variable    Yes
    ${daily_monitoring}=    Set variable    No
    ${activity_complete}=   Set variable    No
    Complete full interview     ${case_interview}   ${daily_monitoring}     ${activity_complete}
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Open All Open Cases
    Search in the case list     ${case_name}
    Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Daily Monitoring - Yes
    Open All Open Cases
    Search in the case list     ${case_name}
    Verify Daily Monitoring Status    ${case_name}      yes
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Daily Monitoring Section

Daily_Monitoring_2
    [Documentation]    Daily monitoring notes
    Open App Home Screen
    Log in as ci_user
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    @{notes_list}=      Create List
    FOR    ${i}    IN RANGE    3
        ${j}=    Evaluate    ${i} + 1
        Open All Cases
        Search in the case list     ${case_name}
        Select Created Case    ${case_created}
        Open Case Investigation Form
        ${note}=    Set Variable    test note ${j}
        ${created_note}=       Daily Monitorying notes     ${note}      @{notes_list}
        Collections.Append To List    ${notes_list}     ${created_note}
    END
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Monitoring logs      @{notes_list}

Daily_Monitoring_3
    [Documentation]    Daily follow up monitoring log/notes
    Open App Home Screen
    Log in as ci_user
    Register New Case
    ${case_interview}=  Set variable    Yes
    ${daily_monitoring}=    Set variable    Yes
    ${activity_complete}=   Set variable    No
    Complete full interview     ${case_interview}   ${daily_monitoring}     ${activity_complete}
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    @{follow_list}=      Create List
    FOR    ${i}    IN RANGE    3
        ${j}=    Evaluate    ${i} + 1
        Open All Cases
        Search in the case list     ${case_name}
        Select Created Case    ${case_created}
        Open Case Investigation Form
        ${followup}=    Set Variable    follow up attempt ${j}
        ${created_log}=       Follow up attempt notes     ${followup}      @{follow_list}
        Collections.Append To List    ${follow_list}     ${created_log}
    END
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Follow Up logs       @{follow_list}

Daily_Monitoring_4
    [Documentation]    Interview not complete and needs monitoring, then interview complete
#    Open App Home Screen
    Log in as ci_user
    Register New Case
    ${case_interview}=  Set variable    No
    ${daily_monitoring}=    Set variable    Yes
    ${activity_complete}=   Set variable    No
    Complete full interview     ${case_interview}   ${daily_monitoring}     ${activity_complete}
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Open All Cases
    Search in the case list     ${case_name}
    Element Should Be Visible    ${case_created}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Interview Not Complete
    Interview Complete
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Interview Complete

Daily_Monitoring_5
    [Documentation]    Successful follow-up attempt and unsuccessful follow-up attempt
#    Open App Home Screen
    Log in as ci_user
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Interview Complete
    Add new follow up log       success
    Enter Response for Follow Up - No
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify fever, symptoms, help all no logs
    Add new follow up log       success
    Enter Response for Follow Up - Yes
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify fever, symptoms, help all logs
    Add new follow up log       unsuccess
    ${log}=     Add follow up unsuccess notes
    Submit Form and Check Success
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify unsuccessful logs        ${log}



Daily_Monitoring_6
    [Documentation]    Successful follow-up attempt and unsuccessful follow-up attempt
    Open App Home Screen
    Log in as ci_user
    Register New Case
    ${case_interview}=  Set variable    Yes
    ${daily_monitoring}=    Set variable    Yes
    ${activity_complete}=   Set variable    No
    Complete full interview     ${case_interview}   ${daily_monitoring}     ${activity_complete}
    ${case_name}    Get Case Name
    ${case_created}   Set Case Name
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Verify Interview Complete
    Enter Provider Info
    Open All Cases
    Search in the case list     ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    Validate Provider Info
