""""Contains test data that are used as user inputs across various areass used in Case Search"""


class BhaUserInput:
    """Test Data"""

    """App Name"""
    bha_app_name = "BHA Provider Services (linked to dev app)"  # check for both staging & prod

    """Users"""
    state_level_user = "state.level.user1"
    clinic_level_user = "clinic.level.user1"
    central_registry_2 = "central.registry.user.2"

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
    lock_out_confirmation = "Upon submission, the client will be locked in to care at Aurora Therapy Center LLC - 13th Ave and the requesting clinic will be notified."

    """Search Fields"""
    first_name_required = "(Required) First Name"
    last_name_required = "(Required) Last Name"
    dob_required = "(Required) DOB"
    first_name = "First Name"
    last_name = "Last Name"
    dob = "DOB"
    date_of_birth = "Date of Birth"
    reason_for_no_ssn = "Reason for no SSN"
    consent = "(Required) Consent obtained by provider for the purposes of searching the Central Registry to confirm admission"
    ssn = "Social Security Number"
    medicaid_id = "Medicaid ID"
    client_id = "Client ID"
    # Form Listing
    search_my_clients = "Search My Clients"

    """User Inputs"""
    date_1950_05_01 = "05/01/1950"
    refused_to_provide = "Refused to provide"
    does_not_have_ssn = "Does not have SSN"
    inactive_first_name = "Ronald"
    inactive_last_name_with_typo = "Lew"
    inactive_dob = "03/31/1984"
    yes = "Yes"
    yes_small = "yes"
    approve = "Approve"

    """Clinics"""
    aurora_therapy_center = "Aurora Therapy Center LLC - 13th Ave"

    """Values_on Case List"""
    zero = "0"
    one = "1"
    two = "2"
    five = "5"
    six = "6"
    pending_status = "Pending"
    pending = "[pending]"
    discharged = "Discharged"
    name = "Name"
    username = "Username"
    creation_date = "Creation date"
    no_potential_match_found = "No potential client matches. Proceed to admit new client."

    # CLR staging
    staging_case_link = "https://staging.commcarehq.org/a/co-carecoordination-test/reports/case_data/89943c0de53441909fb77488c1d18905/#properties"
    potential_duplicate = "potential_duplicate_case_ids"
    staging_potential_duplicate_case_id = "5d490f67-525e-43c6-aebf-539bc3762fe5"

    staging_duplicate_case_link = "https://staging.commcarehq.org/a/co-carecoordination-test/reports/case_data/5d490f67-525e-43c6-aebf-539bc3762fe5/#properties"
    potential_duplicate_index = "potential_duplicate_index_case_ids"
    staging_potential_duplicate_index_case_id = "89943c0de53441909fb77488c1d18905"

    # CLR prod
    prod_case_link = "https://www.commcarehq.org/a/co-carecoordination-test/reports/case_data/9b1a60eaf251408ca96b5fd83c96eef1/#properties"
    prod_potential_duplicate_case_id = "ff1c0e97217448af86e890d5ef14c096"

    prod_duplicate_case_link = "https://staging.commcarehq.org/a/co-carecoordination-test/reports/case_data/ff1c0e97217448af86e890d5ef14c096/#properties"
    prod_potential_duplicate_index_case_id = "9b1a60eaf251408ca96b5fd83c96eef1"
