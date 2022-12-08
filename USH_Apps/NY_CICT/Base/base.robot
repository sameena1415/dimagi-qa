*** Settings ***
Library  SeleniumLibrary        timeout=200s
Library    String
Library    DateTime
Resource    ../Locators/locators.robot
Resource     ../Case Investigation (CI)/Forms/register a new case form.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Library     driverpath.py
Library    base_python_functions.py
Library    Collections

*** Keywords ***
    
Driver Launch
    ${chromedriver_path}=   Wait Until Keyword Succeeds  2 min  10 sec   driverpath.Get Driver Path
    ${chrome_options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
    Call Method    ${chrome_options}    add_argument    --disable-extensions
    Call Method    ${chrome_options}    add_argument    --headless
    Call Method    ${chrome_options}    add_argument    --start-maximized
    Call Method    ${chrome_options}    add_argument    --disable-dev-shm-usage
    Call Method    ${chrome_options}    add_argument    --no-sandbox
    Wait Until Keyword Succeeds  2 min  5 sec        Open Browser    ${LOGIN URL}    ${BROWSER}      executable_path=${chromedriver_path}       options=${chrome_options}

    Set Window Size    1920    1080
    Set Selenium Implicit Wait  ${implcit_wait_time}
    Maximize Browser Window

HQ Login
    Input Text    ${username}    ${email}
    Input Text    ${password}   ${pass}
    Run Keyword And Ignore Error    Wait Until Page Contains Element    ${confirm_cookie}   20s
    ${IsElementVisible}=  Run Keyword And Return Status    Element Should Be Visible   ${confirm_cookie}
    Run Keyword If     ${IsElementVisible}    Click Element  ${confirm_cookie}
    Click Button  ${submit_button}
    ${token}    Generate 2FA Token    ${secret}
    Input Text    ${otp_token}   ${token}
    Click Button  ${submit_button}
    Title Should Be    ${commcare hq title}
    Open Web App


Open Web App
    ${IsElementVisible}=  Run Keyword And Return Status    Element Should Be Visible   ${confirm_cookie}
    Run Keyword If     ${IsElementVisible}    Click Element  ${confirm_cookie}
    Click Element    ${webapps_menu}
   
Open App Home Screen
    Sleep    10s
    TRY
        Wait Until Element Is Visible    ${app_home}
        Wait Until Element Is Enabled    ${app_home}
        Click Element    ${app_home}
        ${AnotherProcess}=  Run Keyword And Return Status    Element Should Be Visible   ${another_process_error}
         IF     ${AnotherProcess}
            Sleep 60s
            JS Click      ${app_home}
         END
    EXCEPT
        Run Keyword And Ignore Error    Click Element    ${select_app}
    END

Open WebApp Home
    Sleep    3s
    ${CookieVisible}=  Run Keyword And Return Status    Element Should Be Visible   ${confirm_cookie}
    Run Keyword If     ${CookieVisible}    Click Element  ${confirm_cookie}
    ${LoginPopUpVisible}=  Run Keyword And Return Status    Element Should Be Visible   ${confirm_user_login}
    Run Keyword If     ${LoginPopUpVisible}    JS Click      ${confirm_user_login}
    Wait Until Element Is Enabled    ${webapps_home}
    Click Element        ${webapps_home}
    
Sync App
    Open WebApp Home
    Click Element    ${sync}
    Sleep    5s
    Run Keyword And Ignore Error    Wait Until Element Is Visible    ${sync success}

Go Back Home and Sync App
    Click Element    ${home_btn}
    Click Element    ${sync}
    Sleep    5s
    Wait Until Element Is Visible    ${sync success}
    Sleep    5s
    Run Keyword And Ignore Error    Click Element    ${select_app}

Log in as ci_user
   ${default_selenium_timeout}     Get Selenium Timeout
   Sync App
   Click Element    ${login_as}
   Click Element    ${ci_user}
   Sleep    2s
   Click Element    ${confirm_user_login}
   Sleep    2s
   Sync App
   Click Element    ${select_app} 
   
Log in as ct_user
   Sync App
   Click Element    ${login_as}
   Click Element    ${ct_user}
   Sleep    2s
   Click Element    ${confirm_user_login}
   Sync App
   Click Element    ${select_app} 

Log in as ctsup_user
   Sync App
   Click Element    ${login_as}
   Wait Until Keyword Succeeds  2 min  5 sec   Input Text    ${search_username}     CT Supervisor
   Sleep    2s
   JS Click    ${search_user_button}
   Sleep    2s
   TRY
        Click Element    ${ctsup_user}
   EXCEPT
        Input Text    ${search_username}     CT Supervisor
        Click Element    ${search_user_button}
        Click Element    ${ctsup_user}
   END
   Click Element    ${confirm_user_login}
   Sleep    2s
   Sync App
   Click Element    ${select_app}

Log in as cisup_user
   Sync App
   Click Element    ${login_as}
   Input Text    ${search_username}     CI Supervisor
   Click Element    ${search_user_button}
   Sleep    2s
   Click Element    ${cisup_user}
   Sleep    2s
   Click Element    ${confirm_user_login}
   Sleep    2s
   Sync App
   Click Element    ${select_app}

JS Click
    [Arguments]    ${element}
    Wait Until Element Is Enabled    ${element}
    Wait Until Element Is Visible    ${element}
    Execute JavaScript    document.evaluate("${element}",document.body,null,9,null).singleNodeValue.click();
    Complete Page Load Jquery

Generate Mobile Number
   ${mobile number}    Generate random string    10    0123456789 
   [Return]    ${mobile number}   
   
Yesterday's Date
   ${date}     Get Current Date    result_format=%m/%d/%Y    increment=-1 day
   [Return]   ${date}
   
Past Date Generator
   [Arguments]      ${n}
   ${date}     Get Current Date    result_format=%m/%d/%Y    increment=-${n} day
   [Return]   ${date}


Today's Date
   ${date}     Get Current Date    result_format=%m/%d/%Y
   [Return]   ${date}


Future Date Generator
   [Arguments]      ${n}
   ${date}     Get Current Date    result_format=%m/%d/%Y    increment=${n} day
   [Return]   ${date}


Select Dropdown
   [Arguments]    ${question}    ${answer}
   Wait Until Element Is Enabled   ${question}
   Wait Until Element Is Visible    ${question}
   Select From List By Index    ${answer}   ${1}
   
Answer Dropdown
   [Arguments]    ${question}    ${answer}
   Wait Until Element Is Enabled   ${question}
   Wait Until Element Is Visible    ${question}
   Click Element   ${question}
   Wait Until Element Is Visible    ${answer}
   Click Element  ${answer}

Answer Input Text
   [Arguments]    ${question}    ${answer}    ${success}
   Wait Until Element Is Enabled    ${question} 
   Scroll Element Into View    ${question} 
   Clear Element Text   ${question} 
   Input Text    ${question}     ${answer}
   Wait Until Element Is Visible    ${success}

Go Back
    Execute Javascript  history.back()

Complete Page Load Jquery
    Wait for condition  return window.document.readyState === 'complete'        300s
    Wait for condition  return((window.jQuery != null) && (jQuery.active === 0))        300s

Search in the case list
    [Arguments]    ${case_or_contact_created}
    Input Text    ${search_case}    ${case_or_contact_created}
    Wait Until Element Is Enabled  ${search_button}
    Click Element    ${search_button}
    ${AnotherProcess}=  Run Keyword And Return Status    Wait Until Element Is Visible    ${another_process_error}  60s
    IF   ${AnotherProcess}
        Sleep   100s
        Clear Element Text  ${search_case}
        Input Text    ${search_case}    ${case_or_contact_created}
        Click Element   ${search_button}
    END

Select Created Case
    [Arguments]    ${case_or_contact_created}
    JS Click    ${case_or_contact_created}
    Sleep   10s
    Wait Until Element Is Visible    ${continue}
    Wait Until Keyword Succeeds  3x  1 min   Scroll Element Into View    ${continue}
    Click Element    ${continue}
    ${AnotherProcess}=  Run Keyword And Return Status    Wait Until Element Is Visible    ${another_process_error}  60s
        IF   ${AnotherProcess}
        Sleep   100s
        JS Click   ${select_first case_in_caselist}
        Wait Until Element Is Visible    ${continue}
        Wait Until Keyword Succeeds  3x  1 min   Scroll Element Into View    ${continue}
        Click Element    ${continue}
    END


Open Form
    [Arguments]    ${form_name}
    JS Click    ${form_name}
    ${AnotherProcess}=  Run Keyword And Return Status    Wait Until Element Is Visible    ${another_process_error}      60s
    ${MenuContainer}=   Run Keyword And Return Status    Element Should Be Visible   ${menu container}

    IF  ${AnotherProcess}
        Sleep   100s
        Select Created Case    ${select_first case_in_caselist}
        Wait Until Element Is Visible    ${continue}
        Wait Until Keyword Succeeds  3x  1 min   Scroll Element Into View    ${continue}
        Click Element    ${continue}
        Sleep   100s
        JS Click    ${form_name}
    END


Open Menu
    [Arguments]    ${menu_name}
    Open App Home Screen
    Sleep   5s
    TRY
        Wait Until Element Is Enabled    ${menu_name}
    EXCEPT
        Open App Home Screen
        Wait Until Element Is Enabled    ${menu_name}
    END
    JS Click    ${menu_name}

Select Cluster
    [Arguments]    ${case_or_contact_created}
    Wait Until Element Is Enabled    //tr[.//td[text()='${case_or_contact_created}']]
    Sleep    2s
    JS Click    //tr[.//td[text()='${case_or_contact_created}']]

Select Created Case with no lab result
    [Arguments]    ${case_or_contact_created}
    Wait Until Element Is Enabled    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[6][(normalize-space())])
    Sleep    2s
    JS Click    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[6][(normalize-space())])
    Wait Until Element Is Enabled    ${continue}
    Sleep    2s
    Click Element    ${continue}

Select Created Case with lab result
    [Arguments]    ${case_or_contact_created}
    Wait Until Element Is Enabled    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[6][not(normalize-space())])
    Sleep    2s
    JS Click    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[6][not(normalize-space())])
    Wait Until Element Is Enabled    ${continue}
    Sleep    2s
    Click Element    ${continue}

Select Case with Open Status
    [Arguments]    ${case_or_contact_created}
    Wait Until Element Is Enabled    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[9][normalize-space()='Open']
    Sleep    2s
    JS Click    (//tr[.//td[text()='${case_or_contact_created}']]/self::tr//td[9][normalize-space()='Open']
    Wait Until Element Is Enabled    ${continue}
    Sleep    2s
    Click Element    ${continue}

Case Search Search All
    Wait Until Element Is Enabled    ${search all cases in the list}
    JS Click    ${search all cases in the list}
    Wait Until Element Is Enabled    ${case search submit}
    JS Click    ${case search submit}
    
Case Search
    [Arguments]     ${case_or_contact_created}   
    Wait Until Element Is Enabled    ${search all cases in the list}
    JS Click    ${search all cases in the list}
    Wait Until Element Is Enabled    ${first-name_case_search}
    Wait Until Keyword Succeeds  3x  60s  Input Text    ${first-name_case_search}    ${case_or_contact_created}
    Wait Until Keyword Succeeds  3x  60s  Input Text    ${last-name_case_search}    ${case_or_contact_created}
    Wait Until Element Is Enabled    ${case search submit}
    Wait Until Keyword Succeeds  3x  60s  JS Click    ${case search submit}
    ${present}=  Run Keyword And Return Status    Element Should Be Visible   ${another_process_error}
    IF   ${present}
        Sleep   120s
        JS Click    ${case search submit}
    END

Submit Form and Check Success
    Element Should Be Enabled    ${submit_form}
    JS Click   ${submit_form}
    Wait Until Element Is Visible    ${success_message}
    Element Should Be Visible    ${success_message}

Click Element
    [Arguments]     ${element}
    Wait Until Element Is Visible    ${element}
    SeleniumLibrary.Click Element    ${element}
    Complete Page Load Jquery

Click Button
    [Arguments]     ${element}
    Wait Until Element Is Visible    ${element}
    SeleniumLibrary.Click Button    ${element}
    Complete Page Load Jquery

Input Text
    [Arguments]    ${element}     ${text}
    Wait Until Element Is Visible    ${element}
    SeleniumLibrary.Input Text    ${element}     ${text}
    Complete Page Load Jquery
