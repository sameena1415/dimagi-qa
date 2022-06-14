*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot 


*** Variables ***

## Case Investigation Form ##

${Case Investigation Form}    //tr[@aria-label='Case Investigation']

*** Keywords *** 


Verify Hub Status Contacts
    [Arguments]      ${case_name}   ${hub_status}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[normalize-space()='${hub_status}']

Verify School Name and Date Contacts
    [Arguments]     ${case_name}    ${school}   ${date}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    ${value}=   Get Text    //tr[.//td[text()='${case_name}']]/self::tr//td[5]
    ${ispresent}=       Run Keyword And Return Status    Should Contain    ${school}    ${value}
    Should Be True    ${ispresent}
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[6][normalize-space()='${date}']



Update Hub Status Contacts
    [Arguments]     ${hub_status}
    Scroll Element Into View    ${hub_task_force_followup}
    JS Click    ${cluster_hub_status_selection}\[.='${hub_status}']
    Submit Form and Check Success

Update Cluster Hub Status Contacts
    [Arguments]     ${hub_status}
    Scroll Element Into View    ${hub_task_force_followup}
    JS Click    ${cluster_hub_status_selection}\[.='${hub_status}']
    Submit Form and Check Success

Update School Hub Status Contacts
    [Arguments]     ${hub_status}
    Scroll Element Into View    ${hub_task_force_followup}
    JS Click    ${cluster_hub_status_selection}\[.='${hub_status}']
    Submit Form and Check Success
