*** Settings ***
Documentation     Workflow to test Patient Good Path
Suite Setup    HQ Login
Library  SeleniumLibrary
Resource    ../Case Investigation (CI)/Menu/menu.robot
Resource    ../Case Investigation (CI)/Forms/create a new cluster form.robot
Resource    ../Case Investigation (CI)/Forms/view record lab results.robot
Resource    ../Case Investigation (CI)/Forms/case investigation form.robot
Resource    ../Contact Tracing (CT)/Forms/register a new contact form.robot
Resource    ../Contact Tracing (CT)/Forms/contact montitoring form.robot
Resource    ../Case Investigation (CI)/Forms/create a new cluster form.robot
Resource    ../Case Investigation (CI)/Forms/create a new cluster form.robot
#Suite Teardown  Close Browser

*** Test Cases ***

Clusters_1
    [Documentation]    Create cluster - non school/college
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    ${cluster_non_id_created}=      Create New Cluster - non school/college
    ${cluster_non_name}    Get Cluster Name
    ${cluster_non_created}    Set Cluster Name
    Log To Console    ${cluster_non_id_created}
    Set Global Variable    ${cluster_non_id_created}
    Set Global Variable    ${cluster_non_created}
    Set Global Variable    ${cluster_non_name}

Clusters_2
    [Documentation]    Create cluster - school/college
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    ${cluster_id_created}=      Create New Cluster - school/college
    ${cluster_name}    Get Cluster Name
    ${cluster_created}    Set Cluster Name
    Log To Console    ${cluster_id_created}
    Set Global Variable    ${cluster_id_created}
    Set Global Variable    ${cluster_created}
    Set Global Variable    ${cluster_name}

Clusters_3
    [Documentation]    Assign patient to cluster
    Log in as ci_user
    Register New Case
    ${case_name}    Get Case Name
    ${case_created}    Set Case Name
    Open All Cases
    Search in the case list    ${case_name}
    Select Created Case    ${case_created}
    Open View Record Lab Results Form
    Record specimen date        44
    Open All Cases
    Search in the case list    ${case_name}
    Select Created Case    ${case_created}
    Open Case Investigation Form
    ${date_specimen}=    Get specimen collection date
    Log To Console    ${date_specimen}
    Set Global Variable    ${date_specimen}
    Run Keyword And Ignore Error    Add Case Disposition
    Add Cluster Information To Case     ${cluster_non_name}   ${cluster_non_id_created}   ${cluster_name}   ${cluster_id_created}
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${cluster_non_name}
    Select Cluster    ${cluster_non_name}
    Verify Specimen collection date in cluster      ${date_specimen}
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${cluster_name}
    Select Cluster    ${cluster_name}
    Verify Specimen collection date in cluster      ${date_specimen}


Clusters_4
    [Documentation]    Assign contact to cluster
    Log in as ct_user
    Register contact with phone number
    ${contact_name}    Get Contact Name
    ${contact_created}    Set Contact Name
    Open All Contacts
    Search in the case list    ${contact_name}
    Select Created Case    ${contact_created}
    Open Contact Monitoring Form
    Add Contact Monitoring Details
    Add Cluster Information To Contact     ${cluster_non_name}   ${cluster_non_id_created}

Clusters_5
    [Documentation]    Update site info - non school/college
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${cluster_non_name}
    Select Cluster    ${cluster_non_name}
    ${updated_cluster_non_name}     Update Cluster - non school/college     ${date_specimen}    ${cluster_non_name}
    Set Global Variable    ${updated_cluster_non_name}



Clusters_6
    [Documentation]    Update site info - school/college
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${cluster_name}
    Select Cluster    ${cluster_name}
    ${updated_cluster_name}     Update Cluster - school/college     ${cluster_name}
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_name}
    Select Cluster    ${updated_cluster_name}
    Verify non school cluster update    ${updated_cluster_name}     ${cluster_id_created}
    Set Global Variable    ${updated_cluster_name}


Clusters_7
    [Documentation]    Close a cluster (outbreak ended)
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Select Cluster    ${updated_cluster_non_name}
    Close Cluster
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Verify cluster closed       ${updated_cluster_non_name}

Clusters_8
    [Documentation]    Reopen a cluster
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Select Cluster    ${updated_cluster_non_name}
    Reopen Cluster
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Verify cluster open     ${updated_cluster_non_name}

Clusters_9
    [Documentation]    close a cluster (registered in error)
    Log in as ci_user
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Select Cluster    ${updated_cluster_non_name}
    Close Cluster error registered
    Open Clusters PUIs, Cases, Contacts
    Open View Update Cluster Info Form
    Search in the case list    ${updated_cluster_non_name}
    Verify cluster not present      ${updated_cluster_non_name}

