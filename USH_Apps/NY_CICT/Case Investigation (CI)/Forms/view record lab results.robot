*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot

*** Keywords ***

Add New Lab Result
    Open Form   ${View Record Lab results}
    Wait Until Element Is Enabled    ${Record New Result}
    Click Button    ${Record New Result}
    Wait Until Element Is Visible    ${specimen_collection_date}
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
    Wait Until Element Is Visible    ${specimen_collection_date}
    ${Past date}    Past Date Generator     ${days}
    Input Text    ${specimen_collection_date}   ${Past date}
    Submit Form and Check Success

