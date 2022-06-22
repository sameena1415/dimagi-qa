*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Keywords ***

Generate Random Patient Name
    ${hex} =    Generate Random String	6	[NUMBERS]abcdef
    ${date}     Get Current Date    result_format=%m/%d/%Y
    ${name_random} =     Catenate	SEPARATOR=-	Patient	${hex} ${date}
    Set Suite Variable  ${name_random}

Register New Case
    [Arguments]     ${name}=${null}     ${mpi_id}=${EMPTY}
    Sleep    2s
    Wait Until Element Is Enabled    ${Register a New Case}
    Click Element    ${Register a New Case}
    IF    "${name}" != "${null}"
        Input Text       ${patient_first_name}    ${name}
        Input Text       ${patient_last_name}    ${name}
        Input Text       ${mpi_id_input}      ${mpi_id}
    ELSE
        Generate Random Patient Name
        ${name_random}    Get Variable Value    ${name_random}
        Input Text       ${patient_first_name}    ${name_random}
        Input Text       ${patient_last_name}    ${name_random}
        Input Text       ${mpi_id_input}      ${mpi_id}
    END
    Submit Form and Check Success
  [Return]  ${mpi_id}   ${name}

Get Case Name
    ${name_random}    Get Variable Value    ${name_random}
#    ${name_random}     Set Variable     Patient-bf57
    Log    ${name_random}
    [Return]    ${name_random}

Set Case Name
    ${name_random}  Get Case Name
#    ${case_created}   Set Variable    //tr[.//td[text()='${name_random}' and @class='module-case-list-column']]
    ${case_created}   Set Variable    //tr[.//td[text()='${name_random}']]
    Log    ${case_created}
    Set Suite Variable    ${case_created}
    [Return]    ${case_created}    
    