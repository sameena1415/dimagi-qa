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
${Q:Needs Daily Monitoring}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]
${Q:Needs Daily Monitoring A: No}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]/following-sibling::div//p[text()='No']
${Q:Needs Daily Monitoring A: Yes}    //label[.//span[contains(.,'Does the case need daily monitoring?')]]/following-sibling::div//label//input[@value='Yes']
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
   Submit Form and Check Success

Daily Monitoring - Yes
    Open Case Investigation Form
    Wait Until Element Is Visible    ${interview_info_section}
    ${IsElementPresent}=     Element Should Be Visible    ${interview_info_section}
    IF    ${IsElementPresent}
       Log To Console    Interview Information section is present
    END
    Scroll Element Into View    ${Q:Needs Daily Monitoring A: No}
    JS Click    ${Q:Needs Daily Monitoring A: Yes}

#    ${IsElementPresent}=    Element Should Not Be Visible    ${daily_monitoring_section}
#    Sleep    2s
#    IF    not ${IsElementPresent}
#       Log To Console    Daily Monitoring section is not present
#    END
#    Sleep    10s
#    Wait for condition  return window.document.readyState === 'complete'
##    Sleep    10s
#    Wait Until Element Is Enabled    ${Q: Willing to receive survey via SMS A: No}
#    Scroll Element Into View    ${Q: Willing to receive survey via SMS}
##    ${IsElementPresent}=    Element Should Be Visible    ${Q: Willing to receive survey via SMS}
##    Log To Console    ${IsElementPresent}
#    Wait Until Element Is Visible    ${Q: Willing to receive survey via SMS A: No}
#    Click Element    ${Q: Willing to receive survey via SMS A: No}
#    Element Should Not Be Visible    ${daily_monitoring_section}
#    Submit Form and Check Success

Verify Daily Monitoring Status
    [Arguments]  ${case_name}      ${daily_monitoring_status}
    Wait Until Element Is Visible    //tr[.//td[text()='${case_name}']]
    Element Should Be Visible    //tr[.//td[text()='${case_name}']]/self::tr//td[8][normalize-space()='${daily_monitoring_status}']

Verify Daily Monitoring Section
    Open Case Investigation Form
    Wait Until Element Is Visible    ${submit_form}
    Element Should Be Visible    ${daily_monitoring_section}
    Element Should Be Visible    ${view_update_rest_of_the_case_info}
    Element Should Not Be Visible    ${interview_info_section}
