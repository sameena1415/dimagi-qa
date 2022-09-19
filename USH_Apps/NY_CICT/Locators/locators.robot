*** Settings ***
Resource    ../Utilities/user_inputs.robot


*** Variables ***

## User HQ Login ##

${username}    id:id_auth-username
${password}    id:id_auth-password
${submit_button}   (//button[@type="submit"])[last()]
${otp_token}    id:id_token-otp_token
${confirm_cookie}    css:#hs-eu-confirmation-button
${commcare hq title}    CommCare HQ

## Webapps Login  ##

${webapps_menu}    css:#CloudcareTab > a
${login_as}    css:.js-restore-as-item
${ct_user}    //span[contains(., "CT")]
${ci_user}    //span[contains(., "CI")]
${ctsup_user}    (//span[contains(., "CT Sup")])[1]
${cisup_user}    (//span[contains(., "CI Sup")])[1]
${search_username}      //input[@placeholder='Filter workers']
${search_user_button}       //*[@class='fa fa-search']
${confirm_user_login}    //button[@id='js-confirmation-confirm']
${select_app}    xpath://div[contains(@aria-label,"${app name}")]
${home_btn}     //*[@class="fa fa-home"]
${app_home}    xpath://ol//li[contains(.,"${app name}")]
${webapps_home}    //a[@href="/a/${domain}/cloudcare/apps/v2/" and @class="navbar-brand"]
${check_in_menu}   (//div[@aria-label='Check In']/div)[1]

## Sync App ##

${sync}    xpath://div[@class='js-sync-item appicon appicon-sync']
${sync success}    xpath:(//div[text()='User Data successfully synced.'])[last()]
${first-name_case_search}    xpath:(//td/div[contains(., "First Name")]/following::input)[1]

## Case Search ##
${first-name_case_search}    xpath:(//td/div[contains(., "First Name")]/following::input)[1]
${last-name_case_search}    xpath:(//td/div[contains(., "Last Name")]/following::input)[1]
${search all cases in the list}    //button[contains(., 'Search All')]

## Register New Contact(s) Form

${register_new_contacts_form}    //h3[.='Register New Contact(s)']
${how_many_new_contacts}     //span[contains(text(),'contacts do you want to record?')]/following::div[1]/div[@class='widget']/descendant::input
${close_contacts_header}    //h1[text()='Close Contacts']
#${contact_date_selection_success}   (//*[contains(text(),'had contact')])[1]/following::i[@class="fa fa-check text-success"][1]
${another_process_error}    //*[contains(text(),'Another process')][1]
# Type of Contacts
${type_of_contact_household}      //p[contains(text(),'Household')]
${type_of_contact_international_traveller}      //p[contains(text(),'International Travel')]
${arrival_date_in_us}   (//span[contains(text(),'Arrival date')]/following::div[1]//input[@type='text'])
${calendar_close}   //a[@data-action='close']
${type_of_contact_visitor_traveling}    //p[contains(text(),'visitor traveling from a')]
${Date_last_impacted_states}   (//span[contains(text(),' impacted states')]/following::div[1]//input[@type='text'])
${state_traveled_from}  //span[text()='State traveled from']/following::span[@title='Please choose an item'][1]
${state_traveled_from_select}   //label[.//*[contains(.,'State travel')]]/following-sibling::div//select
${transportation_airline}   //span[contains(text(), 'transportation')]/following::input[@value='Airline']
${airline}  (//span[text()='Airline']/following::div[1]/div[@class='widget']/descendant::textarea)
${date_of_flight}    (//span[contains(text(),' flight')]/following::div[1]//input[@type='text'])
${type_of_contact_ooj_case}      //p[contains(text(),'OOJ case')]
${contact_details_contact_type}  (//strong[contains(text(),'Type of Contact')]//ancestor::li)
${contact_details_exposure date}  (//strong[contains(text(),'Travel Date')]//ancestor::li)
##
${contact_id}   (//strong[contains(text(),'Contact ID')]//ancestor::p)
${contact_id_without_index}   (//h2[contains(text(),'ID')])
${contact_first_name}     (//span[text()='First name']/following::div[1]/div[@class='widget']/descendant::textarea)
${contact_last_name}     (//span[text()='Last name']/following::div[1]/div[@class='widget']/descendant::textarea)
${contact_phone_num}    (//span[text()='Phone number:']/following::div[1]/div[@class='widget']/descendant::input)
${phone_no_not_matching}    (//label[.//*[contains(text(),'phone number the same as the case')]]/following-sibling::div//*[.='No'])
${preferred_language}    (//p[text()='English'])
${last_contact_date}    (//span[contains(text(),'When was the last day ')]/following::div[1]//input[@type='text'])
${email_id}  (//span[contains(text(),'mail')]/following::div[1]/div[@class='widget']/descendant::textarea)
${address_same_yes}     (//p[contains(text(), 'address the same as the case')]/following::p[text()='Yes'][1])
${address_same_no}     (//p[contains(text(), 'address the same as the case')]/following::p[text()='No'][1])
${address_value}     (//p[contains(text(), 'address the same as the case')]/following::strong[1])
${number_same}     (//p[contains(text(), 'number the same as the case')]/following::p[text()='No'][1])
${add_note}    (//span[text()='Add a note']/following::div[1]/div[@class='widget']/descendant::textarea)
${symptomatic_yes}     (//span[contains(text(), 'Symptomatic')]/following::p[text()='Yes'][1])

${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']

# Already registered contacts
${already_registered_label}      (//h1[contains(text(), 'Already Registered Contacts')])
${already_registered_contact_name}       (//h1[contains(text(), 'Already Registered Contacts')]/following::strong[contains(text(),'Contact Name')]//ancestor::p[1])
${already_registered_most_recent_note}       (//h1[contains(text(), 'Already Registered Contacts')]/following::strong[contains(text(),'Recent Note')]//following::p[1])

## Contact Monitoring ##
${contact_info_contact_name}       (//h1[contains(text(), 'Contact Info')]/following::strong[contains(text(),'Name')]//ancestor::li[1])[1]
${contact_info_email}       (//h1[contains(text(), 'Contact Info')]/following::strong[contains(text(),'Email')]//ancestor::li[1])[1]
${contact_info_language}       (//h1[contains(text(), 'Contact Info')]/following::strong[contains(text(),'Language')]//ancestor::li[1])[1]
${contact_info_last_exposure}       (//h1[contains(text(), 'Contact Info')]/following::strong[contains(text(),'Last Exposure')]//ancestor::li[1])[1]
${contact_info_phone_num}       (//h1[contains(text(), 'Contact Info')]/following::strong[contains(text(),'Phone Number')]//ancestor::li[1])[1]

## Case Investigation  ##
${Case Investigation Form}    //tr[@aria-label='Case Investigation']
${select_first case_in_caselist}    //tbody[@class='wrapper js-case-container']/tr[1]
${continue}    //button[contains(text(),'Continue')]
${search_case}    id:searchText
${search_button}    id:case-list-search-button
${contact_monitoring_form}    //tr[@aria-label='Contact Monitoring']
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

## Convert Contact to a Suspected Case PUI Form ##

${covert_to_pui_form}    //tr[@aria-label='Convert Contact to a Suspected Case (PUI)']
${Convert Contact to a Suspected Case PUI Form}    //tr[@aria-label='Convert Contact to a Suspected Case (PUI)']
${yes_convert_pui}    //p[text()='Yes, convert contact/traveler to PUI']
${enter_case_dob}     //p[text()="Enter the case's Date of Birth"]
${date_of_birth}        //*[text()='Date of birth']/following::div[1]/div[@class='widget']/descendant::input
${no_convert_pui}    //p[contains(.,'No, do NOT convert')]
${pui_form_header}    //h1[text()='Convert Contact to a Suspected Case (PUI)' and @class='title']
${confirm_yes_convert_pui}    //p[text()='Yes']
${confirm_no_convert_pui}    //p[text()='No']
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

${specimen_collection_date}   //span[contains(text(),'Specimen Collection Date')]/following::div[1]//input[@type='text']
${lab_result_positive}      //input[@value='Positive']
${accession_number}     //span[contains(text(),'Accession Number')]/following::div[1]//textarea[1]

${suspected_to_confirmed_case}      //input[@value='Convert this Suspected Case to a **Confirmed Case**']
${confirm_suspected_to_confirmed_case}      //p[text()='Yes, convert this Suspected Case into a Confirmed Case']

${selected_patient_is_duplicate}    //p[text()='The selected patient is a duplicate of the current patient']
${keep_current_close_selected}      //input[@value='Keep the **Current Patient** and close the **Selected Patient**']

## View/Record Lab Result Form ##
${View Record Lab results}    //tr[@aria-label='View / Record Lab Results']
${lab_result_tab}       //a[text()='Lab Results' and @role='tab']
${list_is_empty_message}        //*[text()='List is empty.']
${lab_result_tab_positive}  //tr[.//td[text()='positive']]
${close_dialog}     //div//a[text()='Lab Results']/preceding::div[@class='modal-header']/button[@class='close']

## Daily Monitoring Form ##
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

${pui_category}     //label//*[contains(text(),'PUI Category')]
${symptomatic_individual}       //label[.//*[contains(text(),'PUI Category')]]/following-sibling::div//p[.='Symptomatic individual']
${subjected_to_quarantine}       //label[.//*[contains(text(),'PUI Category')]]/following-sibling::div//p[.='Individual who is subject to precautionary or mandatory quarantine']
${able_to_schedule_appointment}     //label[.//*[text()='Were you able to schedule an appointment to be tested?']]/following-sibling::div//p[.='Yes']
${test_scheduled_date}      //label[.//*[text()='When is your test scheduled for?']]/following-sibling::div//input
${have_you_been_tested_yes}     //label[.//*[text()='Have you been tested?']]/following-sibling::div//p[.='Yes']
${have_you_been_tested_no}     //label[.//*[text()='Have you been tested?']]/following-sibling::div//p[.='No']
${do_you_have_results_yes}     //label[.//*[text()='Do you have your results?']]/following-sibling::div//p[.='Yes']
${results_are_positive}     //label[.//*[text()='What are your results?']]/following-sibling::div//p[.='Positive']
${results_are_negative}     //label[.//*[text()='What are your results?']]/following-sibling::div//p[.='Negative']
${message_quarantine_1}     //*[contains(text(),'You are now considered to be a confirmed case and need to isolate for 10 days from the time your symptoms started')]
${message_quarantine_2}     //*[contains(text(),'Once you have confirmed these results in CommCare or ECLRS')][./strong[contains(text(),'Change PUI Status')]]


## Clusters and Hub ##
${cluster_name_field}     //label[.//*[.='Cluster Name']]/following-sibling::div//textarea
${cluster_investigation}       //label[.//*[.='Cluster Type']]/following-sibling::div//p[.='Investigation']
${cluster_outbreak}     //label[.//*[.='Cluster Type']]/following-sibling::div//p[.='Outbreak']
${cluster_mass_testing}     //label[.//*[.='Cluster Type']]/following-sibling::div//p[.='Mass Testing']
${cluster_setting_childcare}    //label[.//*[.='Cluster Setting']]/following-sibling::div//p[.='Childcare']
${cluster_setting_school}       //label[.//*[.='Cluster Setting']]/following-sibling::div//p[.='School (PreK-12)']
${cluster_shelter}       //label[.//*[.='Cluster Setting']]/following-sibling::div//p[.='Shelter']
${clutter_college}      //label[.//*[.='Cluster Setting']]/following-sibling::div//p[contains(text(),'College')]
${description_of_cluster}       //label[.//*[.='Description of the cluster']]/following-sibling::div//textarea
${cluster_site_info}        //*[.='Cluster Site Info']
${cluster_site_name}        //label[.//*[.='Site Name']]/following-sibling::div//textarea
${cluster_phone}        //label[.//*[.='Site Main Phone Number']]/following-sibling::div//input
${cluster_street_address}       //label[.//*[.='Street Address']]/following-sibling::div//textarea
${cluster_city}     //label[.//*[.='City']]/following-sibling::div//textarea
${cluster_state}    //label[.//*[.='State']]/following-sibling::div//select
${cluster_zip}      //label[.//*[.='Zip Code']]/following-sibling::div//textarea
${cluster_site_contact_person}      //label[.//*[.='Site Contact Person Name']]/following-sibling::div//textarea
${cluster_site_contact_person_title}    //label[.//*[.='Site Contact Person Title']]/following-sibling::div//textarea
${cluster_number_of_individuals_on_site}        //label[.//*[.='Number of Individuals on Site']]/following-sibling::div//input
${cluster_id}       //*[contains(text(),'New Cluster ID:')]
${cluster_select_school}    //label[.//*[.='Select school or university']]/following-sibling::div//select

${verify_specimen_collection}       //strong[text()='Specimen Collection Date:']/parent::li
${cluster_section}      //*[.='Clusters']
${clusters_hub_section}      //*[.='Clusters Hub']
${case_part_of_cluster_yes}       //label[.//*[.='Is this case part of a cluster?']]/following-sibling::div//p[.='Yes']
${case_part_of_cluster_no}       //label[.//*[.='Is this case part of a cluster?']]/following-sibling::div//p[.='No']
${how_many_cluster}     //label[.//*[.='How many clusters?']]/following-sibling::div//select
${cluster_1}        //fieldset[.//*[.='Cluster 1']]/following-sibling::div//label[.//*[.='Select the cluster']]/following-sibling::div//select
${cluster_2}        //fieldset[.//*[.='Cluster 2']]/following-sibling::div//label[.//*[.='Select the cluster']]/following-sibling::div//select
${specimen_date_of_first_case}      //span[contains(text(),'Specimen Collection Date of First Positive Case:')]

${last_date_of_contact_with_confirmed_case}        //label[.//*[text()='Last date of contact with the confirmed case:']]//following-sibling::div//input
${contact_part_of_cluster_yes}       //label[.//*[.='Is this contact/traveler part of an Cluster?']]/following-sibling::div//p[.='Yes']
${contact_part_of_cluster_no}       //label[.//*[.='Is this contact/traveler part of an Cluster?']]/following-sibling::div//p[.='No']
${close_cluster_section}        //*[.='Close Cluster']
${close_cluster_yes}        //label[.//*[.='Do you want to close the cluster?']]/following-sibling::div//p[.='Yes']
${cluster_closure_reason}       //label[.//*[.='Select the reason for closing the cluster:']]/following-sibling::div//p[.='Outbreak ended']
${reopen_cluster_section}        //*[.='Reopen Cluster']
${reopen_cluster_yes}        //label[.//*[.='Are you sure you want to reopen the cluster?']]/following-sibling::div//p[.='Yes, reopen this Cluster']
${cluster_closure_registered_in_error}       //label[.//*[.='Select the reason for closing the cluster:']]/following-sibling::div//p[.='Registered in error']

${occupation_section}       //span[.='Occupation']
${occupation_checkbox}      xpath://label[.//*[.='Occupation']]/following-sibling::div//input[@type='checkbox']
${occupation_healthcare}        //label[.//*[.='Occupation']]/following-sibling::div//p[.='Healthcare Worker (HCW)']
${occupation_correlational_worker}      //label[.//*[.='Occupation']]/following-sibling::div//p[.='Correctional worker']
${occupation_child_care}        //label[.//*[.='Occupation']]/following-sibling::div//p[.='Child care']
${occupation_school}        //label[.//*[.='Occupation']]/following-sibling::div//p[contains(text(),'School')]
${healthcare_hub_section}       //span[.='Health Care Hub']
${heathcare_facility_details_section}       //span[.='Healthcare Facility Details']
${living_situation_section}     //span[.='Living Situation']
${contact_living_situation}     //label[.//*[.='How would they describe their living situation?']]/following-sibling::div//p
${living_situation_selection}       //label[.//*[.='How would you describe their living situation?']]/following-sibling::div//p
${living_situation_unsheltered}     //label[.//*[.='How would you describe their living situation?']]/following-sibling::div//p[contains(text(),'Unsheltered')]
${living_situation_student}     //label[.//*[.='How would you describe their living situation?']]/following-sibling::div//p[contains(text(),'Student Housing')]
${contact_living_situation_student}     //label[.//*[.='How would they describe their living situation?']]/following-sibling::div//p[contains(text(),'Student Housing')]
${living_situation_clear}     //label[.//*[.='How would you describe their living situation?']]/following-sibling::div//button
${contact_living_situation_clear}     //label[.//*[.='How would they describe their living situation?']]/following-sibling::div//button
${are_you_able_to_isolate_yes}      //label[.//*[contains(text(),'Are you able to isolate yourself at home')]]/following-sibling::div//p[.='Yes']
${are_you_able_to_isolate_no}      //label[.//*[contains(text(),'Are you able to isolate yourself at home')]]/following-sibling::div//p[.='No']
${are_you_able_to_isolate_clear}      //label[.//*[contains(text(),'Are you able to isolate yourself at home')]]/following-sibling::div//button
${bathroom_only_used_by_patient_no}        //label[.//*[contains(text(),'Is there a private bathroom that could be used by only the patient')]]/following-sibling::div//p[.='No']
${bathroom_only_used_by_patient_yes}        //label[.//*[contains(text(),'Is there a private bathroom that could be used by only the patient')]]/following-sibling::div//p[.='Yes']
${bathroom_only_used_by_patient_clear}        //label[.//*[contains(text(),'Is there a private bathroom that could be used by only the patient')]]/following-sibling::div//button
${need_additional_help_with_food_no}        //label[.//*[contains(text(),'Do you need any additional help with food or any other medical')]]/following-sibling::div//p[.='No']
${need_additional_help_with_food_yes}        //label[.//*[contains(text(),'Do you need any additional help with food or any other medical')]]/following-sibling::div//p[.='Yes']
${need_additional_help_with_food_clear}        //label[.//*[contains(text(),'Do you need any additional help with food or any other medical')]]/following-sibling::div//button
${css_section}      //*[.='Community Support Specialist Hub']
${congregate_setting_hub_section}       //*[.='Congregate Settings Hub']
${activities_section}       //span[.='Activities']
${exposures_section}       //span[.='Exposures']
${went_to_work}     //p[.='Went to work']
${correctional_worker}     //p[.='Correctional worker']
${visited_healthcare_facility}     //p[.='Visited a healthcare facility']
${contact_attended_health_care}     //p[.='Health Care']
${contact_attended_nursing}     //p[.='Nursing / assisted living home']
${type_of_contact_clear}     //label[.//*[.='Type of Contact']]/following-sibling::div//button
${visited_long_term_care}     //p[.='Visited a long-term care or skilled nursing type of facility']
${visited_school}     //p[.='School / University / Childcare Center']
${adult_congregate_living_facility}     //p[.='Adult Congregate Living Facility']
${workplace_setting_type_section}       //label[.//span[.='Workplace Setting Type']]
${workplace_setting_type_selection}     //label[.//span[.='Workplace Setting Type']]/following-sibling::div//p
${hub_task_force_followup}     //*[contains(text(),'Hub/Task Force')]
${hub_status_selection}     //label[.//span[.='Hub Status']]/following-sibling::div//p
${congregate_hub_status_selection}      //fieldset//*[.='Congregate Settings Hub']/following::div//label[.//span[.='Hub Status']]/following-sibling::div//p
${cluster_hub_status_selection}     //label[.//span[.='Status']]/following-sibling::div//p
${did_you_visit_adult_congregate}      //div[.//*[.='Did you visit/attend a:']]/following-sibling::div//p[.='Adult Congregate Living Facility']
${did_you_visit_correctional}      //div[.//*[.='Did you visit/attend a:']]/following-sibling::div//p[.='Correctional Facility']
${multi_family_dwelling}    //label[.//*[contains(text(),'Describe your contact with the known')]]/following-sibling::div//p[contains(text(),'Multi-family')]
${student_hub_section}      //*[.='School Hub']
${student_details_section}      //*[.='Childcare/School/College/Summer Camp Details']
${contact_with_covid_patient_yes}       //label[.//*[.='In the past 14 days, have you been in contact with a COVID-19 Case?']]/following-sibling::div//p[.='Yes']
${contact_at_daycare}       //label[.//*[contains(text(),'Describe your contact')]]/following-sibling::div//p[.='At a daycare or school']
${type_of_school_prek}      //*[contains(text(),'Type of School')]/following::*[.='School (PreK - 12)']
${type_of_childcare}      //*[contains(text(),'Type of School')]/following::*[.='Childcare']
${type_of_college}      //*[contains(text(),'Type of School')]/following::p[contains(text(),'College')]
${is_case_a_school}        //fieldset[.//strong[contains(text(),'Info about PreK')]]/following-sibling::div//label[.//*[contains(text(),'Is case a')]]/following-sibling::div//p[.='Student']
${is_contact_a_school}        //fieldset[.//strong[contains(text(),'Info about PreK')]]/following-sibling::div//label[.//*[contains(text(),'Is contact a')]]/following-sibling::div//p[.='Student']
${school_name}      //label[.//*[.='Name of school']]/following-sibling::div//select
${is_case_a_college}        //fieldset[.//strong[contains(text(),'Info about University')]]/following-sibling::div//label[.//*[contains(text(),'Is case a')]]/following-sibling::div//p[.='Student']
${is_contact_a_college}        //fieldset[.//strong[contains(text(),'Info about University')]]/following-sibling::div//label[.//*[contains(text(),'Is contact a')]]/following-sibling::div//p[.='Student']
${college_name}      //label[.//*[.='Name of university/college']]/following-sibling::div//select
${last_date_at_location_school}      //fieldset[.//strong[contains(text(),'Info about PreK')]]/following-sibling::div//label[.//*[.='Last date at location']]/following-sibling::div//input
${last_date_at_location_college}      //fieldset[.//strong[contains(text(),'Info about University')]]/following-sibling::div//label[.//*[.='Last date at location']]/following-sibling::div//input
${school_hub_status_selection}     //label[.//span[contains(text(),'Status')]]/following-sibling::div//p
${is_case_a_childcare}        //fieldset[.//strong[contains(text(),'Info about Childcare')]]/following-sibling::div//label[.//*[contains(text(),'Is case a')]]/following-sibling::div//p[.='Student']
${is_contact_a_childcare}        //fieldset[.//strong[contains(text(),'Info about Childcare')]]/following-sibling::div//label[.//*[contains(text(),'Is contact a')]]/following-sibling::div//p[.='Student']
${college_name}      //label[.//*[.='Name of university/college']]/following-sibling::div//select
${last_date_at_location_childcare}      //fieldset[.//strong[contains(text(),'Info about Childcare')]]/following-sibling::div//label[.//*[.='Last date at location']]/following-sibling::div//input
${childcare_name}       //label[.//*[.='Name of childcare center']]/following-sibling::div//textarea
${childcare_address}    //label[.//*[.='Childcare center address']]/following-sibling::div//textarea
${childcare_phone}      //label[.//*[.='Childcare center phone number']]/following-sibling::div//input
${childcare_phone_value}    //*[contains(text(),'The childcare center phone number is saved as')]/strong
${school_other_name}       //label[.//*[.='Name of school']]/following-sibling::div//textarea
${school_other_address}    //label[.//*[.='School address']]/following-sibling::div//textarea
${school_other_phone}      //label[.//*[.='School phone number']]/following-sibling::div//input
${school_other_phone_value}     //*[contains(text(),'The school phone number is saved as')]/strong
${college_other_name}       //label[.//*[.='Name of university/college']]/following-sibling::div//textarea
${college_other_address}    //label[.//*[.='University/college address']]/following-sibling::div//textarea
${college_other_phone}      //label[.//*[.='University/college phone number']]/following-sibling::div//input
${college_other_phone_value}    //*[contains(text(),'The university/college phone number is saved as')]/strong
${college_other_name_contact}       //label[.//*[.='University/college Name']]/following-sibling::div//textarea
${college_other_phone_value}    //*[contains(text(),'The university/college phone number is saved as')]/strong

## Case Investigation Form ##

${Case Investigation Form}    //tr[@aria-label='Case Investigation']
${Q:Case Interview Disposition A:Reached person, agreed to call}    //p[text()='Reached person, agreed to call']
${Q:Case Interview Disposition A:Attempted for two days and unable to reach}    //p[text()='Attempted for two days and unable to reach']

${Q:Home/Cell Phone}    //span[text()='Home/Cell Phone']/following::div[1]/div[@class='widget']/descendant::input
${Q:Date Tested}    //p[text()='What date did you get tested?']/following::div[1]/div[@class='widget']/descendant::input
${Q:Preferred Language A:English}    //p[text()='English']
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
${Q:Ethnicity A:Non-Hispanic/Latino}    //p[contains(text(),'-Hispanic')]
@{living_situation_option}      'Group Home for'    'Other Adult Group'     'All Shelters'      'Jails'       'Temporary'
@{living_option_health}      'Long-term Care Facility'    'Post Acute Care'     'Care Inpatient'
@{workplace_option_health}      'Healthcare facility'    'Long-term care'     'Other care'
@{workplace_option_student}     'Daycare'      'College'
${menu container}   //*[@class='module-menu-container']
## Add Address ##

${Q:Search For Address}    //span[text()='Search for Address']/following::div[1]/div[@class='widget']/descendant::input
${Address}     South Side River Bourgeois Road, Subdivision A, Nova Scotia B0E 2X0, Canada
${Fisrt address}    //li[contains(.,'South Side')]
${Q:County of residence}    (//*[contains(text(),'County')])[1]/following::span[@title='Please choose an item'][1]
${A:County of residence}    //label[.//*[contains(text(),'County')]]/following-sibling::div//select
${Country success}    (//*[contains(text(),'County')])[1]/following::i[@class="fa fa-check text-success"][1]

${Q:State}    //span[text()='State']/following::span[@title='Please choose an item'][1]
${A:State}    //label[.//*[.='State']]/following-sibling::div//select
${State success}    //span[text()='State']/following::i[@class="fa fa-check text-success"][1]

${State_Value}    (//span[text()='State']/following::span//following::span[1])[2]
${Street}   (//label[.//*[contains(text(),'Street')]]/following-sibling::div//textarea)[1]
${City}   (//label[.//*[contains(text(),'City')]]/following-sibling::div//textarea)[1]
${Street_input}     test street
${City_input}     test city
${Zip_input}     11111

${Q:Zipcode_error}     (//label[.//*[contains(text(),'Zip Code')]]/following-sibling::div//textarea[contains(@data-bind,'value: $data.rawAnswer')])[1]
${Q:Zipcode_normal}     (//label[.//*[contains(text(),'Zip')]]/following-sibling::div//textarea)[1]
${Zipcode success}    (//label[.//*[contains(text(),'Zip Code')]]/following-sibling::div//i[@class="fa fa-check text-success"])[1]

## Close the Patient Record Form ##

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

## Register a New Case Form ##

${Create New Cluster Form}      //tr[@aria-label='Create New Cluster']
${View Update Cluster Info Form}      //tr[@aria-label='View/Update Cluster Info']

${Register a New Case}    (//div[@aria-label='Register a New Case']/div)[1]
${mpi_id_input}     //span[text()='DOH MPI ID']/following::div[1]/div[@class='widget']/descendant::textarea
${patient_first_name}     //span[text()='Patient First Name']/following::div[1]/div[@class='widget']/descendant::textarea
${patient_last_name}     //span[text()='Patient Last Name']/following::div[1]/div[@class='widget']/descendant::textarea


## Search for Duplicate Patients ##

${Search for Duplicate Patients}    //tr[@aria-label='Search for Duplicate Patients']
${search-first_name}    //input[@aria-label='First Name text entry']
${search-last_name}     //input[@aria-label='Last Name text entry']
${search-submit}        //button[@type='submit' and @id='query-submit-button']
${search-phone}     //input[@aria-label='Home Phone Number text entry"']
${Record New Result}    //button[text()='Record New Result']
${patient_first_name}     //span[text()='Patient First Name']/following::div[1]/div[@class='widget']/descendant::textarea
${patient_last_name}     //span[text()='Patient Last Name']/following::div[1]/div[@class='widget']/descendant::textarea

## Assign or Reassign Contacts Form ##

${Assign or Reassign Contact Form}    //tr[contains(@aria-label,'Assign or Re')]
${Permanently assign}    //p[contains(.,'Permanently assign')]
${Q:Permanently reassign to}    //span[contains(text(),'Permanently reassign')]/following::span[@title='Please choose an item'][1]
${A:Permanently reassign to ct}   //li[contains(.,'CT 1')]
${A:Permanently reassign to poc ct}   //li[contains(.,'CT')]
${A:Permanently unassign}    //p[contains(.,'from its current primary owner')]
${Submit Form}     //button[@type='submit' and @class='submit btn btn-primary']
${Success Message}    //p[text()='Form successfully saved!']

## Assign or Reassign Cases Form ##
${Assign or Reassign Case Form}    //tr[@aria-label='Assign or Reassign the Case']
${A:Permanently reassign to ci}   //li[contains(.,'CI 1')]
${A:Permanently reassign to poc ci}   //li[contains(.,'CI')]


## Contact Monitoring Form ##

${Q:Interview Disposition A:Attempted for two days and unable to reach}    //p[text()='Attempted for two days and unable to reach']
${Q:Home/Cell Phone}    //span[text()='Home/Cell Phone']/following::div[1]/div[@class='widget']/descendant::input
${Q:Convert Contact A:Yes}  //p[contains(.,'Yes, convert contact/traveler to PUI')]
${Q:Interview Disposition A:Reached person, agreed to call}    //p[text()='Reached person, agreed to call']
${Q:Gender A:Female}    //p[text()='Female']
${Q:Race A:Asian}    //p[text()='Asian']
${Q:Ethnicity A:Hispanic/Latino}    //p[text()='Hispanic/Latino']
${Q:Initial interview complete A: Yes}    //p[contains(.,'Yes, the interview is successfully complete')]
${Q: Willing to receive SMS A: Yes}     //span[contains(.,'receive a daily survey via SMS?')]/following::p[contains(.,'Yes')][1]
${Q: Number confirm A: Yes}    //span[contains(.,'would like to receive the SMS on?')]/following::p[contains(.,'Yes')][1]
${Q: Initial interview complete A: No}    //p[contains(.,'No, partial interview needing call back')]
${View/Update the rest of the Contact's info}    //label[contains(.,'View/Update')]
${Q:Initial interview disposition A: Refused}    //p[contains(.,'Reached person, refused to participate')]
${permanent_address}    //p[contains(text(),'permanent address')]/following-sibling::p
@{contact_living_situation_option}      'Group Home for'    'Other Adult Group'     'All Shelters'      'Jails'       'Temporary'
@{contact_living_option_health}      'Long-term Care Facility'    'Post Acute Care'     'Care Inpatient'    'Assisted Living'


## Close the Contact Record Form ##
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
