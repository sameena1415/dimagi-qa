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
    Open Menu   ${Register New Contact(s)}
     
Open All Closed Contacts menu
    Open Menu   ${All Closed Contacts}
     
Open All Open Contacts menu
    Open Menu   ${All Open Contacts}
    
Open All Contacts
   Open Menu    ${All Contacts}
    
Open All Contacts: Incomplete Contact Information
   Open Menu    ${All Contacts: Incomplete Contact Information}
   
Open All Contacts: Assigned & Open
   Open Menu    ${All Contacts: Assigned & Open}
   
Open My Contacts: Require Follow-Up
   Open Menu    ${My Contacts: Require Follow-up}
   
Open All Contacts: Require Follow-Up
   Open Menu     ${All Contacts: Require Follow-up}
   
Open All Contacts: Unable to Reach
   Open Menu     ${All Contacts: Unable to Reach}
      
Open All Contacts Unassigned & Open menu
    Open Menu   ${All Contacts: Unassigned & Open}
   
Open All Suspected Cases (PUIs) menu
    Open Menu    ${All Suspected Cases (PUIs)}

Open Hub Healthcare Contacts
    Open Menu   ${Hub: Healthcare Contacts}

Open Hub Congregate Settings Contacts
    Open Menu   ${Hub: Congregate Contacts}

Open Hub Clusters Contacts
    Open Menu    ${Hub: Clusters Contacts}

Open Hub School Contacts
    Open Menu   ${Hub: School Contacts}
