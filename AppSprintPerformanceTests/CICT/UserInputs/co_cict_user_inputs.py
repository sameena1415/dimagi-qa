class COUserData:
    """Contains user input test data that are used while running the tests. These can be updated as required."""

    repeat_count = 3
    env = "www"  # by default, it's set as prod. Add "staging" if pointed towards staging.
    project_space = "co-performance"
    application = ""
    ci_ct_user1 = "ci_perf_1"
    ci_ct_user2 = "ci/ct_sup_1"

    # This case and contact should be accesible to both the users in test
    pre_configured_case = "November Green"
    pre_configured_contact = "December Blue"
