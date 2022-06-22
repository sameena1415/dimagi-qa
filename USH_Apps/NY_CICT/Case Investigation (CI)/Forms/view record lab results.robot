*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot

*** Keywords ***

Open View Record Lab Results Form
    Wait Until Element Is Enabled    ${View Record Lab results}
    JS Click    ${View Record Lab results}

Add New Lab Result
    Open View Record Lab Results Form
    Wait Until Element Is Enabled    ${Record New Result}
    Click Button    ${Record New Result}
    Wait Until Element Is Visible    ${specimen_collection_date}    60s
    Scroll Element Into View    ${lab_result_positive}
    JS Click    ${lab_result_positive}
    ${num} =    Generate Random String	6	[NUMBERS]
    Input Text    ${accession_number}   ${num}
    ${Past date}    Past Date Generator     4
    Input Text    ${specimen_collection_date}   ${Past date}
    Submit Form and Check Success

Record specimen date
    [Arguments]     ${days}
    Wait Until Element Is Enabled    ${Record New Result}
    JS Click    ${Record New Result}
    Wait Until Element Is Visible    ${specimen_collection_date}    80s
    ${Past date}    Past Date Generator     ${days}
    Input Text    ${specimen_collection_date}   ${Past date}
    Submit Form and Check Success

