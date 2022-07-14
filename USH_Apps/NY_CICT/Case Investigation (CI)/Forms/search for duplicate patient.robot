*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Keywords ***


Generate Random Patient Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Patient	${hex}
    Set Suite Variable  ${name_random}

Open Search for Duplicate Patients
    Wait Until Element Is Enabled    ${Search for Duplicate Patients}
    JS Click    ${Search for Duplicate Patients}

Search Duplicate Patient
    [Arguments]     ${contact_name}
    Open Search for Duplicate Patients
    Wait Until Keyword Succeeds  3x  500ms     JS Click    ${search-submit}
    Wait Until Element Is Visible    //tr[.//td[text()='${contact_name}']]
    JS Click    //tr[.//td[text()='${contact_name}']]
    Wait Until Element Is Enabled    ${continue}
    Sleep    2s
    Click Element    ${continue}
    Wait Until Element Is Visible    ${selected_patient_is_duplicate}
    JS Click    ${selected_patient_is_duplicate}
    JS Click    ${keep_current_close_selected}
    Submit Form and Check Success



Verify Lab result for open case
    [Arguments]     ${case_or_contact_created}
    Sleep    4s
    Wait Until Element Is Enabled    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[9][normalize-space()='Open'])
    Sleep    2s
    JS Click    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[9][normalize-space()='Open'])
    Sleep    3s
    Wait Until Element Is Visible    ${lab_result_tab}
    Click Element    ${lab_result_tab}
    Sleep    2s
    Element Should Be Visible    ${lab_result_tab_positive}
    Click Element    ${continue}

Verify Registered Contacts for open case
     [Arguments]    ${created_name}
     JS Click    ${register_new_contacts_form}
     Wait Until Keyword Succeeds    2 min  5 sec    Element Should Be Visible    //p['Contact Name:'][contains(text(),'${created_name}_1 ${created_name}_1')]
     Element Should Be Visible    //p['Contact Name:'][contains(text(),'${created_name}_2 ${created_name}_2')]