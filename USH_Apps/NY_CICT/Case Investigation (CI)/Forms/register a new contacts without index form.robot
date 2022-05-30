*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot
Resource    ../Menu/menu.robot

*** Variables ***

## Register a New Contact Form

${how_many_new_contacts}     //span[text()='How many new close contacts do you want to record?']/following::div[1]/div[@class='widget']/descendant::input
${type_of_contact}      //p[text()='Household']
${contact_first_name_1}     (//span[text()='First name']/following::div[1]/div[@class='widget']/descendant::textarea)[1]
${contact_last_name_1}     (//span[text()='Last name']/following::div[1]/div[@class='widget']/descendant::textarea)[1]
${contact_phone_num_1}    (//span[text()='Phone number:']/following::div[1]/div[@class='widget']/descendant::input)[1]
${preferred_language_1}    (//p[text()='English'])[1]
${last_contact_date_1}    (//span[contains(text(),'When was the last day ')]/following::div[1]//input[@type='text'])[1]

${contact_first_name_2}     (//span[text()='First name']/following::div[1]/div[@class='widget']/descendant::textarea)[2]
${contact_last_name_2}     (//span[text()='Last name']/following::div[1]/div[@class='widget']/descendant::textarea)[2]
${contact_phone_num_2}    (//span[text()='Phone number:']/following::div[1]/div[@class='widget']/descendant::input)[2]
${preferred_language_2}    (//p[text()='English'])[2]
${last_contact_date_2}    (//span[contains(text(),'When was the last day ')]/following::div[1]//input[@type='text'])[2]

${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']


*** Keywords ***

Generate Random Patient Name
    ${hex} =    Generate Random String	4	[NUMBERS]abcdef
    ${name_random} =     Catenate	SEPARATOR=-	Patient	${hex}
    Set Suite Variable  ${name_random}

Register New Contacts to Case
    [Arguments]     ${n}    ${name}     ${phone}
    Sleep    2s
    Wait Until Element Is Visible   ${register_new_contacts_form}
    JS Click    ${register_new_contacts_form}
    Wait Until Element Is Visible    ${type_of_contact}
    JS Click    ${type_of_contact}
    Input Text    ${how_many_new_contacts}  ${n}
    Press Keys   ${how_many_new_contacts}   TAB
    FOR    ${i}    IN RANGE   0  ${n}
       ${j}=    Evaluate    ${i} + 1
       Scroll Element Into View    ${contact_first_name_${j}}
       Input Text       ${contact_first_name_${j}}     ${name}_${j}
       Input Text       ${contact_last_name_${j}}    ${name}_${j}
       Input Text       ${contact_phone_num_${j}}    ${phone}
       JS Click    ${preferred_language_${j}}
       JS Click   ${last_contact_date_${j}}
       ${Yesterday's date}    Yesterday's Date
       Input Text    ${last_contact_date_${j}}    ${Yesterday's date}
       JS Click    ${last_contact_date_${j}}
    END
    Submit Form and Check Success

Register contact with given values
    [Arguments]  ${name}     ${phone}
    Open Register New Contact without index
    JS Click    ${type_of_contact}
    Scroll Element Into View    ${contact_first_name}
    Input Text       ${contact_first_name}     ${name}
    Input Text       ${contact_last_name}    ${name}
    Input Text       ${contact_phone_num}    ${phone}
    JS Click    ${preferred_language}
    JS Click   ${last_contact_date}
    ${Yesterday's date}    Yesterday's Date
    Input Text    ${last_contact_date}    ${Yesterday's date}
    JS Click    ${last_contact_date}
    Submit Form and Check Success
