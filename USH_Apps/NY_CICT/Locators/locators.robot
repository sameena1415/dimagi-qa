*** Settings ***
Resource    ../Utilities/user_inputs.robot


*** Variables ***

${username}    id:id_auth-username
${password}    id:id_auth-password
${submit_button}   (//button[@type="submit"])[last()]
${otp_token}    id:id_token-otp_token
${confirm_cookie}    css:#hs-eu-confirmation-button
${commcare hq title}    CommCare HQ
${webapps_menu}    css:#CloudcareTab > a
${login_as}    css:.js-restore-as-item
${ct_user}    //span[contains(., "CT")]
${ci_user}    //span[contains(., "CI")]
${ctsup_user}    (//span[contains(., "CT Sup")])[1]
${cisup_user}    (//span[contains(., "CI Sup")])[1]
${search_username}      //input[@placeholder='Filter workers']
${search_user_button}       //*[@class='fa fa-search']

${confirm_user_login}    //button[@id="js-confirmation-confirm"]

${select_app}    xpath://div[contains(@aria-label,"${app name}")]
${home_btn}     //*[@class="fa fa-home"]


${select_first case_in_caselist}    //tbody[@class='wrapper js-case-container']/tr[1]
${continue}    id:select-case
${register_new_contacts_form}    //h3[.='Register New Contact(s)']
#//tr[@aria-label="Register New Contact(s)"]
${contact_first_name}     xpath://span[text()='First name']/following::div[1]/div[@class='widget']/descendant::textarea
${contact_last_name}     xpath://span[text()='Last name']/following::div[1]/div[@class='widget']/descendant::textarea
${contact_phone_num}    xpath://span[text()='Phone number:']/following::div[1]/div[@class='widget']/descendant::input
${preferred_language}    //p[text()='English']
${last_contact_date}    //span[contains(text(),'When was the last day ')]/following::div[1]//input[@type='text']
${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']
${phone_no_not_matching}    //label[.//*[contains(text(),'phone number the same as the case')]]/following-sibling::div//*[.='No']

${app_home}    xpath://ol//li[contains(.,"${app name}")]

${search_case}    id:searchText
${search_button}    id:case-list-search-button    
${contact_monitoring_form}    xpath://tr[@aria-label="Contact Monitoring"]
${initial_interview_disposition}    //p[text()='Reached person, agreed to call']
${final_disposition2}    //p[text()='Reached, completed investigation']
${no_attempts_made_disposition}    //p[text()='No attempt made yet']
${follow_up_complete_disposition}       //p[text()='Follow up completed']
${symptom_fever}    //p[contains(.,'Fever')]
${symptom_chill}    //p[contains(.,'Chills')]
${symptom_fatigue}    //p[text()='Fatigue']
${symptom_congestion}    //p[text()='Congestion']
${symptom_runny_nose}    //p[text()='Runny nose']
${date_of_symptomp_onset}    //label[.//span[contains(text(),'date of onset')]]/following-sibling::div//input[contains(@id,'date')]
${gender}    //p[text()='Female']
${race}    //p[text()='Asian']
${ethnicity}    //p[text()='Hispanic/Latino']
${yes_convert_pui}    //p[text()='Yes, convert contact/traveler to PUI']
${enter_case_dob}     //p[text()="Enter the case's Date of Birth"]
${date_of_birth}        //*[text()='Date of birth']/following::div[1]/div[@class='widget']/descendant::input
${no_convert_pui}    //p[contains(.,'No, do NOT convert')]
${pui_form_header}    //h1[text()='Convert Contact to a Suspected Case (PUI)' and @class='title']
${confirm_yes_convert_pui}    //p[text()='Yes']
${confirm_no_convert_pui}    //p[text()='No']
${covert_to_pui_form}    //tr[@aria-label='Convert Contact to a Suspected Case (PUI)']


${webapps_home}    //a[@href="/a/${domain}/cloudcare/apps/v2/" and @class="navbar-brand"]
${check_in_menu}   (//div[@aria-label='Check In']/div)[1] 
${search all cases}    //button[text()='Search All Cases']
${case search submit}    //button[@id='query-submit-button']
${change pui status form}    //tr[@aria-label='Change PUI Status']
${convert_back_to_contact}    //p[contains(.,'Convert this Suspected Case back to being a Contact')]
${are_you_sure}    //p[text()='Yes, convert this Suspected Case back into a Contact']
${close_record}    //p[text()="Yes"]
${dont_close_record}    //p[text()="No"]
${do_you_want_to_close_record}     //label[.//*[.='Do you want to close this record?']]/self::label
${convert_this_suspected_case}    //p[contains(.,'Yes, convert this Suspected Case back into a Contact')]
${no_longer_active_message}    //strong[text()="This Suspected Case's contact record is no longer active, so you may not choose to convert it back to a contact."]
${no_longer_active_message2}       //p[contains(.,'This Suspected Case (PUI) will be converted back to being a contact. The Contact Tracing team will resume monitoring of this patient.')]
${close_yes_message}    //p[text()="The Suspected Case (PUI) will be closed, as will the associated contact record."]
${close_yes_message2}    //strong[text()="In order for the contact to be monitored again, the Contact Tracing team must re-open their record."]
${close_no_message}    //p[text()="This Suspected Case (PUI) will be converted back to being a contact. The Contact Tracing team will resume monitoring of this patient."]
${close_no_message2}    //strong[text()="To undo this action, a Contact Tracer will need to convert the Contact back into a PUI"]
${final_disposition}    //p[text()='Follow up completed']
${ send the release from quarantine notice by mail question}    //span[text()='Do you want to send the release from quarantine notice by mail?']
${date_notice_sent}    //span[text()='Date notice was sent by mail']
${send quarantine mail no}    //span[text()='Do you want to send the release from quarantine notice by mail?']/following::p[text()='No']
${send quarantine mail yes}    //span[text()='Do you want to send the release from quarantine notice by mail?']/following::p[text()='Yes']
${no notice label}    //span[text()="No notice will be sent"]

${like to send mail no}    //span[text()='Would you like to send the quarantine release notice by email?']/following::p[text()='No']
${like to send mail yes}    //span[text()='Would you like to send the quarantine release notice by email?']/following::p[text()='Yes']
${what_address}    xpath:(//span[text()='What email address should the notice be sent to']/following::textarea)[1]
${email_input}    test@test.in
${mail_label}    xpath://p/strong[text() = '${email_input}']


${archieved_contact}    //td[text()='${archieved_contact_name}']

${sync}    xpath://div[@class='js-sync-item appicon appicon-sync']
${sync success}    xpath:(//div[text()='User Data successfully synced.'])[last()]
${first-name_case_search}    xpath:(//td/div[contains(., "First Name")]/following::input)[1]

${specimen_collection_date}   //span[contains(text(),'Specimen Collection Date')]/following::div[1]//input[@type='text']
${lab_result_positive}      //input[@value='Positive']
${accession_number}     //span[contains(text(),'Accession Number')]/following::div[1]//textarea[1]

${suspected_to_confirmed_case}      //input[@value='Convert this Suspected Case to a **Confirmed Case**']
${confirm_suspected_to_confirmed_case}      //p[text()='Yes, convert this Suspected Case into a Confirmed Case']

${selected_patient_is_duplicate}    //p[text()='The selected patient is a duplicate of the current patient']
${keep_current_close_selected}      //input[@value='Keep the **Current Patient** and close the **Selected Patient**']

${lab_result_tab}       //a[text()='Lab Results' and @role='tab']
${list_is_empty_message}        //*[text()='List is empty.']
${lab_result_tab_positive}  //tr[.//td[text()='positive']]
${close_dialog}     //div//a[text()='Lab Results']/preceding::div[@class='modal-header']/button[@class='close']

${interview_info_section}       //div[@class='collapsible-icon-container']/following-sibling::span[text()='Interview Info']
${daily_monitoring_section}     //*[text()='Daily Follow Up Monitoring']
${status_section}     //*[text()='Status']
${view_update_rest_of_the_case_info}        //*[.='Case Details']/following::span[./p/strong]/preceding-sibling::input
${case_details_section}     //*[text()="Case Details"]
${view_all_notes}       //p[.='View all notes']
${view_follow_up_logs}      //p[.='View Follow Up Log']
${add_new_note}     //p[.='Add a new note']
${add_new_follow_up_log}     //p[.='Record a new Follow Up Attempt']
${follow_up_attempt_success}     //label[.//span[.='Follow Up Attempt Result']]/following-sibling::div//p[.='Successful']
${follow_up_attempt_unsuccess}     //label[.//span[.='Follow Up Attempt Result']]/following-sibling::div//p[.='Unsuccessful']
${add_new_note_field}       //label[.//span[.='Add a new note']]/following-sibling::div//textarea
${add_follow_up_log_field}      //label[.//span[.='Follow Up Attempt Notes']]/following-sibling::div//textarea
${patient_notes}        //h1[.='Patient Notes']

${fever_greater_than_100_no}    //label[.//span[contains(text(),'had a fever of greater than 100 degrees')]]/following-sibling::div//p[.='No']
${fever_reducing_medication_no}     //label[.//span[contains(text(),'used fever-reducing medication')]]/following-sibling::div//p[.='No']
${any_other_symptoms_no}    //label[.//span[contains(text(),'Do you have any other symptoms')]]/following-sibling::div//p[.='No']
${two_negative_results_no}     //label[.//span[contains(text(),'two negative results taken 24 hours apart')]]/following-sibling::div//p[.='No']
${help_for_isolation_no}    //label[.//span[contains(text(),'help with food, or any of your medical, mental health or other social service')]]/following-sibling::div//p[.='No']
${fever_greater_than_100_yes}    //label[.//span[contains(text(),'had a fever of greater than 100 degrees')]]/following-sibling::div//p[.='Yes']
${fever_reducing_medication_yes}     //label[.//span[contains(text(),'used fever-reducing medication')]]/following-sibling::div//p[.='Yes']
${any_other_symptoms_yes}    //label[.//span[contains(text(),'Do you have any other symptoms')]]/following-sibling::div//p[.='Yes']
${two_negative_results_yes}     //label[.//span[contains(text(),'two negative results taken 24 hours apart')]]/following-sibling::div//p[.='Yes']
${help_for_isolation_yes}    //label[.//span[contains(text(),'help with food, or any of your medical, mental health or other social service')]]/following-sibling::div//p[.='Yes']
${fever_greater_than_100_clear}    //label[.//span[contains(text(),'had a fever of greater than 100 degrees')]]/following-sibling::div//button
${fever_reducing_medication_clear}     //label[.//span[contains(text(),'used fever-reducing medication')]]/following-sibling::div//button
${any_other_symptoms_clear}    //label[.//span[contains(text(),'Do you have any other symptoms')]]/following-sibling::div//button
${two_negative_results_clear}     //label[.//span[contains(text(),'two negative results taken 24 hours apart')]]/following-sibling::div//button
${help_for_isolation_clear}    //label[.//span[contains(text(),'help with food, or any of your medical, mental health or other social service')]]/following-sibling::div//button
${highest_temp_field}       //label[.//span[contains(text(),'What was your highest temperature in the last 24 hours?')]]/following-sibling::div//input
${had_following_symptoms}       //p[text()='Have you had any of the following symptoms?']
${are_symptoms_improving}       //*[text()='Are the symptoms improving']
${are_symptoms_improving_no}       //label[.//*[text()='Are the symptoms improving']]/following-sibling::div//p[.='No']
${are_symptoms_improving_yes}       //label[.//*[text()='Are the symptoms improving']]/following-sibling::div//p[.='Yes']
${are_symptoms_improving_clear}       //label[.//*[text()='Are the symptoms improving']]/following-sibling::div//button
${help_needed_field}        //label[.//span[contains(text(),'Please describe the help needed')]]/following-sibling::div//textarea
${help_needed_text}     help needed
${emergency_warning_signs}      //*[contains(text(),'Are you experiencing any emergency warning signs such as')]
${emergency_warning_signs_none}     //label[.//*[contains(text(),'Are you experiencing any emergency warning signs such as')]]/following-sibling::div//p[.='None']
${emergency_warning_signs_value}     //label[.//*[contains(text(),'Are you experiencing any emergency warning signs such as')]]/following-sibling::div//p[.='New confusion']
${message_on_no_warning_signs}        //strong[contains(text(),'so glad to hear that') and contains(text(),'we went over some of the things you might need during isolation and some of the ways we can help you')]
${message_on_warning_signs}     //strong[contains(text(),'Encourage the case to call 9-1-1') and contains(text(),'remind them to tell the operator that they have been diagnosed')]

${verify_attempt}   //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[contains(text(),'Successful')][./strong[text()='Attempt Status:']]
${verify_unsuccess_attempt}   //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[contains(text(),'Unsuccessful')][./strong[text()='Attempt Status:']]
${verify_fever}     //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Fever:']]
${verify_fever_temp}       //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Fever Temp:']]
${verify_other_symptoms}    //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Other Symptoms:']]
${verify_needs}     //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='New Needs:']]
${verify_notes}     //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Notes:']]
${symptoms_improving_log}    //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Symptoms Improving:']]
${warning_sign_log}    //div[.//*[.='Daily Follow Up Monitoring']]/following::div//p[./strong[text()='Emergency Warning Signs:']]

${provider_section}     //*[.='Provider Info']
${provider_name}        //span[text()='Provider Name']/following::div[1]/div[@class='widget']/descendant::textarea
${dr_name}      Doctor Nick