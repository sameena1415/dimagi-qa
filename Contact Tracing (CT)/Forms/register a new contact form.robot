*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../Menu/menu.robot
Resource    ../../Base/base.robot
             									

*** Keywords ***  

Generate Random Contact Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Contact	${hex}
    Set Suite Variable  ${name_random}


Register contact with phone number
   Open Register New Contacts Menu
   Click Element    ${select_first case_in_caselist}
   Click Element    ${continue}
   Run Keyword And Ignore Error    Click Element    ${register_new_contacts_form} 
   Generate Random Contact Name
   ${name_random}    Get Variable Value    ${name_random}
   Input Text       ${contact_first_name}    ${name_random} 
   Input Text       ${contact_last_name}    ${name_random}  
   ${Mobile number}    Generate Mobile Number
   Input Text       ${contact_phone_num}    ${Mobile number}
   JS Click    ${preferred_language}
   JS Click    ${first_symptom_date}
   ${Yesterday's date}    Yesterday's Date
   Input Text    ${first_symptom_date}    ${Yesterday's date}
   JS Click    ${first_symptom_date}
   Submit Form and Check Success  
   
Get Contact Name
    ${name_random}    Get Variable Value    ${name_random} 
    # ${name_random}     Set Variable     Patient-fbe5
    Log    ${name_random}
    [Return]    ${name_random}

Set Contact Name
    ${name_random}    Get Contact Name
    ${contact_created}   Set Variable    //td[text()='${name_random}' and @class='module-caselist-column']
    Log    ${contact_created}
    Set Suite Variable   ${contact_created} 
    [Return]    ${contact_created} 
