*** Settings ***
Library  SeleniumLibrary
Resource    ../../Base/base.robot

*** Keywords *** 

Convert contact to PUI using CM form
        Open All Contacts Unassigned & Open menu
        ${contact_name}    Get Contact Name
        ${contact_created}   Set Contact Name
        Search in the case list    ${contact_name}
        Select Created Case    ${contact_created}         
        Click Element    ${contact_monitoring_form}
        Wait Until Element Is Enabled    ${initial_interview_disposition}    
        JS Click    ${initial_interview_disposition}
        JS Click    ${race}
        JS Click    ${ethnicity}
        JS Click    ${gender}
        JS Click    ${symptom_congestion}
        JS Click   ${symptom_fatigue}      
        JS Click    ${symptom_fever}
        JS Click    ${symptom_runny_nose} 
        Wait Until Element Is Enabled    ${date_of_symptomp_onset}
        JS Click    ${date_of_symptomp_onset} 
        Input Text    ${date_of_symptomp_onset}    Yesterday's Date
        JS Click    ${date_of_symptomp_onset} 
        JS Click    ${yes_convert_pui} 
        Submit Form and Check Success