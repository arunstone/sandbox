import sys
import pytest

def run_tests(test_type="all"):
    """
    Run tests based on type.
    :param test_type: "selenium", "char", or "all"
    """
    if test_type == "selenium":
        test_paths = ["test_google_search.py"]
    elif test_type == "char":
        test_paths = ["test_char_utils.py"]
    else:  # all
        test_paths = ["test_google_search.py", "test_char_utils.py"]

    # Run pytest programmatically
    pytest_args = test_paths + ["-q", "--html=report.html", "--self-contained-html"]
    exit_code = pytest.main(pytest_args)
    return exit_code

if __name__ == "__main__":
    # Accept command line argument
    if len(sys.argv) > 1:
        choice = sys.argv[1].lower()
        if choice not in ["selenium", "char", "all"]:
            print("Invalid choice. Options: selenium, char, all")
            sys.exit(1)
    else:
        choice = "all"

    print(f"Running tests: {choice}")
    run_tests(choice)
