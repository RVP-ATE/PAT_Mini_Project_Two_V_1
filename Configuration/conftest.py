import pytest  # Imports the pytest framework for writing and running tests
from selenium import webdriver  # Imports the Selenium WebDriver module

@pytest.fixture(scope="function")  # Defines a pytest fixture with function-level scope
def driver():
    driver = webdriver.Chrome()  # Initializes a new Chrome browser instance
    driver.maximize_window()  # Maximizes the browser window
    yield driver  # Provides the WebDriver instance to the test and waits until the test is finished
    driver.quit()  # Quits the browser after the test is done
