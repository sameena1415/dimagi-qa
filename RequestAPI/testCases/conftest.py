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
    save_summary_charts(_test_stats)

import base64

def save_base64_chart(image_path, b64_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    with open(b64_path, "w") as f:
        f.write(encoded)

def save_summary_charts(stats):
    from pathlib import Path
    out_dir = Path("slack_charts")
    out_dir.mkdir(exist_ok=True)

    passed  = int(stats.get("passed", 0))
    failed  = int(stats.get("failed", 0))
    skipped = int(stats.get("skipped", 0))
    reruns  = int(stats.get("rerun", 0))  # from pytest-rerunfailures

    # --- Pie chart (Passed/Failed/Skipped) ---
    fig, ax = plt.subplots()
    ax.pie(
        [passed, failed, skipped],
        startangle=90,
        colors=["#66bb6a", "#ef5350", "#fad000"],
        wedgeprops=dict(width=0.4),
        autopct="%1.0f%%" if (passed+failed+skipped) else None,
    )
    ax.axis("equal")
    pie_path = out_dir / "summary_pie.png"
    fig.savefig(pie_path, bbox_inches="tight")
    plt.close(fig)
    save_base64_chart(pie_path, out_dir / "summary_pie_b64.txt")

    # --- Bar chart (Failures & Reruns) ---
    fig, ax = plt.subplots()
    ax.bar(["Failed", "Reruns"], [failed, reruns])
    ax.set_title("Failures and Reruns")
    bar_path = out_dir / "summary_bar.png"
    fig.savefig(bar_path, bbox_inches="tight")
    plt.close(fig)
    save_base64_chart(bar_path, out_dir / "summary_bar_b64.txt")

def _matplotlib_img(fig) -> str:
    """Convert a matplotlib figure to base64 string."""
    buf = BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

def pytest_html_results_summary(prefix, summary, postfix, session):
    """Inject donut pie + bar chart with reruns support (parallel-safe)."""
    tr = session.config.pluginmanager.get_plugin("terminalreporter")
    stats = tr.stats if tr and hasattr(tr, "stats") else {}

    passed  = len(stats.get("passed", []))
    failed  = len(stats.get("failed", []))
    skipped = len(stats.get("skipped", []))

    # Reruns are recorded separately by pytest-rerunfailures
    reruns = len(stats.get("rerun", []))

    # --- Donut Pie Chart (Passed, Failed, Skipped) ---
    pie_labels = ["Passed", "Failed", "Skipped"]
    pie_sizes = [passed, failed, skipped]
    pie_colors = ["#66bb6a", "#ef5350", "#fad000"]

    fig, ax = plt.subplots()
    wedges, texts = ax.pie(
        pie_sizes,
        labels=None,
        colors=pie_colors,
        startangle=90,
        wedgeprops=dict(width=0.4)
    )
    ax.axis("equal")

    # Legend below the donut
    plt.legend(
        wedges,
        [f"{l}: {v}" for l, v in zip(pie_labels, pie_sizes)],
        title="Results",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.08),
        ncol=len(pie_labels)
    )
    pie_img = _matplotlib_img(fig)

    # --- Bar Chart (Failures + Reruns) ---
    bar_img = None
    if failed > 0 or reruns > 0:
        fig, ax = plt.subplots()
        bars = ax.bar(["Failed", "Reruns"], [failed, reruns], color=["#ef5350", "#ff9933"])
        ax.set_title("Failures and Reruns")
        ax.set_ylabel("Number of Tests")
        plt.legend(
            bars,
            [f"Failed: {failed}", f"Reruns: {reruns}"],
            loc="upper center",
            bbox_to_anchor=(0.5, -0.12),
            ncol=2
        )
        bar_img = _matplotlib_img(fig)

    # --- Embed in HTML report ---
    html = "<div style='text-align:center; margin-top:20px;'>"
    html += f"<h3>Test Summary</h3><img src='data:image/png;base64,{pie_img}' style='max-width:500px;'/>"
    if bar_img:
        html += f"<h3>Failures and Reruns</h3><img src='data:image/png;base64,{bar_img}' style='max-width:500px;'/>"
    html += "</div>"

    summary.append(html)
