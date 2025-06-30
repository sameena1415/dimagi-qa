import argparse
import subprocess
import time
import os
from datetime import datetime

def run_locust_for_hour(hour, args, is_ci):
    html_report_name = f"hour_{hour:02d}_report.html"
    cmd = [
        "locust",
        "-f", args.locustfile,
        "-u", args.users,
        "-r", args.spawn_rate,
        "--run-time", args.run_time,
        f"--host={args.host}",
        f"--domain={args.domain}",
        f"--app-id={args.app_id}",
        f"--build-id={args.build_id}",
        f"--app-config={args.app_config}",
        f"--user-details={args.user_details}",
        f"--html={html_report_name}"
    ]

    print(f"[{datetime.now()}] Starting Locust for hour {hour:02d}...")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running locust for hour {hour:02d}: {e}")
    else:
        print(f"[{datetime.now()}] Completed hour {hour:02d}")

def wait_until_next_hour():
    now = time.time()
    next_hour = (int(now // 3600) + 1) * 3600
    sleep_duration = max(0, next_hour - now)
    print(f"Waiting {sleep_duration:.2f} seconds until next hour...")
    time.sleep(sleep_duration)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--locustfile", required=True)
    parser.add_argument("-u", "--users", required=True)
    parser.add_argument("-r", "--spawn-rate", required=True)
    parser.add_argument("--run-time", default="1h")
    parser.add_argument("--host", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--app-id", required=True)
    parser.add_argument("--build-id", required=True)
    parser.add_argument("--app-config", required=True)
    parser.add_argument("--user-details", required=True)

    args = parser.parse_args()
    is_ci = os.environ.get("CI") == "true"

    for hour in range(24):
        run_locust_for_hour(hour, args, is_ci)
        if hour < 23:
            wait_until_next_hour()

if __name__ == "__main__":
    main()
