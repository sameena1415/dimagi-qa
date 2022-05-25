import os
from pathlib import Path

""""Contains test data that are used as user inputs across various areasn in CCHQ"""


class UserData:

    """Path Settings"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    if os.environ.get("CI") == "true":
        ROOT = os.path.abspath(os.pardir)+"/dimagi-qa"
    else:
        ROOT = os.path.abspath(os.pardir)
    if os.environ.get("CI") == "true":
        DOWNLOAD_PATH = Path("/home/runner/work/dimagi-qa/dimagi-qa")
    else:
        DOWNLOAD_PATH = Path('~/Downloads').expanduser()

    """User Test Data"""
    domain = 'a/api-tests/'
    post_domain_url = 'api/v0.5/'

