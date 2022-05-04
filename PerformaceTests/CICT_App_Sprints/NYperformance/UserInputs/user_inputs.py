import os


class UserData:
    """Contains user input test data that are used while running the tests. These can be updated as required."""

    """Path Settings"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir, os.pardir))

    no_of_repeat = 3
    env = "www"  # by default, it's set as prod. Add "staging" if pointed towards staging.
    project_space = "ny-performance-cdcms"
    application_before_release = "NY Communicable Disease Case Management System"
    application_after_release = "NY Communicable Disease Case Management System"
    ci_ct_user = "pcg.rayan.singh"
    pre_configured_case = "2 - 1 performance"
    pre_configured_contact = "2 - 1 performance"
    school_search = "ACADEMY FOR"
