import os
import pytest

from configparser import ConfigParser
from pathlib import Path
from common_utilities.fixtures import *

from AppSprintPerformanceTests.CICT.UserInputs.ny_cict_user_inputs import NYUserData
from AppSprintPerformanceTests.CICT.UserInputs.co_cict_user_inputs import COUserData

""""This file provides fixture functions for driver initialization"""

global driver


@pytest.fixture(scope="session", autouse=True)
def environment_settings_for_cicit_perf(appsite):
    """Load settings from os.environ

            Names of environment variables:
                DIMAGIQA_URL
                DIMAGIQA_LOGIN_USERNAME
                DIMAGIQA_LOGIN_PASSWORD

            See https://docs.github.com/en/actions/reference/encrypted-secrets
            for instructions on how to set them.
            """
    settings = {}
    for name in ["login_username", "login_password"]:
        var = f"DIMAGIQA_{name.upper()}"
        if var in os.environ:
            settings[name] = os.environ[var]
    if "url" not in settings:
        if appsite == "CO":
            settings["url"] = f"https://www.commcarehq.org/a/{COUserData.project_space}/cloudcare/apps/v2/"
        elif appsite == "NY":
            settings["url"] = f"https://www.commcarehq.org/a/{NYUserData.project_space}/cloudcare/apps/v2/"
    return settings


@pytest.fixture(scope="session", autouse=True)
def settings(environment_settings_for_cicit_perf, appsite):
    if os.environ.get("CI") == "true":
        settings = environment_settings_for_cicit_perf
        settings["CI"] = "true"
        if any(x not in settings for x in ["url", "login_username", "login_password"]):
            lines = environment_settings_for_cicit_perf.__doc__.splitlines()
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
    if appsite == "CO":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{COUserData.project_space}/cloudcare/apps/v2/"
    elif appsite == "NY":
        settings["default"]["url"] = f"https://www.commcarehq.org/a/{NYUserData.project_space}/cloudcare/apps/v2/"
    return settings["default"]
