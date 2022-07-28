from QA_Requests.PerfTickets.testPages.cle_perf.cle import CLEPage


def test_case_cle(driver):
    cle = CLEPage(driver)
    global parent_case_type, child_case_type,  load
    load = "10k"
    parent_case_type = "song_perf_1_1_500000"
    child_case_type = "show_perf_1_1_50000"
    cle.record_cle_time(load, parent_case_type, location="no")
    cle.record_subquery_cle_time(load, child_case_type, parent_case_type)
    cle.record_cle_time_without_filter()
    print("Successful!")
