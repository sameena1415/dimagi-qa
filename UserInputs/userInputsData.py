from pathlib import Path


class UserInputsData:
    application = "Village Health"
    domain = "qa-automation"
    download_path = Path('~/Downloads').expanduser()
    download_path_ci = r"/home/runner/work/dimagi-qa/dimagi-qa/"
    # Report names
    form_export_name = "CCHQ Smoke Tests Form Export"
    case_export_name = "CCHQ Smoke Tests Case Export"
    dashboard_feed_form = "CCHQ Smoke Tests Dashboard Form feed"
    dashboard_feed_case = "CCHQ Smoke Tests Dashboard Case feed"
    odata_feed_form = "CCHQ Smoke Tests Odata Form feed"
    odata_feed_case = "CCHQ Smoke Tests Odata Case feed"
