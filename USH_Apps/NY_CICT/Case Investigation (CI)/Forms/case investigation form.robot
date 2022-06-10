*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot
Resource    ../../Case Investigation (CI)/Forms/hub cases.robot


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
@{living_situation_option}      'Group Home for'    'Other Adult Group'     'All Shelters'      'Jails'       'Temporary'
@{living_option_health}      'Long-term Care Facility'    'Post Acute Care'     'Care Inpatient'
@{workplace_option_health}      'Healthcare facility'    'Long-term care'     'Other care'
@{workplace_option_student}     'Daycare'      'College'


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
   
Simple Form Fill up
   Wait Until Element Is Enabled    ${no_attempts_made_disposition}
   JS Click    ${no_attempts_made_disposition}
   Add User Details
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

Enter Symptoms improving
    [Arguments]     ${selection}
    Wait Until Element Is Visible    ${are_symptoms_improving}
    Element Should Be Visible    ${are_symptoms_improving}
    IF    "${selection}" == "No"
        JS Click    ${are_symptoms_improving_no}
        Wait Until Element Is Visible    ${emergency_warning_signs}
        JS Click    ${emergency_warning_signs_none}
        Wait Until Element Is Visible    ${message_on_no_warning_signs}
        Page Should Contain Element    ${message_on_no_warning_signs}
        JS Click    ${emergency_warning_signs_none}
    ELSE
        JS Click    ${are_symptoms_improving_yes}
    END
    Sleep    3s

    JS Click    ${are_symptoms_improving_yes}


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

Fill up PUI Category for Positive test
    Wait Until Element Is Visible    ${pui_category}
    JS Click    ${symptomatic_individual}
    JS Click    ${able_to_schedule_appointment}
    ${Yesterday's date}    Yesterday's Date
    Input Text    ${test_scheduled_date}    ${Yesterday's date}
    JS Click    ${test_scheduled_date}
    Wait Until Element Is Visible    ${have_you_been_tested_yes}
    JS Click    ${have_you_been_tested_yes}
    Wait Until Element Is Visible    ${do_you_have_results_yes}
    JS Click    ${do_you_have_results_yes}
    Wait Until Element Is Visible    ${results_are_positive}
    JS Click    ${results_are_positive}
    Wait Until Element Is Visible    ${message_quarantine_1}
    Page Should Contain Element    ${message_quarantine_1}
    Page Should Contain Element    ${message_quarantine_2}
    Enter fever greater than 100    Yes
    Enter any other symptoms    Yes
    Enter Symptoms improving    Yes
    Enter any needs    No
    Submit Form and Check Success


Fill up PUI Category for Negative test
    Wait Until Element Is Visible    ${pui_category}
    JS Click    ${subjected_to_quarantine}
    JS Click    ${able_to_schedule_appointment}
    ${Yesterday's date}    Yesterday's Date
    Input Text    ${test_scheduled_date}    ${Yesterday's date}
    JS Click    ${test_scheduled_date}
    Wait Until Element Is Visible    ${have_you_been_tested_yes}
    JS Click    ${have_you_been_tested_yes}
    Wait Until Element Is Visible    ${do_you_have_results_yes}
    JS Click    ${do_you_have_results_yes}
    Wait Until Element Is Visible    ${results_are_negative}
    JS Click    ${results_are_negative}
    Wait Until Element Is Visible    ${message_quarantine_2}
    Page Should Contain Element    ${message_quarantine_2}
    Enter fever greater than 100    Yes
    Enter any other symptoms    No
    Enter any needs    No
    Submit Form and Check Success


Verify results received
    [Arguments]  ${case_name}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[10][normalize-space()='Received Results']

Get specimen collection date
    ${string}=      Get Text    ${verify_specimen_collection}
    ${str}=       String.Split String    ${string}    :
    ${str}=     String.Strip String    ${str}[1]
    [Return]     ${str}

Add Case Disposition
    Wait Until Element Is Enabled    ${no_attempts_made_disposition}
    JS Click    ${no_attempts_made_disposition}

Add Cluster Information To Case
    [Arguments]     ${cluster1_name}    ${cluster1_id}      ${cluster2_name}    ${cluster2_id}
    Scroll Element Into View    ${cluster_section}
    JS Click    ${case_part_of_cluster_yes}
    Wait Until Element Is Visible    ${how_many_cluster}
    Select From List By Label    ${how_many_cluster}    2
    Wait Until Element Is Visible    ${cluster_1}
    Select From List By Label    ${cluster_1}    ${cluster1_name}
    Wait Until Page Contains    ${cluster1_id}
    Page Should Contain    ${cluster1_id}
    Wait Until Element Is Visible    ${cluster_2}
    Select From List By Label    ${cluster_2}    ${cluster2_name}
    Wait Until Page Contains    ${cluster2_id}
    Page Should Contain    ${cluster2_id}
    Submit Form and Check Success

Fill up Healthcare section
    Wait Until Element Is Visible    ${occupation_section}
    Scroll Element Into View    ${occupation_section}
    Select Healthcare, verify Hub Section
    Unselect Healthcare, verify Hub Section
    JS Click    ${went_to_work}
    Scroll Element Into View    ${workplace_setting_type_section}
    Validate Workplace Setting Type Healthcare Hub
    JS Click    ${went_to_work}
    Verify Hub Section      No
    JS Click    ${visited_healthcare_facility}
    Verify Hub Section      Yes
    JS Click    ${visited_healthcare_facility}
    Verify Hub Section      No
    JS Click    ${visited_long_term_care}
    Verify Hub Section      Yes
    JS Click    ${visited_long_term_care}
    Verify Hub Section      No
    Sleep    5s
    Scroll Element Into View    ${adult_congregate_living_facility}
    JS Click    ${adult_congregate_living_facility}
    Verify Hub Section      Yes
    JS Click    ${adult_congregate_living_facility}
    Verify Hub Section      No
    Validate Living Situation Healthcare Hub
    Select Healthcare, verify Hub Section
    Submit Form and Check Success

Fill up Congregate section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${living_situation_section}
    Validate Living Situation Congregate
    JS Click    ${correctional_worker}
    Verify Congregate Section      Yes
    JS Click    ${correctional_worker}
    Verify Congregate Section      No
    Scroll Element Into View    ${exposures_section}
    Scroll Element Into View    ${did_you_visit_adult_congregate}
    JS Click    ${did_you_visit_adult_congregate}
    Verify Congregate Section      Yes
    JS Click    ${did_you_visit_adult_congregate}
    Verify Congregate Section      No
    JS Click    ${did_you_visit_correctional}
    Verify Congregate Section      Yes
    JS Click    ${did_you_visit_correctional}
    Verify Congregate Section      No
    JS Click    ${did_you_visit_adult_congregate}
    Verify Congregate Section      Yes
    Submit Form and Check Success

Fill up Cluster section
    Wait Until Element Is Visible    ${case_part_of_cluster_yes}
    Scroll Element Into View    ${case_part_of_cluster_yes}
    JS Click    ${case_part_of_cluster_no}
    Verify Cluster Hub Section      No
    JS Click    ${case_part_of_cluster_yes}
    Verify Cluster Hub Section      Yes
    Submit Form and Check Success

Fill up CSS section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${living_situation_section}
    JS Click    ${living_situation_unsheltered}
    Verify CSS Hub Section      Yes
    JS Click    ${living_situation_clear}
    Verify CSS Hub Section      No
#    JS Click    ${are_you_able_to_isolate_no}
#    Verify CSS Hub Section      Yes
#    JS Click    ${are_you_able_to_isolate_clear}
#    JS Click    ${are_you_able_to_isolate_yes}
#    Verify CSS Hub Section      No
#    JS Click    ${bathroom_only_used_by_patient_no}
#    Verify CSS Hub Section      Yes
#    JS Click    ${bathroom_only_used_by_patient_clear}
#    JS Click    ${bathroom_only_used_by_patient_yes}
#    Verify CSS Hub Section      No
    JS Click    ${need_additional_help_with_food_yes}
    Verify CSS Hub Section      Yes
    JS Click    ${need_additional_help_with_food_clear}
    JS Click    ${need_additional_help_with_food_no}
    Verify CSS Hub Section      No
    JS Click    ${living_situation_unsheltered}
    Verify CSS Hub Section      Yes
    Submit Form and Check Success

Fill up School section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${living_situation_student}
    JS Click    ${living_situation_student}
    Verify Student Hub Section      Yes
    JS Click    ${living_situation_clear}
    Verify Student Hub Section    No
    JS Click    ${occupation_child_care}
    Verify Student Hub Section      Yes
    JS Click    ${occupation_child_care}
    Verify Student Hub Section      No
    JS Click    ${occupation_school}
    Verify Student Hub Section      Yes
    JS Click    ${occupation_school}
    Verify Student Hub Section      No
    JS Click    ${went_to_work}
    Validate Workplace Setting Type School Hub
    JS Click    ${went_to_work}
    Scroll Element Into View    ${exposures_section}
    JS Click    ${visited_school}
    Verify Student Hub Section      Yes
    JS Click    ${visited_school}
    Verify Student Hub Section      No
    JS Click    ${contact_with_covid_patient_yes}
    JS Click    ${contact_at_daycare}
    Verify Student Hub Section      Yes
    JS Click    ${contact_at_daycare}
    Verify Student Hub Section      No
    JS Click    ${contact_at_daycare}
    Verify Student Hub Section      Yes
    ${school}       ${date}=    Fill up school detail section
    Update School Hub Status    In Progress
    [Return]    ${school}   ${date}

Fill up school detail section
     Scroll Element Into View    ${student_details_section}
     JS Click    ${type_of_school_prek}
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_school}    ${past_date}
     Wait Until Element Is Visible    ${is_case_a_school}
     JS Click    ${is_case_a_school}
     Wait Until Element Is Visible    ${school_name}
     Select From List By Index    ${school_name}       2
     ${school}=     Get Selected List Label    ${school_name}
     [Return]   ${school}   ${past_date}

Enter value for other School
     Scroll Element Into View    ${student_details_section}
     ${isNotSelected}=     Run Keyword And Return Status    Checkbox Should Not Be Selected    ${type_of_school_prek}
     IF    ${isNotSelected}
          JS Click    ${type_of_school_prek}
     END
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_school}    ${past_date}
     Wait Until Element Is Visible    ${is_case_a_school}
     JS Click    ${is_case_a_school}
     Wait Until Element Is Visible    ${school_name}
     Select From List By Label    ${school_name}    Other
     ${alpha_num}=     Generate Random String	4	[NUMBERS]abcdef
     ${name}=      Set Variable      school test ${past_date} ${alpha_num} name
     Input Text    ${school_other_name}    ${name}
     ${Mobile number}    Generate Mobile Number
     Input Text       ${school_other_phone}     ${Mobile number}
     ${address}=     Set Variable        school test ${past_date} ${alpha_num} address
     Input Text    ${school_other_address}    ${address}
     ${phone}    Get Text    ${school_other_phone_value}
     [Return]    ${name}     ${address}      ${phone}        ${past_date}

Enter value for other College
     Scroll Element Into View    ${student_details_section}
     ${isNotSelected}=     Run Keyword And Return Status    Checkbox Should Not Be Selected    ${type_of_college}
     IF    ${isNotSelected}
          JS Click    ${type_of_college}
     END
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_college}    ${past_date}
     Wait Until Element Is Visible    ${is_case_a_college}
     JS Click    ${is_case_a_college}
     Wait Until Element Is Visible    ${college_name}
     Select From List By Index    ${college_name}       1
     ${alpha_num}=     Generate Random String	4	[NUMBERS]abcdef
     ${name}=      Set Variable      school test ${past_date} ${alpha_num} name
     Input Text    ${college_other_name}    ${name}
     ${Mobile number}    Generate Mobile Number
     Input Text       ${college_other_phone}     ${Mobile number}
     ${address}=     Set Variable        school test ${past_date} ${alpha_num} address
     Input Text    ${college_other_address}    ${address}
     ${phone}    Get Text    ${college_other_phone_value}
     [Return]    ${name}     ${address}      ${phone}        ${past_date}


Fill up college detail section
     Scroll Element Into View    ${student_details_section}
     JS Click    ${type_of_college}
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_college}    ${past_date}
     Wait Until Element Is Visible    ${is_case_a_college}
     JS Click    ${is_case_a_college}
     Wait Until Element Is Visible    ${college_name}
     Select From List By Index    ${college_name}       2
     ${college}=     Get Selected List Label    ${college_name}
     [Return]   ${college}   ${past_date}

Enter Information in School College Details section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${living_situation_student}
    JS Click    ${living_situation_student}
    Verify Student Hub Section      Yes
    ${school}       ${school_date}=    Fill up school detail section
    ${college}       ${college_date}=    Fill up college detail section
    ${cc_name}     ${cc_address}      ${cc_phone}        ${cc_date}=    Fill up childcare detail section
    ${school_name}      ${school_address}       ${school_phone}=    Get school or college details      ${school}
    ${college_name}      ${college_address}       ${college_phone}=    Get school or college details      ${college}
    Verify School Details present in Hub section    ${school_name}      ${school_address}       ${school_phone}     ${school_date}
    Verify School Details present in Hub section    ${college_name}      ${college_address}       ${college_phone}     ${college_date}
    Verify School Details present in Hub section    ${cc_name}      ${cc_address}       ${cc_phone}     ${cc_date}
    ${otherschool_name}     ${otherschool_address}      ${otherschool_phone}        ${otherschool_date}=    Enter value for other School
    ${othercollege_name}     ${othercollege_address}      ${othercollege_phone}        ${othercollege_date}=    Enter value for other College
    Verify School Details present in Hub section    ${otherschool_name}     ${otherschool_address}      ${otherschool_phone}        ${otherschool_date}
    Verify School Details present in Hub section    ${othercollege_name}     ${othercollege_address}      ${othercollege_phone}        ${othercollege_date}
    Submit Form and Check Success

Get school or college details
    [Arguments]     ${school}
    ${string}=      String.Split String    ${school}    -
    ${name}     String.Strip String    ${string}[0]
    Page Should Contain Element    //p[.='${name}']
    ${value}=       Get Text    //p[.='${name}']/following-sibling::ul/li[contains(text(),'Address')]
    ${address}=      String.Split String    ${value}    :
    ${value}=       Get Text    //p[.='${name}']/following-sibling::ul/li[contains(text(),'Phone')]
    ${phone}=       String.Split String    ${value}    :
    [Return]        ${name}     ${address}[1]       ${phone}[1]

Fill up childcare detail section
    Scroll Element Into View    ${student_details_section}
    JS Click    ${type_of_childcare}
    Sleep    3s
    Scroll Element Into View    ${childcare_name}
    ${past_date}=      Past Date Generator    1
    ${alpha_num}=     Generate Random String	4	[NUMBERS]abcdef
    ${name}=      Set Variable      childcare test ${past_date} ${alpha_num} name
    Input Text    ${childcare_name}    ${name}
    ${Mobile number}    Generate Mobile Number
    Input Text       ${childcare_phone}     ${Mobile number}
    ${address}=     Set Variable        childcare test ${past_date} ${alpha_num} address
    Input Text    ${childcare_address}    ${address}
    ${phone}    Get Text    ${childcare_phone_value}
    Input Text    ${last_date_at_location_childcare}    ${past_date}
    JS Click    ${is_case_a_childcare}
    [Return]    ${name}     ${address}      ${phone}        ${past_date}


Select Healthcare, verify Hub Section
    JS Click    ${occupation_healthcare}
    Checkbox Should Be Selected    ${occupation_checkbox}\[@value='Healthcare Worker (HCW)']
    Verify Hub Section      Yes


Unselect Healthcare, verify Hub Section
    JS Click    ${occupation_healthcare}
    Checkbox Should Not Be Selected    ${occupation_checkbox}\[@value='Healthcare Worker (HCW)']
    Verify Hub Section      No

Verify Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${healthcare_hub_section}
        Page Should Contain Element    ${heathcare_facility_details_section}
    ELSE
        Page Should Not Contain    ${healthcare_hub_section}
        Page Should Not Contain    ${heathcare_facility_details_section}
    END

Verify Congregate Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${congregate_setting_hub_section}
    ELSE
        Page Should Not Contain    ${congregate_setting_hub_section}
    END

Verify Cluster Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${clusters_hub_section}
    ELSE
        Page Should Not Contain    ${clusters_hub_section}
    END

Verify CSS Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${css_section}
    ELSE
        Page Should Not Contain    ${css_section}
    END

Verify Student Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${student_hub_section}
        Page Should Contain Element    ${student_details_section}
    ELSE
        Page Should Not Contain    ${student_hub_section}
        Page Should Not Contain    ${student_details_section}
    END


Validate Living Situation Congregate
    Scroll Element Into View    ${living_situation_section}
    FOR    ${option}    IN    @{living_situation_option}
            JS Click    ${living_situation_selection}\[contains(text(),${option})]
            Sleep    3s
            Verify Congregate Section      Yes
    END
    JS Click    ${living_situation_selection}\[.='Other']
    Sleep    3s
    Verify Congregate Section      No

Validate Living Situation Healthcare Hub
    Scroll Element Into View    ${living_situation_section}
    FOR    ${option}    IN    @{living_option_health}
            JS Click    ${living_situation_selection}\[contains(text(),${option})]
            Sleep    3s
            Verify Hub Section      Yes
    END
    JS Click    ${living_situation_selection}\[.='Other']
    Sleep    3s
    Verify Hub Section      No


Validate Workplace Setting Type Healthcare Hub
    Scroll Element Into View    ${workplace_setting_type_section}
    FOR    ${option}    IN    @{workplace_option_health}
            JS Click    ${workplace_setting_type_selection}\[contains(text(),${option})]
            Sleep    3s
            Verify Hub Section      Yes
    END

Validate Workplace Setting Type School Hub
    Scroll Element Into View    ${workplace_setting_type_section}
    FOR    ${option}    IN    @{workplace_option_student}
            JS Click    ${workplace_setting_type_selection}\[contains(text(),${option})]
            Sleep    3s
            Verify Student Hub Section    Yes
    END

Verify School Details present in Hub section
    [Arguments]    ${name}      ${address}       ${phone}     ${date}
    ${name}     String.Strip String    ${name}
    ${address}     String.Strip String    ${address}
    ${phone}     String.Strip String    ${phone}
    Page Should Contain Element    //li[contains(text(),'School Name: ${name}')]
    Page Should Contain Element    //li[contains(text(),'School Address: ${address}')]
    Page Should Contain Element    //li[contains(text(),'School Phone Number: ${phone}')]
    Page Should Contain Element    //li[contains(text(),'Last date at this location: ${date}')]
    Page Should Contain Element    //li[contains(text(),'Case is a: Student')]
