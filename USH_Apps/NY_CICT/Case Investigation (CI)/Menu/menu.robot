*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Variables ***

## Menus
${Register a New Case}    (//div[@aria-label='Register a New Case']/div)[1]
${All Cases: Incomplete Demographic Information}    (//div[@aria-label='All Cases: Incomplete Demographic Information']/div)[1]
${All Open Cases}    (//div[@aria-label='All Open Cases']/div)[1]
${All Cases: Unassigned & Open}    (//div[@aria-label='All Cases: Unassigned & Open']/div)[1]
${All Cases: Assigned & Open}    (//div[@aria-label='All Cases: Assigned & Open']/div)[1]
${My Cases}    (//div[@aria-label='My Cases']/div)[1]
${All Closed Cases}    (//div[@aria-label='All Closed Cases']/div)[1]
${All Cases}   (//div[@aria-label='All Cases']/div)[1]
${All Cases: Unable to Reach}    (//div[@aria-label='All Cases: Unable to Reach']/div)[1]    
${Register New Contact without index}    (//div[@aria-label='Register New Contact(s) without Index Case']/div)[1]
${Clusters PUIs, Cases, Contacts}       (//div[@aria-label='Clusters (PUIs, Cases, Contacts)']/div)[1]
${Hub: Healthcare Cases}    (//div[@aria-label='Hub: Healthcare (Cases)']/div)[1]
${Hub: Congregate Cases}    (//div[@aria-label='Hub: Congregate Settings (Cases)']/div)[1]
${Hub: Clusters Cases}    (//div[@aria-label='Hub: Clusters (Cases)']/div)[1]
${Hub: School Cases}    (//div[@aria-label='Hub: School (Cases)']/div)[1]
${Hub: Community Support Specialist Cases}     (//div[@aria-label='Hub: Community Support Specialist (Cases)']/div)[1]
*** Keywords ***
    
Open All Cases
    Open Menu   ${All Cases}
    Sleep    120s

Open All Open Cases
    Open Menu  ${All Open Cases}
    
Open All Closed Cases
    Open Menu   ${All Closed Cases}
    
All Cases: Unable to Reach
    Open Menu   ${All Cases: Unable to Reach}

Open All Cases: Incomplete Demographic Information Menu
    Open Menu   ${All Cases: Incomplete Demographic Information}

Open All Cases: Unassigned & Open
    Open Menu   ${All Cases: Unassigned & Open}

Open All Cases: Assigned & Open
    Open Menu   ${All Cases: Assigned & Open}

Open My Cases
    Open Menu   ${My Cases}

Open Register New Contact without index
    Open Menu   ${Register New Contact without index}

Open Clusters PUIs, Cases, Contacts
    Open Menu   ${Clusters PUIs, Cases, Contacts}

Open Hub Healthcare Cases
    Open Menu   ${Hub: Healthcare Cases}

Open Hub Congregate Settings Cases
    Open Menu    ${Hub: Congregate Cases}

Open Hub Clusters Cases
    Open Menu    ${Hub: Clusters Cases}

Open Hub School Cases
    Open Menu    ${Hub: School Cases}

Open Hub Community Support Specialist Cases
    Open Menu    ${Hub: Community Support Specialist Cases}