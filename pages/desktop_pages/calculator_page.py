from pywinauto.application import Application

class CalculatorPage:
    """Page object class for the Calculator application."""

    def __init__(self, app_path):
        """Initialize the CalculatorPage with the application path."""
        self.app = Application().start("C:\\Windows\\System32\\calc.exe")
        self.window = self.app.window(title="Calculator")  # Adjust title based on your app

    def click_button(self, button_text):
        """Click a button on the calculator."""
        self.window[button_text].click()

    def get_result(self):
        """Retrieve the result displayed on the calculator."""
        return self.window["Result"].texts()[0]

    def perform_addition(self, num1, num2):
        """Perform an addition operation."""
        self.click_button(str(num1))
        self.click_button("Add")
        self.click_button(str(num2))
        self.click_button("Equals")
        return self.get_result()

    def close_calculator(self):
        """Close the calculator application."""
        self.app.kill()
