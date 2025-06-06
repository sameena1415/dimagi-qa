import os

from configparser import ConfigParser
from pathlib import Path

import pytest_html

from common_utilities.fixtures import *
from datetime import datetime

""""This file provides fixture functions for driver initialization"""

global driver

failed_items = []

@pytest.fixture(scope="session")
def environment_settings_hq():
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_LOGIN_USERNAME
                DIMAGIQA_LOGIN_PASSWORD
                DIMAGIQA_MAIL_USERNAME
                DIMAGIQA_MAIL_PASSWORD

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["url", "login_username", "login_password", "mail_username",
                 "mail_password", "bs_user", "bs_key", "staging_auth_key", "prod_auth_key", "india_auth_key", "eu_auth_key", "invited_webuser_password", "imap_password"]:

        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    if "url" not in settings:
        env = os.environ.get("DIMAGIQA_ENV") or "staging"
        subdomain = "www" if env == "production" else env
        # updates the url with the project domain while testing in CI
        project = "a/qa-automation-prod" if env == "production" else "a/qa-automation"
        settings["url"] = f"https://{subdomain}.commcarehq.org/{project}"
    return settings


@pytest.fixture(scope="session", autouse=True)
def settings(environment_settings_hq):
    if os.environ.get("CI") == "true":
        settings = environment_settings_hq
        settings["CI"] = "true"
        if any(x not in settings for x in ["url", "login_username", "login_password",
                                           "mail_username", "mail_password", "bs_user", "bs_key", "staging_auth_key",
                                           "prod_auth_key", "india_auth_key", "eu_auth_key", "invited_webuser_password", "imap_password"]):
            lines = environment_settings_hq.__doc__.splitlines()
            vars_ = "\n  ".join(line.strip() for line in lines if "DIMAGIQA_" in line)
            raise RuntimeError(
                f"Environment variables not set:\n  {vars_}\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )
        return settings
    path = Path(__file__).parent.parent / "settings.cfg"
    if not path.exists():
        raise RuntimeError(
            f"Not found: {path}\n\n"
            "Copy settings-sample.cfg to settings.cfg and populate "
            "it with values for the environment you want to test."
        )
    settings = ConfigParser()
    settings.read(path)
    # updates the url with the project domain while testing in local
    if settings["default"]["url"] == "https://www.commcarehq.org/":
        settings["default"]["url"] = f"{settings['default']['url']}a/qa-automation-prod"
    else:
        settings["default"]["url"] = f"{settings['default']['url']}a/qa-automation"
    return settings["default"]


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Collect test counts
    passed = terminalreporter.stats.get('passed', [])
    failed = terminalreporter.stats.get('failed', [])
    error = terminalreporter.stats.get('error', [])
    skipped = terminalreporter.stats.get('skipped', [])
    xfail = terminalreporter.stats.get('xfail', [])

    env = os.environ.get("DIMAGIQA_ENV", "default_env")

    # Define the filename based on the environment
    filename = f'hqsmoke_test_counts_{env}.txt'

    # Write the counts to a file
    with open(filename, 'w') as f:
        f.write(f'PASSED={len(passed)}\n')
        f.write(f'FAILED={len(failed)}\n')
        f.write(f'ERROR={len(error)}\n')
        f.write(f'SKIPPED={len(skipped)}\n')
        f.write(f'XFAIL={len(xfail)}\n')

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Call existing screenshot hook from fixtures if it exists
    try:
        from common_utilities.fixtures import pytest_runtest_makereport as screenshot_hook
        # Simulate calling the other makereport logic manually
        screenshot_hook(item, call)
    except (ImportError, AttributeError):
        pass

    if report.when == "call" and report.failed:
        failed_items.append(item)


def pytest_sessionfinish(session, exitstatus):
    if not failed_items:
        return

    lines = []
    for item in failed_items:
        try:
            doc = item.function.__doc__ or "No reproduction steps provided."
        except AttributeError:
            doc = "No docstring available (non-function test case)"
        lines.append(f"Test: {item.nodeid}\nRepro Steps:\n{doc.strip()}\n\n---")

    with open("jira_ticket_body.txt", "w", encoding="utf-8") as f:
        f.write(f"🔥 Automated Failure Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("\n".join(lines) if lines else "✅ All tests passed.")


