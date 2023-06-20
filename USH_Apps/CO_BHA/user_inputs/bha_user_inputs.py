""""Contains test data that are used as user inputs across various areass used in Case Search"""


class BhaUserInput:
    """Test Data"""

    """App Name"""
    bha_app_name = "BHA Provider Services (linked to dev app)"  # check for both staging & prod

    """Users"""
    state_level_user = "state.level.user1"
    clinic_level_user = "clinic.level.user1"
    central_registry_2 = "central.registry.2"

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
    first_name = "(Required) First Name"
    last_name = "(Required) Last Name"
    dob = "(Required) DOB"
    reason_for_no_ssn = "Reason for no SSN"
    consent = "(Required) Consent obtained by provider for the purposes of searching the Central Registry to confirm admission"
    ssn = "Social Security Number"
    medicaid_id = "Medicaid ID"
    client_id = "Client ID"

    """User Inputs"""
    date_1950_05_01 = "05/01/1950"
    does_not_have_ssn = "Does not have SSN"
    inactive_first_name = "inactive_first_name"  # Anthony/Sameena to create
    inactive_last_name = "inactive_last_name"  # Anthony/Sameena to create (with a typo)
    inactive_dob = "some dob"  # Anthony/Sameena to create
    yes = "Yes"
    approve = "Approve"

    """Clinics"""
    aurora_therapy_center = "Aurora Therapy Center LLC - 13th Ave"

    """Values_on Case List"""
    one = "1"
    two = "2"
    six = "6"
    pending = "[pending]"
    discharged = "Discharged"
    name = "Name"
    username = "Username"
    creation_date = "Creation Date"
