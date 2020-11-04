import os

from pathlib import Path


class UserInputsData:

    domain = "another-upstream"
    download_path = Path(str(os.path.expanduser('~\Downloads')))
    # Report names
    form_export_name = "CCHQ Smoke Tests Form Export"
    case_export_name = "CCHQ Smoke Tests Case Export"
    dashboard_feed_form = "CCHQ Smoke Tests Dashboard Form feed"
    dashboard_feed_case = "CCHQ Smoke Tests Dashboard Case feed"
    odata_feed_form = "CCHQ Smoke Tests Odata Form feed"
    odata_feed_case = "CCHQ Smoke Tests Odata Case feed"
