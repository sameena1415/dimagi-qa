*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot

*** Keywords ***

Open Register New Contacts Menu
   Open App Home Screen
   Wait Until Element Is Enabled    ${register_new_contacts_menu}  
   JS Click    ${register_new_contacts_menu}
     
All Closed Contacts menu
    Wait Until Element Is Enabled    ${all_closed_contacts_menu}
    Click Element    ${all_closed_contacts_menu}
     
All Open Contacts menu
    Open App Home Screen
    Reload Page
    Wait Until Element Is Enabled    ${all_open_contacts_menu} 
    Click Element    ${all_open_contacts_menu} 
   
Open All Contacts Unassigned & Open menu 
        Sleep    2s
        Open App Home Screen
        Wait Until Element Is Visible     ${contacts_unassigned_open_menu}
        Wait Until Element Is Enabled      ${contacts_unassigned_open_menu}
        Sleep    2s
        JS Click    ${contacts_unassigned_open_menu}      
   
All Suspected Cases (PUIs) menu
    Sleep    2s
    Wait Until Element Is Enabled    ${all_suspected_cases_menu} 
    Click Element    ${all_suspected_cases_menu} 


