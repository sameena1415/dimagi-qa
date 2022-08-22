
class NYUserData:
    """Contains user input test data that are used while running the tests. These can be updated as required."""

    repeat_count = 3
    env = "www"  # by default, it's set as prod. Add "staging" if pointed towards staging.
    project_space = "ny-performance-cdcms"
    application_before_release = "NY Communicable Disease Case Management System"
    application_after_release = "v13836 - 01/02 release"
    ci_ct_user1 = "pcg.rayan.singh"
    ci_ct_user2 = "pcg.alaina.francis"

    # This case and contact should be accesible to both the users in test
    pre_configured_case = "2 - 1 performance"
    pre_configured_contact = "2 - 1 performance"
    school_list = ["ACADEMY FOR", "ADELPHI UNIVERSITY", "ADIRONDACK COMMUNITY COLLEGE", "ALBANY COLLEGE OF PHARMACY", "ALBANY LAW SCHOOL"]
