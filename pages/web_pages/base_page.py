class BasePage:
    """A base class for all page objects."""

    def __init__(self, driver):
        """Initialize the BasePage with a WebDriver instance."""
        self.driver = driver

    def open_url(self, url):
        """Open a URL in the browser."""
        self.driver.get(url)

    def find_element(self, by, value):
        """Find a single web element."""
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        """Find multiple web elements."""
        return self.driver.find_elements(by, value)

    def click_element(self, by, value):
        """Click on a web element."""
        self.find_element(by, value).click()

    def enter_text(self, by, value, text):
        """Enter text into an input field."""
        self.find_element(by, value).send_keys(text)

    def get_element_text(self, by, value):
        """Get the text of a web element."""
        return self.find_element(by, value).text

    def is_element_displayed(self, by, value):
        """Check if a web element is displayed."""
        return self.find_element(by, value).is_displayed()
