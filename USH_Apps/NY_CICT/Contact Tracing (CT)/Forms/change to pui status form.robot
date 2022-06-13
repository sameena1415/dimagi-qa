*** Settings ***
Library  SeleniumLibrary
Resource    ../../Base/base.robot

*** Variables ***
${Convert Contact to a Suspected Case PUI Form}    //tr[@aria-label='Convert Contact to a Suspected Case (PUI)']

*** Keywords ***
     
Open Convert Contact to a Suspected Case (PUI) Form
    Sleep    2s
    Wait Until Element Is Enabled    ${Convert Contact to a Suspected Case PUI Form}
    JS Click    ${Convert Contact to a Suspected Case PUI Form}


PUI form submission
    Wait Until Element Is Enabled    ${confirm_yes_convert_pui}
    JS Click    ${confirm_yes_convert_pui}
    Submit Form and Check Success

PUI form submission - No
    Wait Until Element Is Enabled    ${confirm_no_convert_pui}
    JS Click    ${confirm_no_convert_pui}
    Submit Form and Check Success

Search Archieved Case in All Suspected Cases (PUIs) menu
    Open All Suspected Cases (PUIs) menu
    Wait Until Element Is Enabled    ${search all cases}
    JS Click    ${search all cases}
    IF    '${archieved_contact_lname}' == '\'
        Input Text    ${first-name_case_search}    ${archieved_contact_name}
    ELSE
         Input Text    ${first-name_case_search}    ${archieved_contact_name}
         Input Text    ${last-name_case_search}    ${archieved_contact_lname}
    END
    Wait Until Element Is Enabled    ${case search submit}
    JS Click    ${case search submit}

Search Case in All Suspected Cases (PUIs) menu
    Open All Suspected Cases (PUIs) menu
    Wait Until Element Is Enabled    ${search all cases}
    JS Click     ${search all cases}
    Wait Until Element Is Enabled    ${case search submit}
    JS Click    ${case search submit}
    
    
Change PUI Status form
    Wait Until Element Is Enabled    ${change pui status form}
    JS Click    ${change pui status form}
    Wait Until Element Is Enabled    ${convert_back_to_contact}
    JS Click    ${convert_back_to_contact}
    Run Keyword And Ignore Error    Wait Until Element Is Enabled    ${convert_this_suspected_case}
    Run Keyword And Ignore Error    JS Click    ${convert_this_suspected_case}
    
Yes, Close the Record
    Wait Until Element Is Enabled    ${are_you_sure}
    JS Click     ${are_you_sure}
    Wait Until Element Is Enabled     ${close_record}
    Click Element    ${close_record}
    Element Should Be Visible    ${close_yes_message}  
    Element Should Be Visible    ${close_yes_message2} 
    Wait Until Element Is Enabled    ${final_disposition}
    JS Click    ${final_disposition}
    
    #Would you like to send the quarantine release notice by email?  no 
    Wait Until Element Is Enabled    ${like to send mail no}
    JS Click    ${like to send mail no}
    Element Should Be Visible       ${ send the release from quarantine notice by mail question} 
    #Do you want to send the release from quarantine notice by mail?  yes
    Wait Until Element Is Enabled  ${send quarantine mail yes}
    JS Click    ${send quarantine mail yes}
    Element Should Be Visible     ${date_notice_sent} 
    #Do you want to send the release from quarantine notice by mail?  no
    Wait Until Element Is Enabled    ${send quarantine mail no}
    JS Click    ${send quarantine mail no}
    Wait Until Page Does Not Contain    ${date_notice_sent}    
    Element Should Not Be Visible     ${date_notice_sent}     
    Element Should Be Visible    ${no notice label}
    
    ###Would you like to send the quarantine release notice by email? yes   
    Wait Until Element Is Enabled    ${like to send mail yes}
    JS Click    ${like to send mail yes} 
    Input Text    ${what_address}    ${email_input}
    ## toprocess the input
    JS Click    ${like to send mail yes}
    Element Should Be Visible    ${mail_label} 
    #label to process
    JS Click    ${like to send mail yes}
    Submit Form and Check Success
    
No , Close the Record
    Wait Until Element Is Enabled    ${are_you_sure}
    JS Click    ${are_you_sure}
    Wait Until Element Is Enabled     ${dont_close_record} 
    Click Element    ${dont_close_record} 
    Element Should Be Visible    ${close_no_message}
    Element Should Be Visible    ${close_no_message2}
    Submit Form and Check Success
        
Search and Select Archieved Case
    IF    '${archieved_contact_lname}' == '\'
        Search in the case list    ${archieved_contact_name}
    ELSE
         Search in the case list    ${archieved_contact_name} ${archieved_contact_lname}
    END
    Sleep    10s
    Select Created Case    ${archieved_contact}

Yes, Close the Archieved Record
    Wait Until Element Is Enabled     ${close_record}
    Scroll Element Into View    ${close_record}
#    Click Element    ${close_record}
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    ${parent_id}=   SeleniumLibrary.Get Element Attribute    ${do_you_want_to_close_record}     for
    Log To Console    ${parent_id}
    Select Radio Button    ${parent_id}   Yes
    Run Keyword And Ignore Error  Element Should Be Visible    ${no_longer_active_message}
    Run Keyword And Ignore Error  Element Should Be Visible    ${close_yes_message}
    Run Keyword And Ignore Error    JS Click     ${final_disposition2}
    Run Keyword And Ignore Error    JS Click       ${final_disposition}
    Submit Form and Check Success

No , Close the Archieved Record
    Wait Until Element Is Enabled     ${dont_close_record} 
    Scroll Element Into View    ${dont_close_record}
#    Click Element    ${dont_close_record}
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    ${parent_id}=   SeleniumLibrary.Get Element Attribute    ${do_you_want_to_close_record}     for
    Log To Console    ${parent_id}
    Select Radio Button    ${parent_id}   No
    Run Keyword And Ignore Error  Element Should Be Visible    ${no_longer_active_message}
    Run Keyword And Ignore Error  Element Should Be Visible    ${no_longer_active_message2}
    Submit Form and Check Success 
     
    
