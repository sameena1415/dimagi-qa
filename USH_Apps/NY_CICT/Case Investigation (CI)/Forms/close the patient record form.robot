*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


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
