*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## Menus
${Register New Contact(s)}    (//div[@aria-label='Register New Contact(s)']/div)[1]
${All Closed Contacts}   (//div[@aria-label='All Closed Contacts']/div)[1]
${All Open Contacts}    (//div[@aria-label='All Open Contacts']/div)[1]
${All Contacts: Unassigned & Open}    (//div[@aria-label='All Contacts: Unassigned & Open']/div)[1]
${All Suspected Cases (PUIs)}    (//div[@aria-label='All Suspected Cases (PUIs)']/div)[1]
${All Contacts: Incomplete Contact Information}    (//div[@aria-label='All Contacts: Incomplete Contact Information']/div)[1]
${All Contacts: Unable to Reach}    (//div[@aria-label='All Contacts: Unable to Reach']/div)[1]
${All Contacts: Assigned & Open}    (//div[@aria-label='All Contacts: Assigned & Open']/div)[1]
${My Contacts: Require Follow-up}    (//div[@aria-label='My Contacts: Require Follow-up']/div)[1]
${All Contacts: Require Follow-up}    (//div[@aria-label='All Contacts: Require Follow-up']/div)[1]
${All Contacts}    (//div[@aria-label='All Contacts']/div)[1]    
${Hub: Healthcare Contacts}    (//div[@aria-label='Hub: Healthcare (Contacts)']/div)[1]
${Hub: Congregate Contacts}    (//div[@aria-label='Hub: Congregate Settings (Contacts)']/div)[1]
${Hub: Clusters Contacts}    (//div[@aria-label='Hub: Clusters (Contacts)']/div)[1]
${Hub: School Contacts}    (//div[@aria-label='Hub: School (Contacts)']/div)[1]



*** Keywords ***

Open Register New Contacts Menu
    Open App Home Screen
    Sleep    2s 
    JS Click    ${Register New Contact(s)}
     
Open All Closed Contacts menu
    Open App Home Screen
    Sleep    2s
    JS Click    ${All Closed Contacts}
     
Open All Open Contacts menu
    Open App Home Screen
    Reload Page
    Sleep    2s 
    JS Click    ${All Open Contacts} 
    
Open All Contacts
   Open App Home Screen
   Sleep    2s  
   JS Click    ${All Contacts}
    
Open All Contacts: Incomplete Contact Information
   Open App Home Screen
   Sleep    2s    
   JS Click    ${All Contacts: Incomplete Contact Information}
   
Open All Contacts: Assigned & Open
   Open App Home Screen
   Sleep    2s   
   JS Click    ${All Contacts: Assigned & Open}
   
Open My Contacts: Require Follow-Up
   Open App Home Screen
   Sleep    2s  
   JS Click    ${My Contacts: Require Follow-up}
   
Open All Contacts: Require Follow-Up
   Open App Home Screen
   Sleep    2s
   JS Click    ${All Contacts: Require Follow-up}
   
Open All Contacts: Unable to Reach
   Open App Home Screen
   Sleep    2s
   JS Click    ${All Contacts: Unable to Reach}
      
Open All Contacts Unassigned & Open menu 
    Sleep    10s
    Open App Home Screen
    Sleep    2s
    JS Click    ${All Contacts: Unassigned & Open}     
   
Open All Suspected Cases (PUIs) menu
    Open App Home Screen
    Sleep    2s
    JS Click    ${All Suspected Cases (PUIs)}

Open Hub Healthcare Contacts
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Hub: Healthcare Contacts}
    JS Click    ${Hub: Healthcare Contacts}

Open Hub Congregate Settings Contacts
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Hub: Congregate Contacts}
    JS Click    ${Hub: Congregate Contacts}

Open Hub Clusters Contacts
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Hub: Clusters Contacts}
    JS Click    ${Hub: Clusters Contacts}

Open Hub School Contacts
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Hub: School Contacts}
    JS Click    ${Hub: School Contacts}

