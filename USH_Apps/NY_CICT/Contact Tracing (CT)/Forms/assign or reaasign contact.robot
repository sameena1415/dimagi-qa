*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../../Base/base.robot


*** Keywords ***
    
Open Assign or Reassign Contact Form
    Sleep    2s
    Wait Until Element Is Enabled    ${Assign or Reassign Contact Form} 
    JS Click    ${Assign or Reassign Contact Form} 
    
Permanently Assign to Self (CM)
    Open Assign or Reassign Contact Form
    Wait Until Element Is Enabled    ${Permanently assign}  
    JS Click    ${Permanently assign} 
    Execute JavaScript    window.scrollBy(900, 900);
    IF  "${domain}"=="ny-staging-cdcms"
    Answer Dropdown    ${Q:Permanently reassign to}    ${A:Permanently reassign to ct}
    ELSE
    Answer Dropdown    ${Q:Permanently reassign to}    ${A:Permanently reassign to poc ct}
    END
    Submit Form and Check Success 

Unassign from Self (CM)
    Open Assign or Reassign Contact Form  
    Wait Until Element Is Enabled    ${A:Permanently unassign}  
    JS Click    ${A:Permanently unassign} 
    Submit Form and Check Success 


    
   