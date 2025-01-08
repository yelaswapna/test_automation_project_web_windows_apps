import pytest
from utils.jira_helper import create_jira_issue

def pytest_runtest_makereport(item, call):
    if call.excinfo is not None and call.excinfo.typename != 'Skipped':
        summary = f"Test {item.name} failed"
        description = f"Test {item.name} failed with the following error:\n{call.excinfo}"
        create_jira_issue(summary, description)