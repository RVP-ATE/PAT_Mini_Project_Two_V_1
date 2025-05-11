import pytest
import time
from selenium import webdriver
from PageObjects.home_page import HomePage
from Configuration.conftest import driver
from TestData.data import Data

# Test to verify that the correct URL is opened
def test_home_url(driver):
    # Open the OrangeHRM login page
    driver.get(Data.url)
    # Create an instance of the HomePage with the driver
    home_page = HomePage(driver)
    home_page.validate_homepage_url()
    # Wait briefly to ensure the page has fully loaded (can be replaced with an explicit wait)
    time.sleep(2)
    # Verify that the URL contains 'orangehrmlive'
    assert "orangehrmlive" in driver.current_url

