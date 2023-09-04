""""Contains test data that are used as user inputs across various areass used in the project"""


class BhaUserInput:
    """Test Data"""

    """App Name"""
    bha_app_name = "BHA Provider Services"  # check for both staging & prod

    """Users"""
    state_level_user = "state.level.user1"
    clinic_level_user = "clinic.level.user1"

    """Menus"""
    search_central_registry = "Search Central Registry"
    search_and_admit_client = "Search and Admit Client"
    search_my_clients = "Search My Clients"
    pending_requests = "Pending Requests"
    user_management = "User Management"

    """Forms"""
    admit_client_form = "Admit Client"
    request_admission_review = "Request admission review"
    discharge_client = "Discharge Client"
    update_lock_status_request = "Update Lock Status Request"

    """Clinics"""

    arts_parkside_clinic = "ARTS Parkside Clinic"
    aurora_therapy_center = "Aurora Therapy Center"

    """Labels On Form"""
    first_name_on_form = "First Name"
    last_name_on_form = "Last Name"
    dob_on_form = "Date of Birth"
    cancel = "Cancel"
    completed_treatment = "Completed treatment"
    suboxone = "Suboxone"
    lock_in = "Lock In"

    "Questions"
    where_admit = "(Required) Where would you like to admit this client?"
    bha_approval_needed = "BHA approval is required before the client can be locked in. Please submit this form to send the lock status request to BHA for review."
    lock_out_confirmation = "Upon submission, the client will be locked in to care at " + aurora_therapy_center + " and the requesting clinic will be notified."

    """Search Fields"""
    first_name_required = "(Required) First Name"
    last_name_required = "(Required) Last Name"
    dob_required = "(Required) DOB"
    first_name = "First Name"
    last_name = "Last Name"
    name = "Name"
    dob = "DOB"
    date_of_birth = "Date of Birth"
    reason_for_no_ssn = "Reason for no SSN"
    consent = "(Required) Consent obtained by provider for the purposes of searching the Central Registry to confirm admission"
    ssn = "Social Security Number"
    medicaid_id = "Medicaid ID"
    client_id = "Client ID"
    case_name = "Case Name"
    admission_status = "(Required) Admission Status"

    """User Inputs"""
    inactive = "Inactive"
    date_1950_05_01 = "05/01/1950"
    refused_to_provide = "Refused to provide"
    does_not_have_ssn = "Does not have SSN"
    staging_inactive_first_name = "CLIENT1 FIRST NAME"
    staging_inactive_last_name_with_typo = "CLIENT1 LAST NAAA"
    staging_inactive_dob = "01/01/2010"
    prod_inactive_first_name = "PROD CLIENT1 FIRST NAME"
    prod_inactive_last_name_with_typo = "PROD CLIENT1 LAST NAAA"
    prod_inactive_dob = "01/01/2010"
    yes = "Yes"
    yes_small = "yes"
    approve = "Approve"
    provider = "Provider"

    """Values_on Case List"""
    zero = "0"
    one = "1"
    two = "2"
    five = "5"
    six = "6"
    pending_status = "Pending"
    pending = "[pending]"
    discharged = "Discharged"
    username = "Username"
    creation_date = "Creation date"
    no_potential_match_found = "No potential client matches. Proceed to admit new client."

    # CLR staging
    staging_case_link = "https://staging.commcarehq.org/a/bha-auto-tests/reports/case_data/604a9a80-a83c-4081-97d2-8dc74990ff0b/#properties"
    potential_duplicate = "potential_duplicate_case_ids"
    staging_potential_duplicate_case_id = "8d0dfeaf-c9d4-41fd-801b-18e44bfb6b4a"

    staging_duplicate_case_link = "https://staging.commcarehq.org/a/bha-auto-tests/reports/case_data/8d0dfeaf-c9d4-41fd-801b-18e44bfb6b4a/#properties"
    potential_duplicate_index = "potential_duplicate_index_case_ids"
    staging_potential_duplicate_index_case_id = "604a9a80-a83c-4081-97d2-8dc74990ff0b"

    # CLR prod
    prod_case_link = "https://www.commcarehq.org/a/bha-auto-tests/reports/case_data/a339335b-76cd-4763-82fc-8162d21e30d2/#properties"
    prod_potential_duplicate_case_id = "7faed59b-2f09-40e2-8b59-f4acee0e5c39"

    prod_duplicate_case_link = "https://www.commcarehq.org/a/bha-auto-tests/reports/case_data/7faed59b-2f09-40e2-8b59-f4acee0e5c39/#properties"
    prod_potential_duplicate_index_case_id = "a339335b-76cd-4763-82fc-8162d21e30d2"

    # Messaging History
    clinic_admission_request = "Clinic Admission Request"
    clinic_admission_request_content = "A admission request was submitted by"

    clinic_same_admit_discahrge = "Clinic Same Admit/Discharge"
    clinic_same_admit_discahrge_content = "An admission and discharge form were submitted by"

    clinic_update_lock_status = "Clinic Update Lock Status"
    clinic_update_lock_status_content = "A lock status request was submitted by"

    state_determination_lock_status = "State Determination Lock Status"
    state_determination_lock_status_content = "The lock status request submitted by"



