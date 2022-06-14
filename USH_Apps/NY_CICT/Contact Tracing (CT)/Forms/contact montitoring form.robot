*** Settings ***
Library  SeleniumLibrary
Resource    ../../Base/base.robot
Resource    ../../Contact Tracing (CT)/Forms/hub contacts.robot


*** Variables ***
${Q:Interview Disposition A:Attempted for two days and unable to reach}    //p[text()='Attempted for two days and unable to reach']
${Q:Home/Cell Phone}    //span[text()='Home/Cell Phone']/following::div[1]/div[@class='widget']/descendant::input

${Q:Search For Address}    //span[text()='Search for Address']/following::div[1]/div[@class='widget']/descendant::input
${Address}     South Side River Bourgeois Road, Subdivision A, Nova Scotia B0E 2X0, Canada
${Fisrt address}    //li[contains(.,'South Side')]

${Q:County of residence}    (//*[contains(text(),'County')])[1]/following::span[@title='Please choose an item'][1]
${A:County of residence}    //label[.//*[contains(text(),'County')]]/following-sibling::div//select
${Country success}    (//*[contains(text(),'County')])[1]/following::i[@class="fa fa-check text-success"][1]

${Q:State}    //span[text()='State']/following::span[@title='Please choose an item'][1]
${A:State}    //label[.//span[.='State']]/following-sibling::div//select
${State_Value}    (//span[text()='State']/following::span//following::span[1])[2]
${State success}    //span[text()='State']/following::i[@class="fa fa-check text-success"][1]

${Q:Zipcode_error}     (//label[.//*[contains(text(),'Zip Code')]]/following-sibling::div//textarea[contains(@data-bind,'value: $data.rawAnswer')])[1]
${Q:Zipcode_normal}     (//label[.//*[contains(text(),'Zip')]]/following-sibling::div//textarea)[1]
${Zipcode success}    (//label[.//*[contains(text(),'Zip Code')]]/following-sibling::div//i[@class="fa fa-check text-success"])[1]
${Zipcode failure}    (//label[.//*[contains(text(),'Zip Code')]]/following-sibling::div//i[@class="fa fa-warning text-danger clickable"])[1]

${Q:Transer Patient A:No}  //p[contains(.,'No, do not transfer')]
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


${Street}   (//label[.//*[contains(text(),'Street')]]/following-sibling::div//textarea)[1]
${City}   (//label[.//*[contains(text(),'City')]]/following-sibling::div//textarea)[1]
${Street_input}     test street
${City_input}     test city
${Zip_input}     11111
${permanent_address}    //p[contains(text(),'permanent address')]/following-sibling::p
@{contact_living_situation_option}      'Group Home for'    'Other Adult Group'     'All Shelters'      'Jails'       'Temporary'
@{contact_living_option_health}      'Long-term Care Facility'    'Post Acute Care'     'Care Inpatient'    'Assisted Living'


*** Keywords *** 

Open Contact Monitoring Form
    Click Element    ${contact_monitoring_form}
    

Convert contact to PUI using CM form
        Open All Contacts Unassigned & Open menu
        ${contact_name}    Get Contact Name
        ${contact_created}   Set Contact Name
        Search in the case list    ${contact_name}
        Select Created Case    ${contact_created}
        Click Element    ${contact_monitoring_form}
        JS Click    ${initial_interview_disposition}
        JS Click    ${race}
        JS Click    ${ethnicity}
        JS Click    ${gender}
        JS Click    ${symptom_congestion}
        JS Click    ${symptom_fatigue}
        JS Click    ${symptom_fever}
        JS Click    ${symptom_runny_nose} 
#        JS Click    ${date_of_symptomp_onset}
        ${Yesterday's date}    Yesterday's Date
        Input Text    ${date_of_symptomp_onset}   ${Yesterday's date}
        JS Click    ${date_of_symptomp_onset}
        JS Click    ${Q:Convert Contact A:Yes}
        Submit Form and Check Success

Unable to reach (CM) 
   JS Click    ${Q:Interview Disposition A:Attempted for two days and unable to reach}
   ${Mobile number}    Generate Mobile Number
   Input Text       ${Q:Home/Cell Phone}     ${Mobile number}
   Add Address
   Submit Form and Check Success 
   

Add Address
   # Select Address
   Run Keyword And Ignore Error    Input Text    ${Q:Search For Address}   ${Address}
   Click Element    ${Fisrt address}
   Sleep    15s
   # Country
   Select Dropdown   ${Q:County of residence}    ${A:County of residence}

   # Zipcode
   Scroll Element Into View    ${Q:Zipcode_normal}
   Wait Until Element Is Visible    ${Zipcode failure}    80s
   Wait Until Element Is Enabled   ${Q:Zipcode_error}
   Clear Element Text    ${Q:Zipcode_error}
   Press Keys   ${Q:Zipcode_normal}   12345     TAB
   Wait Until Element Is Visible    ${Zipcode success}     30s
  
   # State
   Select Dropdown    ${Q:State}    ${A:State}
   
   # Do not Transfer
   JS Click    ${Q:Transer Patient A: No}

Change Address
   Input Text    ${Street}    ${Street_input}
   Input Text    ${City}    ${City_input}
   Scroll Element Into View    ${Q:Zipcode_normal}
   Input Text    ${Q:Zipcode_normal}    ${Zip_input}
   # State
   Scroll Element Into View     ${A:State}
   Select From List By Index    ${A:State}  ${37}


Verify Address
    [Arguments]     ${address}=${EMPTY}
    ${permanent_address}    Get Text    ${permanent_address}
    IF  "${address}"!="${EMPTY}"
        Should Contain  ${permanent_address}  ${Street_input}
        Should Contain  ${permanent_address}  ${City_input}
        Should Contain  ${permanent_address}  ${Zip_input}
        Should Contain  ${permanent_address}  NY
    ELSE
        Should Not Contain  ${permanent_address}  ${Street_input}
        Should Not Contain  ${permanent_address}  ${City_input}
        Should Not Contain  ${permanent_address}  ${Zip_input}
    END

Reached and Agreed to Call (CM)   
   JS Click    ${Q:Interview Disposition A:Reached person, agreed to call}
   JS Click    ${Q:Gender A:Female}
   JS Click    ${Q:Race A:Asian}
   JS Click    ${Q:Ethnicity A:Hispanic/Latino}
   JS Click    ${Q:Transer Patient A: No}
   Submit Form and Check Success 
    
Requires Follow-up (CM)
     JS Click    ${symptom_fever}
     JS Click    ${symptom_chill}
     JS Click    ${date_of_symptomp_onset}
     ${Yesterday's date}    Yesterday's Date
     Input Text    ${date_of_symptomp_onset}   ${Yesterday's date}
     JS Click    ${date_of_symptomp_onset}
     JS Click    ${no_convert_pui}
     JS Click    ${Q:Transer Patient A: No}
     Submit Form and Check Success
      
Receive SMS (CM)
    JS Click    ${Q:Initial interview complete A: Yes}
    JS Click    ${Q: Willing to receive SMS A: Yes} 
    JS Click    ${Q: Number confirm A: Yes}  
    JS Click    ${no_convert_pui}
    JS Click    ${Q:Transer Patient A: No}
    Submit Form and Check Success 
    
    
Partial Interview Complete (CM)
    JS Click    ${View/Update the rest of the Contact's info}
    JS Click    ${Q:Initial interview complete A: No}
    JS Click    ${no_convert_pui}
    JS Click    ${Q:Transer Patient A: No}
    Submit Form and Check Success 
    
Interview Complete (CM)
    JS Click    ${Q:Initial interview disposition A: Refused} 
    JS Click    ${Q:Initial interview complete A: Yes}    
    Sleep    5s
    JS Click    ${no_convert_pui}    
    Sleep    5s
    Submit Form and Check Success 

Add Contact Monitoring Details
    Wait Until Element Is Enabled    ${Q:Interview Disposition A:Reached person, agreed to call}
    JS Click    ${Q:Interview Disposition A:Reached person, agreed to call}
    JS Click    ${Q:Gender A:Female}
    JS Click    ${Q:Race A:Asian}
    JS Click    ${Q:Ethnicity A:Hispanic/Latino}
    ${Past date}    Past Date Generator     2
    Input Text    ${last_date_of_contact_with_confirmed_case}   ${Past date}

Add Cluster Information To Contact
    [Arguments]     ${cluster1_name}    ${cluster1_id}
    Scroll Element Into View    ${cluster_section}
    JS Click    ${contact_part_of_cluster_yes}
    Wait Until Element Is Visible    ${how_many_cluster}
    Select From List By Label    ${how_many_cluster}    1
    Wait Until Element Is Visible    ${cluster_1}
    Select From List By Label    ${cluster_1}    ${cluster1_name}
    Wait Until Page Contains    ${cluster1_id}
    Page Should Contain    ${cluster1_id}
    Submit Form and Check Success

Contact Fill up Healthcare section
    Wait Until Element Is Visible    ${occupation_section}
    Scroll Element Into View    ${occupation_section}
    Select Healthcare, verify Hub Section
    Unselect Healthcare, verify Hub Section
    JS Click    ${contact_attended_health_care}
    Verify Hub Section Contacts      Yes
    JS Click    ${type_of_contact_clear}
    Verify Hub Section Contacts      No
    JS Click    ${contact_attended_nursing}
    Verify Hub Section Contacts      Yes
    JS Click    ${type_of_contact_clear}
    Verify Hub Section Contacts      No
    Validate Contact Living Situation Healthcare Hub
    Select Healthcare, verify Hub Section
    JS Click    ${no_attempts_made_disposition}
    Submit Form and Check Success

Select Healthcare, verify Hub Section
    JS Click    ${occupation_healthcare}
    Checkbox Should Be Selected    ${occupation_checkbox}\[@value='Healthcare Worker (HCW)']
    Verify Hub Section Contacts      Yes

Unselect Healthcare, verify Hub Section
    JS Click    ${occupation_healthcare}
    Checkbox Should Not Be Selected    ${occupation_checkbox}\[@value='Healthcare Worker (HCW)']
    Verify Hub Section Contacts      No

Validate Contact Living Situation Healthcare Hub
    Scroll Element Into View    ${living_situation_section}
    FOR    ${option}    IN    @{contact_living_option_health}
            JS Click    ${contact_living_situation}\[contains(text(),${option})]
            Sleep    3s
            Verify Hub Section Contacts      Yes
    END
    JS Click    ${contact_living_situation}\[.='Other']
    Sleep    3s
    Verify Hub Section Contacts      No


Verify Hub Section Contacts
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${healthcare_hub_section}
        Page Should Contain Element    ${heathcare_facility_details_section}
    ELSE
        Page Should Not Contain    ${healthcare_hub_section}
        Page Should Not Contain    ${heathcare_facility_details_section}
    END

Contacts Fill up Congregate section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${living_situation_section}
    Validate Contact Living Situation Congregate
    JS Click    ${correctional_worker}
    Verify Congregate Section Contacts      Yes
    JS Click    ${correctional_worker}
    Verify Congregate Section Contacts      No
    Scroll Element Into View    ${exposures_section}
    JS Click    ${multi_family_dwelling}
    Verify Congregate Section Contacts      Yes
    JS Click    ${multi_family_dwelling}
    Verify Congregate Section Contacts      No
    JS Click    ${correctional_worker}
    Verify Congregate Section Contacts      Yes
    JS Click    ${no_attempts_made_disposition}
    Submit Form and Check Success

Validate Contact Living Situation Congregate
    Scroll Element Into View    ${living_situation_section}
    FOR    ${option}    IN    @{contact_living_situation_option}
            JS Click    ${contact_living_situation}\[contains(text(),${option})]
            Sleep    3s
            Verify Congregate Section Contacts      Yes
    END
    JS Click    ${contact_living_situation}\[.='Other']
    Sleep    3s
    Verify Congregate Section Contacts      No

Verify Congregate Section Contacts
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${congregate_setting_hub_section}
    ELSE
        Page Should Not Contain    ${congregate_setting_hub_section}
    END

Contacts Fill up Cluster section
    Wait Until Element Is Visible    ${contact_part_of_cluster_yes}
    Scroll Element Into View    ${contact_part_of_cluster_yes}
    JS Click    ${contact_part_of_cluster_no}
    Verify Contacts Cluster Hub Section      No
    JS Click    ${contact_part_of_cluster_yes}
    Verify Contacts Cluster Hub Section      Yes
    JS Click    ${no_attempts_made_disposition}
    Submit Form and Check Success
    
Verify Contacts Cluster Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${clusters_hub_section}
    ELSE
        Page Should Not Contain    ${clusters_hub_section}
    END
    
Contacts Fill up School section
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${contact_living_situation_student}
    JS Click    ${contact_living_situation_student}
    Verify Contacts Student Hub Section      Yes
    JS Click    ${contact_living_situation_clear}
    Verify Contacts Student Hub Section    No
    JS Click    ${occupation_child_care}
    Verify Contacts Student Hub Section      Yes
    JS Click    ${occupation_child_care}
    Verify Contacts Student Hub Section      No
    JS Click    ${occupation_school}
    Verify Contacts Student Hub Section      Yes
    JS Click    ${occupation_school}
    Verify Contacts Student Hub Section      No
    Scroll Element Into View    ${exposures_section}
    JS Click    ${contact_at_daycare}
    Verify Contacts Student Hub Section      Yes
    JS Click    ${contact_at_daycare}
    Verify Contacts Student Hub Section      No
    JS Click    ${no_attempts_made_disposition}
    JS Click    ${contact_at_daycare}
    Verify Contacts Student Hub Section      Yes
    ${school}       ${date}     ${end_date}=    Fill up school detail section Contacts
    Update School Hub Status Contacts    In Progress
    [Return]    ${school}   ${date}     ${end_date}

Fill up school detail section Contacts
     Scroll Element Into View    ${student_details_section}
     JS Click    ${type_of_school_prek}
     ${past_date}=      Past Date Generator    1
     ${end_date}=       Future Date Generator    4
     Input Text    ${last_date_at_location_school}    ${past_date}
     Wait Until Element Is Visible    ${is_contact_a_school}
     JS Click    ${is_contact_a_school}
     Wait Until Element Is Visible    ${school_name}
     Select From List By Index    ${school_name}       2
     ${school}=     Get Selected List Label    ${school_name}
     [Return]   ${school}   ${past_date}    ${end_date}

Enter value for other School Contacts
     Scroll Element Into View    ${student_details_section}
     ${isNotSelected}=     Run Keyword And Return Status    Checkbox Should Not Be Selected    ${type_of_school_prek}
     IF    ${isNotSelected}
          JS Click    ${type_of_school_prek}
     END
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_school}    ${past_date}
     Wait Until Element Is Visible    ${is_contact_a_school}
     JS Click    ${is_contact_a_school}
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

Enter value for other College Contacts
     Scroll Element Into View    ${student_details_section}
     ${isNotSelected}=     Run Keyword And Return Status    Checkbox Should Not Be Selected    ${type_of_college}
     IF    ${isNotSelected}
          JS Click    ${type_of_college}
     END
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_college}    ${past_date}
     Wait Until Element Is Visible    ${is_contact_a_college}
     JS Click    ${is_contact_a_college}
     Wait Until Element Is Visible    ${college_name}
     Select From List By Index    ${college_name}       1
     ${alpha_num}=     Generate Random String	4	[NUMBERS]abcdef
     ${name}=      Set Variable      college test ${past_date} ${alpha_num} name
     Input Text    ${college_other_name_contact}    ${name}
     ${Mobile number}    Generate Mobile Number
     Input Text       ${college_other_phone}     ${Mobile number}
     ${address}=     Set Variable        college test ${past_date} ${alpha_num} address
     Input Text    ${college_other_address}    ${address}
     ${phone}    Get Text    ${college_other_phone_value}
     [Return]    ${name}     ${address}      ${phone}        ${past_date}


Fill up college detail section Contacts
     Scroll Element Into View    ${student_details_section}
     JS Click    ${type_of_college}
     ${past_date}=      Past Date Generator    1
     Input Text    ${last_date_at_location_college}    ${past_date}
     Wait Until Element Is Visible    ${is_contact_a_college}
     JS Click    ${is_contact_a_college}
     Wait Until Element Is Visible    ${college_name}
     Select From List By Index    ${college_name}       2
     ${college}=     Get Selected List Label    ${college_name}
     [Return]   ${college}   ${past_date}

Enter Information in School College Details section Contacts
    Wait Until Element Is Visible    ${living_situation_section}
    Scroll Element Into View    ${contact_living_situation_student}
    JS Click    ${contact_living_situation_student}
    Verify Contacts Student Hub Section      Yes
    ${school}       ${school_date}      ${end_date}=    Fill up school detail section Contacts
    ${college}       ${college_date}=    Fill up college detail section Contacts
    ${cc_name}     ${cc_address}      ${cc_phone}        ${cc_date}=    Fill up childcare detail section Contacts
    ${school_name}      ${school_address}       ${school_phone}=    Get school or college details Contacts      ${school}
    ${college_name}      ${college_address}       ${college_phone}=    Get school or college details Contacts      ${college}
    Verify School Details present in Contacts Hub section    ${school_name}      ${school_address}       ${school_phone}     ${school_date}
    Verify School Details present in Contacts Hub section    ${college_name}      ${college_address}       ${college_phone}     ${college_date}
    Verify School Details present in Contacts Hub section    ${cc_name}      ${cc_address}       ${cc_phone}     ${cc_date}
    ${otherschool_name}     ${otherschool_address}      ${otherschool_phone}        ${otherschool_date}=    Enter value for other School Contacts
    ${othercollege_name}     ${othercollege_address}      ${othercollege_phone}        ${othercollege_date}=    Enter value for other College Contacts
    Verify School Details present in Contacts Hub section    ${otherschool_name}     ${otherschool_address}      ${otherschool_phone}        ${otherschool_date}
    Verify School Details present in Contacts Hub section    ${othercollege_name}     ${othercollege_address}      ${othercollege_phone}        ${othercollege_date}
    JS Click    ${no_attempts_made_disposition}
    Submit Form and Check Success

Get school or college details Contacts
    [Arguments]     ${school}
    ${string}=      String.Split String    ${school}    -
    ${name}     String.Strip String    ${string}[0]
    Page Should Contain Element    //p[.='${name}']
    ${value}=       Get Text    //p[.='${name}']/following-sibling::ul/li[contains(text(),'Address')]
    ${address}=      String.Split String    ${value}    :
    ${value}=       Get Text    //p[.='${name}']/following-sibling::ul/li[contains(text(),'Phone')]
    ${phone}=       String.Split String    ${value}    :
    [Return]        ${name}     ${address}[1]       ${phone}[1]

Fill up childcare detail section Contacts
    Scroll Element Into View    ${student_details_section}
    JS Click    ${type_of_childcare}
    Sleep    3s
    Scroll Element Into View    ${childcare_name}
    ${past_date}=      Past Date Generator    1
    ${alpha_num}=     Generate Random String	4	[NUMBERS]abcdef
    ${Mobile number}    Generate Mobile Number
    Input Text       ${childcare_phone}     ${Mobile number}
    ${address}=     Set Variable        childcare test ${past_date} ${alpha_num} address
    Input Text    ${childcare_address}    ${address}
    ${name}=      Set Variable      childcare test ${past_date} ${alpha_num} name
    Input Text    ${childcare_name}    ${name}
    Input Text    ${last_date_at_location_childcare}    ${past_date}
    JS Click    ${is_contact_a_childcare}
#    ${phone}    Get Text    ${childcare_phone_value}
     ${phone}=      Format Phone number    ${Mobile number}
    [Return]    ${name}     ${address}      ${phone}        ${past_date}

Format Phone number
    [Arguments]     ${phone}
#    ${phone}=   Set Variable    4091724500
    ${str1}     Get Substring    ${phone}      0    3
    ${str2}     Get Substring    ${phone}      3    6
    ${str3}     Get Substring    ${phone}      -4
    ${new_number}=      Set Variable        (${str1}) ${str2}-${str3}
    Log To Console    ${new_number}
    [Return]        ${new_number}

Verify Contacts Student Hub Section
    [Arguments]     ${yes_no}
    IF    "${yes_no}" == "Yes"
        Page Should Contain Element    ${student_hub_section}
        Page Should Contain Element    ${student_details_section}
    ELSE
        Page Should Not Contain    ${student_hub_section}
        Page Should Not Contain    ${student_details_section}
    END

Verify School Details present in Contacts Hub section
    [Arguments]    ${name}      ${address}       ${phone}     ${date}
    ${name}     String.Strip String    ${name}
    ${address}     String.Strip String    ${address}
    ${phone}     String.Strip String    ${phone}
    Page Should Contain Element    //li[contains(text(),'School Name: ${name}')]
    Run Keyword And Ignore Error    Page Should Contain Element    //li[contains(text(),'${address}')]
    Run Keyword And Ignore Error    Page Should Contain Element    //li[contains(text(),'School Address: ${address}')]
    Page Should Contain Element    //li[contains(text(),'School Phone Number: ${phone}')]
    Page Should Contain Element    //li[contains(text(),'Last date at this location: ${date}')]
    Page Should Contain Element    //li[contains(text(),'Contact is a: Student')]

Validate Contacts Workplace Setting Type School Hub
    Scroll Element Into View    ${workplace_setting_type_section}
    FOR    ${option}    IN    @{workplace_option_student}
            JS Click    ${workplace_setting_type_selection}\[contains(text(),${option})]
            Sleep    3s
            Verify Contacts Student Hub Section    Yes
    END
