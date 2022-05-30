*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## View/Record Lab Result Form
${View Record Lab results}    //tr[@aria-label='View / Record Lab Results']
${Record New Result}    //button[text()='Record New Result']
${patient_first_name}     //span[text()='Patient First Name']/following::div[1]/div[@class='widget']/descendant::textarea
${patient_last_name}     //span[text()='Patient Last Name']/following::div[1]/div[@class='widget']/descendant::textarea
${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']

*** Keywords ***


Generate Random Patient Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Patient	${hex}
    Set Suite Variable  ${name_random}

Open View Record Lab Results Form
    Wait Until Element Is Enabled    ${View Record Lab results}
    JS Click    ${View Record Lab results}

Add New Lab Result
    Open View Record Lab Results Form
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

