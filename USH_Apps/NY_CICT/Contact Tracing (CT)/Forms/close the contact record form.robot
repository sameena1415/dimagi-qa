*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot

*** Keywords ***

Close Contact record - No
    Open Form   ${Close the Contact Record}
    Wait Until Element Is Enabled    ${Q: Close the Contact}
    JS Click    ${A: No, do not close contact}
    Submit Form and Check Success

Close Contact record - Yes
    Open Form   ${Close the Contact Record}
    Wait Until Element Is Enabled    ${Q: Close the Contact}
    JS Click    ${A: Yes, close contact}
    Wait Until Element Is Visible    ${follow_up_complete_disposition}
    JS Click    ${follow_up_complete_disposition}
    Element Should Be Visible    ${Message: Contact will be closed}
    Submit Form and Check Success

Reopen Contact record - No
    Open Form   ${Close the Contact Record}
    Wait Until Element Is Enabled    ${Q: Reopen the Contact}
    JS Click    ${A: No, do not reopen contact}
    Submit Form and Check Success

Reopen Contact record - Yes
    Open Form   ${Close the Contact Record}
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

