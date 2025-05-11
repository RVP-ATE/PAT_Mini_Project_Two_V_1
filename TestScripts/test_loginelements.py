import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.conftest import driver
from PageObjects.home_page import HomePage
from TestData.data import Data

def test_login_elements_visible(driver):
    # Wait for the username field to be visible
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.username_input_visibility()
    home_page.password_input_visibility()
    home_page.login_button_visibility()
    home_page.login_button_clickable()