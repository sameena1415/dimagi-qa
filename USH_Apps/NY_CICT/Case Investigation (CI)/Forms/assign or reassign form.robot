*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot

*** Keywords ***
    
Permanently Assign to Self
    Open Form   ${Assign or Reassign Case Form}
    Wait Until Element Is Enabled    ${Permanently assign}  
    JS Click    ${Permanently assign} 
    Execute JavaScript    window.scrollBy(900, 900);
    IF  "${domain}"=="ny-staging-cdcms"
    Answer Dropdown    ${Q:Permanently reassign to}    ${A:Permanently reassign to ci}
    ELSE
    Answer Dropdown    ${Q:Permanently reassign to}    ${A:Permanently reassign to poc ci}
    END
    Submit Form and Check Success 

Unassign from Self
    Open Form   ${Assign or Reassign Case Form}
    Wait Until Element Is Enabled    ${A:Permanently unassign}  
    JS Click    ${A:Permanently unassign} 
    Submit Form and Check Success 


    
   