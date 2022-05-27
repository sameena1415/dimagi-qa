import os
import pytest

from configparser import ConfigParser
from pathlib import Path


""""This file provides fixture functions for driver initialization"""
@pytest.fixture(scope="session", autouse=True)
def settings():
    if os.environ.get("CI") == "true":
        settings = {}
        for name in ["url", "password", "login_user", "login_pass", "prod_api_key","staging_api_key"]:
            var = f"DIMAGIQA_{name.upper()}"
            if var in os.environ:
                settings[name] = os.environ[var]
        if any(x not in settings for x in ["url", "password","login_user", "login_pass", "prod_api_key", "staging_api_key"]):
            lines = settings.__doc__.splitlines()
            vars_ = "\n  ".join(line.strip() for line in lines if "DIMAGIQA_" in line)
            raise RuntimeError(
                f"Environment variables not set:\n  {vars_}\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )
        if "url" not in settings:
            env = os.environ.get("DIMAGIQA_ENV") or "staging"
            subdomain = "www" if env == "production" else env
            ## updates the url with the project domain while testing in CI
            project = "a/qa-automation-prod" if env == "production" else "a/qa-automation"
            settings["url"] = f"https://{subdomain}.commcarehq.org/"
            settings['api_key'] = settings['prod_api_key'] if env == "production" else settings['staging_api_key']
    else:
        path = Path(__file__).parent.parent / "settings.cfg"
        if not path.exists():
            raise RuntimeError(
                f"Not found: {path}\n\n"
                "Copy settings-sample.cfg to settings.cfg and populate "
                "it with values for the environment you want to test."
            )
        settings = ConfigParser()
        settings.read(path)
        settings["default"]["password"]=settings["default"].pop("json_password")
        if settings["default"]["url"] == "https://www.commcarehq.org/":
            settings["default"]["api_key"] = settings['default']['prod_api_key']
        else:
            settings["default"]["api_key"] = settings['default']['staging_api_key']
        settings = settings["default"]
    ## updates the url with the project domain while testing in local
    yield settings

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == "call" or report.when == "teardown":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            print("reports skipped or failed")
            # file_name = report.nodeid.replace("::", "_") + ".png"
            # screen_img = _capture_screenshot(item.funcargs["settings"])
            # if file_name:
            #     html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
            #            'onclick="window.open(this.src)" align="right"/></div>' % screen_img
            #     extra.append(pytest_html.extras.html(html))
        report.extra = extra


