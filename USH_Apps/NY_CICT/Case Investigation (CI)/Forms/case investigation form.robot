*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot 


*** Variables ***

## Case Investigation Form ##

${Case Investigation Form}    //tr[@aria-label='Case Investigation']

${Q:Case Interview Disposition A:Reached person, agreed to call}    //p[text()='Reached person, agreed to call']
${Q:Case Interview Disposition A:Attempted for two days and unable to reach}    //p[text()='Attempted for two days and unable to reach']

${Q:Home/Cell Phone}    //span[text()='Home/Cell Phone']/following::div[1]/div[@class='widget']/descendant::input
${Q:Date Tested}    //p[text()='What date did you get tested?']/following::div[1]/div[@class='widget']/descendant::input
${Q:Preferred Language A:English}    //p[text()='English']

${Q:Search For Address}    //span[text()='Search for Address']/following::div[1]/div[@class='widget']/descendant::input
${Address}     South Side River Bourgeois Road, Subdivision A, Nova Scotia B0E 2X0, Canada
${Fisrt address}    //li[contains(.,'South Side')]

${Q:County of residence}    (//*[contains(text(),'County')])[1]/following::span[@title='Please choose an item'][1]

${A:County of residence}    //label[.//*[contains(text(),'County')]]/following-sibling::div//select
#//*[contains(text(),'County')][1]/following::ul[@role='listbox']/li[1]
${Country success}    (//*[contains(text(),'County')])[1]/following::i[@class="fa fa-check text-success"][1]

${Q:State}    //span[text()='State']/following::span[@title='Please choose an item'][1]
${A:State}    //label[.//*[.='State']]/following-sibling::div//select
#//*[contains(text(),'State')][1]/following::ul[@role='listbox']/li[1]
${State success}    //span[text()='State']/following::i[@class="fa fa-check text-success"][1]

${Q:Zipcode_error}     //label[.//span[text()='Zip Code']]/following-sibling::div//textarea[contains(@data-bind,'value: $data.rawAnswer')]
${Q:Zipcode_normal}     //label[.//span[text()='Zip Code']]/following-sibling::div//textarea
${Zipcode success}    //label[.//span[text()='Zip Code']]/following-sibling::div//i[@class="fa fa-check text-success"]
${Zipcode failure}    //label[.//span[text()='Zip Code']]/following-sibling::div//i[@class="fa fa-warning text-danger clickable"]

${Q:Transer Patient A: No}    //p[contains(.,'No, do not transfer')]

${Q:Activity complete A: Yes}    //span[contains(.,'Is all activity for this case complete')]/following::p[text()='Yes']
${Q:Activity complete A: No}    //span[contains(.,'Is all activity for this case complete')]/following::p[text()='No']
${Q:Case Interview complete A: No}    //span[contains(.,'Is the case interview complete?')]/following::p[text()='No']
${Q:Case Interview complete A: Yes}    //span[contains(.,'Is the case interview complete?')]/following::p[text()='Yes']
${Clear Case Interview complete}     //label[.//span[contains(.,'Is the case interview complete?')]]/following-sibling::div//button
${Q:Needs Daily Monitoring}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]
${Q:Needs Daily Monitoring A: No}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]/following-sibling::div//p[text()='No']
${Q:Needs Daily Monitoring A: Yes}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]/following-sibling::div//label//input[@value='Yes']
${Clear Daily monitoring selection}     //label[.//span[contains(.,'Does the case need daily monitoring?')]]/following-sibling::div//button
${Q:Final Disposition A:Reached, completed investigation}    //p[text()='Reached, completed investigation']
${Q: Willing to receive survey via SMS}       //label//span[contains(.,'willing to receive a daily survey via SMS?')]
${Q: Willing to receive survey via SMS A: No}       //label//span[contains(.,'willing to receive a daily survey via SMS?')]//following::p[text()='No']
${Q:Gender A:Female}    //p[text()='Female']
${Q:Race A:Asian}    //p[text()='Asian']
${Q:Ethnicity A:Hispanic/Latino}    //p[text()='Hispanic/Latino']

${Submit Form}     //button[@type='submit' and @class='submit btn btn-primary']
${Success Message}    //p[text()='Form successfully saved!']



*** Keywords *** 
    
Open Case Investigation Form
    Sleep    2s
    Wait Until Element Is Enabled    ${Case Investigation Form} 
    JS Click    ${Case Investigation Form} 
    
Fill up and Submit Case Investigation Form
   Open Case Investigation Form
   Wait Until Element Is Enabled    ${Q:Case Interview Disposition A:Reached person, agreed to call}    
   JS Click    ${Q: Case Interview Disposition A:Reached person, agreed to call}
   Add User Details
   ${Yesterday's date}    Yesterday's Date
   Input Text    ${Q:Date Tested}    ${Yesterday's date}
   Add Address
   Submit Form and Check Success
   
Add Address
   # Select Address
   Run Keyword And Ignore Error    Input Text    ${Q:Search For Address}   ${Address}
   Press Keys   ${Q:Search For Address}     ENTER   TAB
#   Click Element    ${Fisrt address}
   Sleep    15s
   # Contry
   Select Dropdown   ${Q:County of residence}    ${A:County of residence}

   # Zipcode
#   Execute JavaScript    window.document.evaluate(${Q:Zipcode_normal}, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollIntoView(true);
   Scroll Element Into View    ${Q:Zipcode_error}
#   Wait Until Element Is Visible    ${Zipcode failure}    80s
   Wait Until Element Is Enabled   ${Q:Zipcode_error}     60s
   Clear Element Text    ${Q:Zipcode_error}
   Press Keys    ${Q:Zipcode_normal}   12345    TAB
   Sleep    10s
   Wait Until Element Is Visible    ${Zipcode success}  60s

   # State
   Select Dropdown   ${Q:County of residence}    ${A:County of residence}
   Select Dropdown    ${Q:State}    ${A:State}
   Transfer Patient - No
   
Transfer Patient - No
   Wait Until Element Is Enabled    ${Q:Transer Patient A: No} 
   Scroll Element Into View    ${Q:Transer Patient A: No}     
   JS Click    ${Q:Transer Patient A: No}
   
Add User Details
   JS Click    ${Q:Preferred Language A:English}
   ${Mobile number}    Generate Mobile Number
   Input Text       ${Q:Home/Cell Phone}     ${Mobile number}
   JS Click    ${Q:Gender A:Female}
   JS Click    ${Q:Race A:Asian}
   JS Click    ${Q:Ethnicity A:Hispanic/Latino} 
    

Unable to reach
   Wait Until Element Is Enabled    ${Q:Case Interview Disposition A:Attempted for two days and unable to reach}    
   JS Click    ${Q:Case Interview Disposition A:Attempted for two days and unable to reach}
   Run Keyword And Ignore Error    Transfer Patient - No
   Submit Form and Check Success 
   
    

Activity for case complete
    Wait Until Element Is Enabled    ${Q:Activity complete A: Yes}     
    JS Click    ${Q:Activity complete A: Yes} 
    Wait Until Element Is Visible    ${Q:Final Disposition A:Reached, completed investigation}
    JS Click    ${Q:Final Disposition A:Reached, completed investigation}
    Run Keyword And Ignore Error    Transfer Patient - No
    Submit Form and Check Success 

Add Phone Number in Case Investigation form
   [Arguments]      ${phone}
   Wait Until Element Is Enabled    ${Q:Case Interview Disposition A:Reached person, agreed to call}
   JS Click    ${Q: Case Interview Disposition A:Reached person, agreed to call}
   Input Text       ${Q:Home/Cell Phone}     ${phone}
   Submit Form and Check Success


Activity for case complete - Yes
    Wait Until Element Is Enabled    ${no_attempts_made_disposition}
    JS Click    ${no_attempts_made_disposition}
    Wait Until Element Is Enabled    ${Q:Activity complete A: Yes}
    JS Click    ${Q:Activity complete A: Yes}
    Wait Until Element Is Visible    ${Q:Final Disposition A:Reached, completed investigation}
    JS Click    ${Q:Final Disposition A:Reached, completed investigation}
    Submit Form and Check Success

Activity for case complete - No
    Wait Until Element Is Enabled    ${no_attempts_made_disposition}
    JS Click    ${no_attempts_made_disposition}
    Wait Until Element Is Enabled    ${Q:Activity complete A: No}
    JS Click    ${Q:Activity complete A: No}
    Submit Form and Check Success

Complete full interview
   [Arguments]      ${case_interview}   ${daily_monitoring}     ${activity_complete}
   Wait Until Element Is Enabled    ${Q:Case Interview Disposition A:Reached person, agreed to call}
   JS Click    ${Q: Case Interview Disposition A:Reached person, agreed to call}
   ${Mobile number}    Generate Mobile Number
   Input Text       ${Q:Home/Cell Phone}   ${Mobile number}
   Add User Details
   ${Yesterday's date}    Yesterday's Date
   Input Text    ${Q:Date Tested}    ${Yesterday's date}
   JS Click    ${Q:Case Interview complete A: ${case_interview}}
   JS Click    ${Q:Needs Daily Monitoring A: ${daily_monitoring}}
   JS Click    ${Q:Activity complete A: ${activity_complete}}
   Run Keyword And Ignore Error     Scroll Element Into View    ${Q: Willing to receive survey via SMS}
   Run Keyword And Ignore Error     Wait Until Element Is Visible    ${Q: Willing to receive survey via SMS A: No}
   Run Keyword And Ignore Error     JS Click    ${Q: Willing to receive survey via SMS A: No}
   Submit Form and Check Success

Daily Monitoring - Yes
    Sleep    10s
    Wait for condition  return window.document.readyState === 'complete'
    Wait Until Element Is Visible    ${interview_info_section}
    ${IsElementPresent}=     Element Should Be Visible    ${interview_info_section}
    IF    ${IsElementPresent}
       Log To Console    Interview Information section is present
    END
    Scroll Element Into View    ${Q:Needs Daily Monitoring A: No}
    JS Click    ${Clear Daily monitoring selection}
    Sleep    3s
    JS Click    ${Q:Needs Daily Monitoring A: Yes}
    ${IsElementPresent}=    Element Should Not Be Visible    ${daily_monitoring_section}
    Sleep    2s
    IF    ${IsElementPresent}
       Log To Console    Daily Monitoring section is not present
    END
    Scroll Element Into View    ${Q: Willing to receive survey via SMS}
    Wait Until Element Is Visible    ${Q: Willing to receive survey via SMS A: No}
    JS Click    ${Q: Willing to receive survey via SMS A: No}
    Submit Form and Check Success

Verify Daily Monitoring Status
    [Arguments]  ${case_name}      ${daily_monitoring_status}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[8][normalize-space()='${daily_monitoring_status}']

Verify Daily Monitoring Section

    Wait Until Element Is Visible    ${submit_form}
    Element Should Be Visible    ${daily_monitoring_section}
    Element Should Be Visible    ${view_update_rest_of_the_case_info}
    Element Should Not Be Visible    ${interview_info_section}


Daily Monitorying notes
    [Arguments]     ${new_notes}    @{notes}
    Wait Until Element Is Visible    ${patient_notes}
    Scroll Element Into View    ${patient_notes}
    Verify Monitoring logs      @{notes}
    ${today}    Get Current Date    result_format=%#m/%#d/%Y
    ${msg}    Set Variable      ${new_notes} , ${today}
    JS Click    ${add_new_note}
    Input Text    ${add_new_note_field}     ${msg}
    Press Keys      ${add_new_note_field}       TAB
    Submit Form and Check Success
    [Return]    ${msg}

Verify Monitoring logs
    [Arguments]     @{notes}
    JS Click    ${view_all_notes}

    FOR    ${note}    IN    @{notes}
        Log To Console    ${note}
        IF    "${note}" != "${EMPTY}"
            Page Should Contain Element    //p[text()='${note}']
        END
    END

Follow up attempt notes
    [Arguments]     ${new_notes}    @{notes}
    Wait Until Element Is Visible    ${daily_monitoring_section}
    Scroll Element Into View    ${daily_monitoring_section}
    Verify Follow Up logs       @{notes}
    ${today}    Get Current Date    result_format=%#m/%#d/%Y
    ${msg}    Set Variable      ${new_notes} , ${today}
    Add new follow up log       success
    Input Text    ${add_follow_up_log_field}     ${msg}
    Press Keys      ${add_follow_up_log_field}       TAB
    JS Click    ${fever_greater_than_100_no}
    JS Click    ${fever_reducing_medication_no}
    JS Click    ${any_other_symptoms_no}
    JS Click    ${two_negative_results_no}
    JS Click    ${help_for_isolation_no}
    Submit Form and Check Success
    [Return]    ${msg}

Add new follow up log
    [Arguments]     ${result}
    JS Click    ${add_new_follow_up_log}
    Wait Until Element Is Visible    ${follow_up_attempt_${result}}
    JS Click    ${follow_up_attempt_${result}}

Add follow up unsuccess notes
    ${today}    Get Current Date    result_format=%#m/%#d/%Y
    ${msg}    Set Variable      unsuccessful attempt test 1 ${today}
    Input Text      ${add_follow_up_log_field}     ${msg}
    Press Keys      ${add_follow_up_log_field}       TAB
    Sleep   2s
    JS Click    ${view_follow_up_logs}
    [Return]    ${msg}

Enter Response for Follow Up - No
    Enter fever greater than 100        No
    Enter any other symptoms        No
    Enter any needs     No
    Submit Form and Check Success


Enter Response for Follow Up - Yes
    Enter fever greater than 100        Yes
    Enter any other symptoms        Yes
    Enter any needs     Yes
    Symptoms improving and then no
    Submit Form and Check Success


Verify Follow Up logs
    [Arguments]     @{notes}
    JS Click    ${view_follow_up_logs}
    FOR    ${note}    IN    @{notes}
        Log To Console    ${note}
        IF    "${note}" != "${EMPTY}"
            Page Should Contain Element     ${verify_notes}\[contains(text(),'${note}')]
            Page Should Contain Element     ${verify_attempt}
            Page Should Contain Element     ${verify_fever_temp}\[contains(text(),'')]
            Page Should Contain Element     ${verify_fever}\[contains(text(),'no')]
            Page Should Contain Element     ${verify_needs}\[contains(text(),'')]
            Page Should Contain Element     ${verify_other_symptoms}\[contains(text(),'no')]
        END
    END


Verify Interview Not Complete
    ${IsElementPresent}=     Element Should Be Visible    ${interview_info_section}
    IF    ${IsElementPresent}
       Log To Console    Interview Information section is present
    END
    ${IsElementPresent}=    Element Should Be Visible    ${daily_monitoring_section}
    Sleep    2s
    IF    ${IsElementPresent}
       Log To Console    Daily Monitoring section is present
    END

Interview Complete
    Scroll Element Into View    ${Q:Case Interview complete A: No}
    JS Click    ${Clear Case Interview complete}
    Sleep    3s
    JS Click    ${Q:Case Interview complete A: Yes}
    Submit Form and Check Success

Verify Interview Complete
    ${IsElementPresent}=    Element Should Be Visible    ${daily_monitoring_section}
    Sleep    2s
    IF    ${IsElementPresent}
       Log To Console    Daily Monitoring section is present
    END
    ${IsElementPresent}=    Element Should Be Visible    ${view_update_rest_of_the_case_info}
    IF    ${IsElementPresent}
        Log To Console    view/update the rest of the case's information button is present

    END
    ${IsElementPresent}=    Element Should Be Visible    ${status_section}
    IF    ${IsElementPresent}
        Log To Console    Status section is present

    END

Enter Provider Info
    Wait Until Element Is Visible       ${case_details_section}
    Scroll Element Into View    ${case_details_section}
    JS Click    ${view_update_rest_of_the_case_info}
    Wait Until Element Is Visible    ${provider_section}
    Scroll Element Into View    ${provider_section}
    Input Text    ${provider_name}      ${dr_name}
    Submit Form and Check Success
    
Validate Provider Info
    Scroll Element Into View    ${view_update_rest_of_the_case_info}
    JS Click    ${view_update_rest_of_the_case_info}
    ${name}   get element attribute    ${provider_name}     value
#    ${name}=    Get Text    ${provider_name}
    IF    "${name}" == "${dr_name}"
        Log To Console    Provider name already populated
    END

Enter fever greater than 100
    [Arguments]     ${selection}
    IF    "${selection}" == "No"
        Run Keyword And Ignore Error    JS Click    ${fever_greater_than_100_clear}
        JS Click    ${fever_greater_than_100_no}
    ELSE
        Run Keyword And Ignore Error    JS Click    ${fever_greater_than_100_clear}
        JS Click    ${fever_greater_than_100_yes}
        Wait Until Element Is Visible    ${highest_temp_field}
        Input Text    ${highest_temp_field}    103
    END

Enter any other symptoms
    [Arguments]     ${selection}
    IF    "${selection}" == "No"
        Run Keyword And Ignore Error    JS Click    ${any_other_symptoms_clear}
        JS Click    ${any_other_symptoms_no}
    ELSE
        Run Keyword And Ignore Error    JS Click    ${any_other_symptoms_clear}
        JS Click    ${any_other_symptoms_yes}
    END

Symptoms improving and then no
    Sleep    3s
    Wait Until Element Is Visible    ${are_symptoms_improving}
    Element Should Be Visible    ${are_symptoms_improving}
    Element Should Be Visible    ${had_following_symptoms}
    JS Click    ${are_symptoms_improving_yes}
    Scroll Element Into View    ${case_details_section}
    Sleep    5s
    Page Should Contain Element    ${message_on_no_warning_signs}
    JS Click    ${are_symptoms_improving_clear}
    Sleep    2s
    JS Click    ${are_symptoms_improving_no}
    Wait Until Element Is Visible    ${emergency_warning_signs}
    JS Click    ${emergency_warning_signs_none}
    Wait Until Element Is Visible    ${message_on_no_warning_signs}
    Page Should Contain Element    ${message_on_no_warning_signs}
    JS Click    ${emergency_warning_signs_none}
    JS Click    ${emergency_warning_signs_value}
    Wait Until Element Is Visible    ${message_on_warning_signs}
    Page Should Contain Element    ${message_on_warning_signs}


Enter any needs
    [Arguments]     ${selection}
    IF    "${selection}" == "No"
        Run Keyword And Ignore Error    JS Click    ${help_for_isolation_clear}
        JS Click    ${help_for_isolation_no}
    ELSE
        Run Keyword And Ignore Error    JS Click    ${help_for_isolation_clear}
        JS Click    ${help_for_isolation_yes}
        Wait Until Element Is Visible    ${help_needed_field}
        Input Text    ${help_needed_field}      ${help_needed_text}
    END


Verify fever, symptoms, help all no logs
    Scroll Element Into View    ${daily_monitoring_section}
    JS Click    ${view_follow_up_logs}
    Page Should Contain Element     ${verify_attempt}
    Page Should Contain Element     ${verify_fever_temp}\[contains(text(),'')]
    Page Should Contain Element     ${verify_fever}\[contains(text(),'no')]
    Page Should Contain Element     ${verify_needs}\[contains(text(),'')]
    Page Should Contain Element     ${verify_other_symptoms}\[contains(text(),'no')]


Verify fever, symptoms, help all logs
    Scroll Element Into View    ${daily_monitoring_section}
    JS Click    ${view_follow_up_logs}
    Page Should Contain Element     ${verify_attempt}
    Page Should Contain Element     ${verify_fever_temp}\[contains(text(),'103')]
    Page Should Contain Element     ${verify_fever}\[contains(text(),'yes')]
    Page Should Contain Element     ${verify_needs}\[contains(text(),'${help_needed_text}')]
    Page Should Contain Element     ${verify_other_symptoms}\[contains(text(),'yes')]
    Page Should Contain Element     ${symptoms_improving_log}\[contains(text(),'no')]
    Page Should Contain Element     ${warning_sign_log}\[contains(text(),'yes')]


Verify unsuccessful logs
    [Arguments]     ${log}
    Scroll Element Into View    ${daily_monitoring_section}
    JS Click    ${view_follow_up_logs}
    Page Should Contain Element     ${verify_unsuccess_attempt}
    Page Should Contain Element     ${verify_notes}\[contains(text(),'${log}')]
    