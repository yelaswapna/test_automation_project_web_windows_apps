# Test Automation Project For Web and Desktop Applications

This repository contains the base setup of a UI testing project using Python, Selenium Webdriver, Pywinauto, and the Page Object Model pattern.

# Requirements

* Python 3.12.3
* pip (24.0) and setuptools
* [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) (recommended)

# Installation

1. Download or clone the repository.
2. Open a terminal.
3. Go to the project root directory.
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment by executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries: `pip install -r requirements.txt`

# Test Execution

1. Open a terminal.
2. From the project root directory, run: `pytest -v --html=reports/report.html`


# Configuration

Environment variables are stored in the `.env` file:


# Results

To check the report, open the `reports/report.html` file once the execution has finished.

# Links

* [Selenium - Python Documentation](https://selenium-python.readthedocs.io/)
* [Webdriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager)
* [Pywinauto Documentation](https://pywinauto.readthedocs.io/)
   
   #
