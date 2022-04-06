*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## Register a New Case Form
${Register a New Case}    (//div[@aria-label='Register a New Case']/div)[1]
${patient_first_name}     //span[text()='Patient First Name']/following::div[1]/div[@class='widget']/descendant::textarea
${patient_last_name}     //span[text()='Patient Last Name']/following::div[1]/div[@class='widget']/descendant::textarea
${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']

*** Keywords ***

Generate Random Patient Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Patient	${hex}
    Set Suite Variable  ${name_random}

Register New Case
    Sleep    2s
    Wait Until Element Is Enabled    ${Register a New Case}
    Click Element    ${Register a New Case}
    Generate Random Patient Name
    ${name_random}    Get Variable Value    ${name_random}
    Input Text       ${patient_first_name}    ${name_random}
    Input Text       ${patient_last_name}    ${name_random}
    Submit Form and Check Success
    
Get Case Name
    ${name_random}    Get Variable Value    ${name_random}
#    ${name_random}     Set Variable     Patient-bf57
    Log    ${name_random}
    [Return]    ${name_random}

Set Case Name
    ${name_random}  Get Case Name
    ${case_created}   Set Variable    //td[text()='${name_random}' and @class='module-case-list-column']
    Log    ${case_created}
    Set Suite Variable    ${case_created}
    [Return]    ${case_created}    
    