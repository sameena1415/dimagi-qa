*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## Close the Patient Record Form
${Close the Patient Record}    //tr[@aria-label='Close the Patient Record']
${Q: Close the Record}    //p[text()='Are you sure you want to close this record?']
${A: Yes, close record}     //p[text()='Yes, close this case']
${A: No, do not close record}     //p[text()='No, do not close this case']
${Message: Record will remain open}     //p[text()='This record will remain open.']
${Message: Record will be closed}       //p[text()='This record will be closed with the following properties:']
${Q: Reopen the Record}     //*[text()='Are you sure you want to reopen it?']
${A: Yes, reopen record}     //p[text()='Yes, reopen this record']
${A: No, do not reopen record}     //p[text()='No, keep the record closed']
${Message: record will be reopen}       //p[text()='This Patient Record will be reopened with the following properties:']

${submit_form}
${success_message}    //p[text()='Form successfully saved!']

*** Keywords ***


Open Close the Patient Record Form
    Wait Until Element Is Enabled    ${Close the Patient Record}
    JS Click    ${Close the Patient Record}

Close Patient record - No
    Open Close the Patient Record Form
    Wait Until Element Is Enabled    ${Q: Close the Record}
    JS Click    ${A: No, do not close record}
    Element Should Be Visible    ${Message: Record will remain open}
    Submit Form and Check Success

Close Patient record - Yes
    Open Close the Patient Record Form
    Wait Until Element Is Enabled    ${Q: Close the Record}
    JS Click    ${A: Yes, close record}
    Wait Until Element Is Visible    ${final_disposition2}
    JS Click    ${final_disposition2}
    Element Should Be Visible    ${Message: Record will be closed}
    Submit Form and Check Success

Reopen Patient record - No
    Open Close the Patient Record Form
    Wait Until Element Is Enabled    ${Q: Reopen the Record}
    JS Click    ${A: No, do not reopen record}
    Submit Form and Check Success

Reopen Patient record - Yes
    Open Close the Patient Record Form
    Wait Until Element Is Enabled    ${Q: Reopen the Record}
    JS Click    ${A: Yes, reopen record}
    Element Should Be Visible    ${Message: record will be reopen}
    Submit Form and Check Success

Verify Open Status
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[9][normalize-space()='Open']

Verify Close Status
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[9][normalize-space()='Closed']

Verify Final Disposition Blank
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[8][not(normalize-space())]
