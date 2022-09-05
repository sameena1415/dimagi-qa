class COUserData:
    """Contains user input test data that are used while running the tests. These can be updated as required."""

    repeat_count = 3
    project_space = "co-performance"
    application = "Justina"
    ci_user = "ci_perf_1"
    ct_user = "ct_perf_1"
    ci_ct_user = "ci/ct_sup_1"

    # This case and contact should be accesible to both the users in test
    pre_configured_case = "Performance"
    pre_configured_contact = "Performance"
    language_list = ["English", "Arabic", "Burmese", "Chinese", "Amharic"]
