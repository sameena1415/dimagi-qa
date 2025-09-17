import os
import pytest

from configparser import ConfigParser
from pathlib import Path

import matplotlib.pyplot as plt
import base64
from io import BytesIO


""""This file provides fixture functions for driver initialization"""


@pytest.fixture(scope="session", autouse=True)
def settings():
    if os.environ.get("CI") == "true":
        settings = {}
        for name in ["url", "password", "login_user", "login_pass", "prod_api_key","staging_api_key", "india_api_key"]:
            var = f"DIMAGIQA_{name.upper()}"
            if var in os.environ:
                settings[name] = os.environ[var]
        if "url" not in settings:
            env = os.environ.get("DIMAGIQA_ENV") or "staging"
            subdomain = "www" if env == "production" else ("india" if env == "india" else env)
            # updates the url with the project domain while testing in CI
            settings["url"] = f"https://{subdomain}.commcarehq.org/"
            settings['api_key'] = settings['prod_api_key'] if env == "production" else settings[subdomain+'_api_key']

        if any(x not in settings for x in ["url", "password","login_user", "login_pass", "prod_api_key", "staging_api_key", "india_api_key"]):
            lines = settings.__doc__.splitlines()
            vars_ = "\n  ".join(line.strip() for line in lines if "DIMAGIQA_" in line)
            raise RuntimeError(
                f"Environment variables not set:\n  {vars_}\n\n"
                "See https://docs.github.com/en/actions/reference/encrypted-secrets "
                "for instructions on how to set them."
            )

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
        elif settings["default"]["url"] == "https://india.commcarehq.org/":
            settings["default"]["api_key"] = settings['default']['india_api_key']
        else:
            settings["default"]["api_key"] = settings['default']['staging_api_key']
        settings = settings["default"]
    # updates the url with the project domain while testing in local
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
        report.extra = extra


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # Collect test counts
    passed = terminalreporter.stats.get('passed', [])
    failed = terminalreporter.stats.get('failed', [])
    error = terminalreporter.stats.get('error', [])
    skipped = terminalreporter.stats.get('skipped', [])
    xfail = terminalreporter.stats.get('xfail', [])
    # Write the counts to a file
    # Determine the environment
    env = os.environ.get("DIMAGIQA_ENV", "default_env")

    # Define the filename based on the environment
    filename = f'test_counts_{env}.txt'
    with open(filename, 'w') as f:
        f.write(f'PASSED={len(passed)}\n')
        f.write(f'FAILED={len(failed)}\n')
        f.write(f'ERROR={len(error)}\n')
        f.write(f'SKIPPED={len(skipped)}\n')
        f.write(f'XFAIL={len(xfail)}\n')


# conftest.py
import pytest
import matplotlib.pyplot as plt
import base64
from io import BytesIO

_test_stats = {}

def pytest_sessionfinish(session, exitstatus):
    """Collect stats at the end of the test session."""
    tr = session.config.pluginmanager.get_plugin("terminalreporter")
    global _test_stats
    _test_stats = {
        "passed": len(tr.stats.get("passed", [])),
        "failed": len(tr.stats.get("failed", [])),
        "skipped": len(tr.stats.get("skipped", [])),
        "error": len(tr.stats.get("error", [])),
        "xfail": len(tr.stats.get("xfail", [])),
    }

def _matplotlib_img(fig) -> str:
    """Convert a matplotlib figure to base64 string."""
    buf = BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

def pytest_html_results_summary(prefix, summary, postfix):
    """Inject donut pie + conditional bar chart into pytest-html report."""
    if not _test_stats:
        return

    passed = _test_stats.get("passed", 0)
    failed = _test_stats.get("failed", 0)
    skipped = _test_stats.get("skipped", 0)
    reruns = _test_stats.get("rerun", 0)

    # --- Donut Pie Chart (Passed, Failed, Skipped) ---
    pie_labels = ["Passed", "Failed", "Skipped"]
    pie_sizes = [passed, failed, skipped]
    pie_colors = ["#66bb6a", "#ef5350", "#ffee58"]

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        pie_sizes,
        labels=None,  # don't place labels inside
        colors=pie_colors,
        startangle=90,
        wedgeprops=dict(width=0.4)  # donut style
    )
    ax.axis("equal")

    # Add labels outside with leader lines
    ax.legend(
        wedges,
        [f"{l}: {v}" for l, v in zip(pie_labels, pie_sizes)],
        title="Results",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1)
    )

    pie_img = _matplotlib_img(fig)

    # --- Bar Chart (Failures + Reruns) ---
    bar_img = None
    if failed > 0 or reruns > 0:   # only generate if relevant
        bar_labels = ["Failed", "Reruns"]
        bar_sizes = [failed, reruns]
        bar_colors = ["#ef5350", "#42a5f5"]

        fig, ax = plt.subplots()
        ax.bar(bar_labels, bar_sizes, color=bar_colors)
        ax.set_title("Failures and Reruns")
        ax.set_ylabel("Number of Tests")
        bar_img = _matplotlib_img(fig)

    # --- Embed in HTML report (center aligned) ---
    html = (
        "<div style='text-align:center; margin-top:20px;'>"
        f"<h3>Test Summary</h3>"
        f"<img src='data:image/png;base64,{pie_img}' style='max-width:500px;'/>"
    )
    if bar_img:
        html += (
            f"<h3>Failures and Reruns</h3>"
            f"<img src='data:image/png;base64,{bar_img}' style='max-width:500px;'/>"
        )
    html += "</div>"

    summary.append(html)
