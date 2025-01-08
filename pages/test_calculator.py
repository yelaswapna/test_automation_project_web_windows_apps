import pytest
#from pages.desktop_pages.calculator_page import CalculatorPage

@pytest.fixture(scope="module")
def calculator():
    """Fixture to initialize and terminate the Calculator application."""
    calc = CalculatorPage("C:\\Windows\\System32\\calc.exe")  # Path to Calculator app
    yield calc  # Provide the CalculatorPage instance to tests
    calc.close_calculator()

def test_addition(calculator):
    """Test the addition functionality of the calculator."""
    result = calculator.perform_addition(2, 3)
    assert result == "5", f"Expected result to be 5 but got {result}"

def test_subtraction(calculator):
    """Test the subtraction functionality of the calculator."""
    calculator.click_button("5")
    calculator.click_button("Subtract")
    calculator.click_button("2")
    calculator.click_button("Equals")
    result = calculator.get_result()
    assert result == "3", f"Expected result to be 3 but got {result}"

def test_multiplication(calculator):
    """Test the multiplication functionality of the calculator."""
    calculator.click_button("4")
    calculator.click_button("Multiply by")
    calculator.click_button("3")
    calculator.click_button("Equals")
    result = calculator.get_result()
    assert result == "12", f"Expected result to be 12 but got {result}"

def test_division(calculator):
    """Test the division functionality of the calculator."""
    calculator.click_button("8")
    calculator.click_button("Divide by")
    calculator.click_button("2")
    calculator.click_button("Equals")
    result = calculator.get_result()
    assert result == "4", f"Expected result to be 4 but got {result}"
