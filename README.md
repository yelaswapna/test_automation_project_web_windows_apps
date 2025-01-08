# Test Automation Project For Web and Desktop Applications

This repository contains the base setup of a UI testing project using Python, Selenium Webdriver, Pywinauto, and the Page Object Model pattern. It also includes integration with Jira to create defects when test cases fail.

## Requirements

* Python 3.12.3
* pip (24.0) and setuptools
* [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (recommended)
* ChromeDriver (for web application testing)
* Jira account and API token

## Installation

1. Download or clone the repository.
2. Open a terminal.
3. Go to the project root directory.
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment by executing the following:
    - On Windows: `venv\Scripts\activate`
    - On Unix or MacOS: `source venv/bin/activate`
6. Install the required packages: `pip install -r requirements.txt`

## Configuration

1. Create a `jira_config.py` file in the `utils` directory with the following content:
    ```python
    JIRA_SERVER = 'https://your-jira-instance.atlassian.net'
    JIRA_USER = 'your-email@example.com'
    JIRA_API_TOKEN = 'your-api-token'
    JIRA_PROJECT_KEY = 'PROJECT_KEY'
    ```

2. Create a [.env](http://_vscodecontentref_/1) file in the project root directory with the following content:
    ```
    BASE_URL=https://www.google.co.in/
    USERNAME=testuser
    PASSWORD=testpass
    JIRA_SERVER=https://your-jira-instance.atlassian.net
    JIRA_USER=your-email@example.com
    JIRA_API_TOKEN=your-api-token
    JIRA_PROJECT_KEY=PROJECT_KEY
    ```

## Running Tests

1. To run the tests, execute the following command in the terminal:
    ```sh
    pytest
    ```

2. If a test case fails, a Jira issue will be automatically created with the failure details.

## Project Structure

- [tests](http://_vscodecontentref_/2): Contains the test cases for web and desktop applications.
- [utils](http://_vscodecontentref_/3): Contains utility functions and configuration files.
- [conftest.py](http://_vscodecontentref_/4): Contains pytest hooks for test setup and teardown.