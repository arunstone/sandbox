import sys
import pytest
import subprocess
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTER_DIR = os.path.join(BASE_DIR, "tester")


def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def run_pytest(test_type, test_file, report_dir):
    """
    Run pytest with proper report/log/screenshot output.
    """
    ts = timestamp()
    base_name = f"{test_type}_{ts}"

    html_report = os.path.join(report_dir, "html-report", f"{base_name}.html")
    log_file = os.path.join(report_dir, "logging", f"{base_name}.log")

    # ensure dirs exist
    os.makedirs(os.path.dirname(html_report), exist_ok=True)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    pytest_args = [
        test_file,
        "-q",
        f"--html={html_report}",
        "--self-contained-html",
        f"--log-file={log_file}",
        "--log-cli-level=INFO"
    ]

    return pytest.main(pytest_args)


def run_tests(test_type="all"):
    """
    Run tests based on type.
    :param test_type: "selenium", "char", "api", "load", "db", or "all"
    """

    if test_type == "selenium":
        test_file = os.path.join(TESTER_DIR, "ui", "test_google_search.py")
        return run_pytest("ui", test_file, os.path.join(TESTER_DIR, "ui"))

    elif test_type == "char":
        test_file = os.path.join(TESTER_DIR, "test", "code", "test_char_utils.py")
        return run_pytest("char", test_file, os.path.join(TESTER_DIR, "test", "code"))

    elif test_type == "api":
        test_file = os.path.join(TESTER_DIR, "api", "test_google_search_api.py")
        return run_pytest("api", test_file, os.path.join(TESTER_DIR, "api"))

    elif test_type == "db":
        test_file = os.path.join(TESTER_DIR, "db", "test_db.py")
        return run_pytest("db", test_file, os.path.join(TESTER_DIR, "db"))

    elif test_type == "load":
        ts = timestamp()
        log_file = os.path.join(TESTER_DIR, "load", "logging", f"load_{ts}.log")
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        cmd = [
            "locust",
            "-f", os.path.join(TESTER_DIR, "load", "load_google_search.py"),
            "--headless",
            "-u", "10",        # number of users
            "-r", "2",         # spawn rate
            "-t", "10s",       # run duration
            "--host", "https://www.google.com"
        ]

        print("Running Locust load test...")
        with open(log_file, "w") as f:
            return subprocess.call(cmd, stdout=f, stderr=f)

    else:  # all
        results = []
        results.append(run_tests("char"))
        results.append(run_tests("selenium"))
        results.append(run_tests("api"))
        results.append(run_tests("db"))
        results.append(run_tests("load"))
        return max(results)  # return highest exit code


if __name__ == "__main__":
    if len(sys.argv) > 1:
        choice = sys.argv[1].lower()
        if choice not in ["selenium", "char", "api", "load", "db", "all"]:
            print("Invalid choice. Options: selenium, char, api, load, db, all")
            sys.exit(1)
    else:
        choice = "all"

    print(f"Running tests: {choice}")
    exit_code = run_tests(choice)
    sys.exit(exit_code)
