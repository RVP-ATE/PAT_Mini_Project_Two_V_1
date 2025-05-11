from selenium.webdriver.support.ui import WebDriverWait  # Waits for a condition before proceeding
from selenium.webdriver.support import expected_conditions as EC  # Provides common expected conditions
from selenium.common.exceptions import TimeoutException  # Raised when an explicit wait times out
from selenium.common.exceptions import ElementNotVisibleException  # Raised when element is present but not visible
from selenium.common.exceptions import NoSuchElementException  # Raised when element is not found in the DOM

class BasePage:

    def __init__(self, driver):
        self.driver = driver  # Assigns the WebDriver instance
        self.timeout = 15  # Default wait time for elements

    def find_element(self, locator):
        # Waits until the element is present in the DOM and returns it
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR in find_element: ", error)  # Logs error if element not found
            return None

    def is_visible(self, locator):
        # Checks if the element is visible on the page
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return web_element.is_displayed()
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR: ", error)  # Logs error if visibility check fails
            return None

    def is_clickable(self, locator):
        # Checks if the element is clickable
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            return True
        except (TimeoutException, ElementNotVisibleException, NoSuchElementException) as error:
            print("ERROR in is_clickable: ", error)  # Logs error if element isn't clickable
            return False

    def click(self, locator, post_click_locator=None, wait_time=10):
        # Clicks on the element and optionally waits for another element to appear after click
        element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(locator))
        element.click()

        if post_click_locator:
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(post_click_locator))

    def enter_text(self, locator, text):
        # Enters text into a field after clearing it
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def fetch_title(self):
        # Returns the current page title
        return self.driver.title

    def fetch_url(self):
        # Returns the current page URL
        return self.driver.current_url
