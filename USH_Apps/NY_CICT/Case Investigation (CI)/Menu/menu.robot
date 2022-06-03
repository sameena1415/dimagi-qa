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
*** Keywords ***
    
Open All Cases
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Cases} 
    JS Click    ${All Cases}

Open All Open Cases
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Open Cases}
    JS Click    ${All Open Cases}
    
Open All Closed Cases
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Closed Cases}
    JS Click    ${All Closed Cases}
    
All Cases: Unable to Reach
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Cases: Unable to Reach}
    JS Click    ${All Cases: Unable to Reach}

Open All Cases: Incomplete Demographic Information Menu
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Cases: Incomplete Demographic Information}
    JS Click    ${All Cases: Incomplete Demographic Information}

Open All Cases: Unassigned & Open
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Cases: Unassigned & Open}
    JS Click    ${All Cases: Unassigned & Open}    

Open All Cases: Assigned & Open
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${All Cases: Assigned & Open}
    JS Click    ${All Cases: Assigned & Open} 
    

Open My Cases
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${My Cases}
    JS Click    ${My Cases}

Open Register New Contact without index
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Register New Contact without index}
    Click Element    ${Register New Contact without index}

Open Clusters PUIs, Cases, Contacts
    Open App Home Screen
    Sleep    2s
    Wait Until Element Is Enabled    ${Clusters PUIs, Cases, Contacts}
    JS Click    ${Clusters PUIs, Cases, Contacts}