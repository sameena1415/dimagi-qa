*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## Close the Contact Record Form
${Close the Contact Record}    //tr[@aria-label='Close the Contact Record']
${Q: Close the Contact}    //p[text()='Are you sure you want to close this record?']
${A: Yes, close contact}     //p[text()='Yes, close this contact']
${A: No, do not close contact}     //p[text()='No, do not close this contact']
${Message: Contact will be closed}       //p[text()='This Contact will be closed with the following properties:']
${Q: Reopen the Contact}     //*[text()='Are you sure you want to reopen it?']
${A: Yes, reopen contact}     //p[text()='Yes, reopen this Contact']
${A: No, do not reopen contact}     //p[text()='No, keep the record closed']
${Message: contact will be reopen}       //p[text()='This Contact will be reopened with the following properties:']
${Message: final disposition blank}     //li[contains(normalize-space(),'blank')]/strong[text()='Final Disposition:']

${submit_form}
${success_message}    //p[text()='Form successfully saved!']

*** Keywords ***


Open Close the Contact Record Form
    Wait Until Element Is Enabled    ${Close the Contact Record}
    JS Click    ${Close the Contact Record}

Close Contact record - No
    Open Close the Contact Record Form
    Wait Until Element Is Enabled    ${Q: Close the Contact}
    JS Click    ${A: No, do not close contact}
    Submit Form and Check Success

Close Contact record - Yes
    Open Close the Contact Record Form
    Wait Until Element Is Enabled    ${Q: Close the Contact}
    JS Click    ${A: Yes, close contact}
    Wait Until Element Is Visible    ${follow_up_complete_disposition}
    JS Click    ${follow_up_complete_disposition}
    Element Should Be Visible    ${Message: Contact will be closed}
    Submit Form and Check Success

Reopen Contact record - No
    Open Close the Contact Record Form
    Wait Until Element Is Enabled    ${Q: Reopen the Contact}
    JS Click    ${A: No, do not reopen contact}
    Submit Form and Check Success

Reopen Contact record - Yes
    Open Close the Contact Record Form
    Wait Until Element Is Enabled    ${Q: Reopen the Contact}
    JS Click    ${A: Yes, reopen contact}
    Element Should Be Visible    ${Message: contact will be reopen}
    Element Should Be Visible    ${Message: final disposition blank}
    Submit Form and Check Success

Verify Contact Open Status
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[10][normalize-space()='Open']

Verify Contact Close Status
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[10][normalize-space()='Closed']

