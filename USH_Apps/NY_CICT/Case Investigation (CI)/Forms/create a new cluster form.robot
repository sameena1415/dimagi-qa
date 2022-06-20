*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Keywords ***

Generate Random Cluster Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Cluster	${hex}
    Set Suite Variable  ${name_random}


Open View Update Cluster Info Form
    Sleep    2s
    Wait Until Element Is Enabled    ${View Update Cluster Info Form}
    JS Click    ${View Update Cluster Info Form}

Open Create New Cluster Form
    Sleep    2s
    Wait Until Element Is Enabled    ${Create New Cluster Form}
    JS Click    ${Create New Cluster Form}



Create New Cluster - non school/college
    Open Create New Cluster Form
    ${date}    Get Current Date    result_format=%#m/%#d/%Y
    Generate Random Cluster Name
    ${name_random}    Get Variable Value    ${name_random}
    Wait Until Keyword Succeeds  2 min  5 sec   Wait Until Element Is Visible    ${cluster_name_field}
    Input Text    ${cluster_name_field}       ${name_random}
    JS Click    ${cluster_investigation}
    JS Click    ${cluster_setting_childcare}
    Input Text    ${description_of_cluster}     test
    Page Should Contain Element    ${cluster_site_info}
    Scroll Element Into View    ${cluster_site_name}
    Input Text    ${cluster_site_name}      ${name_random} site
    ${Mobile number}    Generate Mobile Number
    Input Text       ${cluster_phone}     ${Mobile number}
    Input Text    ${cluster_street_address}     ${name_random} street address
    Input Text    ${cluster_city}       ${name_random} city
    Select From List By Label    ${cluster_state}       New York
    Input Text    ${cluster_zip}        90210
    Input Text    ${cluster_site_contact_person}        ${name_random} contact person
    Input Text    ${cluster_site_contact_person_title}      title ${name_random}
    Input Text    ${cluster_number_of_individuals_on_site}    5
    ${id}=      Get Cluster ID created
    Submit Form and Check Success
    [Return]    ${id}


Create New Cluster - school/college
    Open Create New Cluster Form
    ${date}    Get Current Date    result_format=%#m/%#d/%Y
    Generate Random Cluster Name
    ${name_random}    Get Variable Value    ${name_random}
    Wait Until Element Is Visible    ${cluster_name_field}
    Input Text    ${cluster_name_field}       ${name_random}
    JS Click    ${cluster_investigation}
    JS Click    ${cluster_setting_school}
    Input Text    ${description_of_cluster}     test school
    Page Should Contain Element    ${cluster_site_info}
    Scroll Element Into View    ${cluster_site_info}
    Select From List By Index    ${cluster_select_school}       2
    Input Text    ${cluster_site_contact_person}        ${name_random} school contact person
    Input Text    ${cluster_site_contact_person_title}      title school ${name_random}
    Input Text    ${cluster_number_of_individuals_on_site}    5
    ${id}=      Get Cluster ID created
    Submit Form and Check Success
    [Return]    ${id}

Get Cluster ID created
    ${string}=      Get Text    ${cluster_id}
    ${str}=       String.Split String    ${string}    :
    ${str}=     String.Strip String    ${str}[1]
    [Return]     ${str}

Get Cluster Name
    ${name_random}    Get Variable Value    ${name_random}
#    ${name_random}     Set Variable     Patient-bf57
    Log    ${name_random}
    [Return]    ${name_random}

Set Cluster Name
    ${name_random}  Get Cluster Name
#    ${case_created}   Set Variable    //tr[.//td[text()='${name_random}' and @class='module-case-list-column']]
    ${case_created}   Set Variable    //tr[.//td[text()='${name_random}']]
    Log    ${case_created}
    Set Suite Variable    ${case_created}
    [Return]    ${case_created}



    
Verify Specimen collection date in cluster
    [Arguments]     ${date}
    Sleep    5s
    Page Should Contain Element    ${specimen_date_of_first_case}\[contains(text(),'${date}')]

Update Cluster - non school/college
    [Arguments]     ${date}     ${name}
    ${name_random}    Get Variable Value    ${name}
    ${name_random}    Set Variable      update ${name_random}
    Wait Until Element Is Visible       ${cluster_name_field}
    Input Text    ${cluster_name_field}       ${name_random}
    JS Click    ${cluster_outbreak}
    JS Click    ${cluster_shelter}
    Input Text    ${description_of_cluster}     update
    Page Should Contain Element    ${cluster_site_info}
    Scroll Element Into View    ${cluster_site_name}
    Input Text    ${cluster_site_name}      ${name_random} site
    ${Mobile number}    Generate Mobile Number
    Input Text       ${cluster_phone}     ${Mobile number}
    Input Text    ${cluster_street_address}     ${name_random} street address
    Input Text    ${cluster_city}       ${name_random} city
    Select From List By Label    ${cluster_state}       New York
    Input Text    ${cluster_zip}        62321
    Input Text    ${cluster_site_contact_person}        ${name_random} contact person
    Input Text    ${cluster_site_contact_person_title}      title ${name_random}
    Input Text    ${cluster_number_of_individuals_on_site}    3
    Verify Specimen collection date in cluster      ${date}
    Submit Form and Check Success
    [Return]    	${name_random}

Update Cluster - school/college
    [Arguments]     ${name}
    ${name_random}    Get Variable Value    ${name}
    ${name_random}    Set Variable      update ${name_random}
    Wait Until Element Is Visible    ${cluster_name_field}
    Input Text    ${cluster_name_field}       ${name_random}
    JS Click    ${cluster_outbreak}
    JS Click    ${clutter_college}
    Input Text    ${description_of_cluster}     update school
    Page Should Contain Element    ${cluster_site_info}
    Scroll Element Into View    ${cluster_site_info}
    Select From List By Index    ${cluster_select_school}       3
    Input Text    ${cluster_site_contact_person}        ${name_random} school contact person
    Input Text    ${cluster_site_contact_person_title}      title school ${name_random}
    Input Text    ${cluster_number_of_individuals_on_site}    3
    Submit Form and Check Success
    [Return]    	${name_random}

Verify non school cluster update
    [Arguments]     ${updated_cluster_name}     ${cluster_id_created}
    Page Should Contain    ${cluster_id_created}
    ${string}=      Get Element Attribute    ${cluster_name_field}    value
    IF    "${string}" == "${updated_cluster_name}"
        Log To Console    Cluster Updated
    END

Close Cluster
    Scroll Element Into View    ${close_cluster_section}
    JS Click    ${close_cluster_yes}
    Wait Until Element Is Visible    ${cluster_closure_reason}
    JS Click    ${cluster_closure_reason}
    Submit Form and Check Success

Verify cluster closed
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[9][normalize-space()='Closed']


Reopen Cluster
    Scroll Element Into View    ${reopen_cluster_section}
    JS Click    ${reopen_cluster_yes}
    Submit Form and Check Success

Verify cluster open
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[9][normalize-space()='Open']

Close Cluster error registered
    Scroll Element Into View    ${close_cluster_section}
    JS Click    ${close_cluster_yes}
    Wait Until Element Is Visible    ${cluster_closure_registered_in_error}
    JS Click    ${cluster_closure_registered_in_error}
    Submit Form and Check Success

Verify cluster not present
    [Arguments]  ${case_name}
    Element Should Not Be Visible    //tr[.//td[text()='${case_name}']]
