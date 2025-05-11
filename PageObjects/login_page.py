from selenium.webdriver.common.by import By  # For locating elements using different strategies (ID, XPATH, etc.)
from TestLocator.locators import Locators  # Locator values are managed separately for maintainability
from PageObjects.base_page import BasePage
from utilities.excel_utilities import get_login_data

class LoginPage(BasePage):
    USER_NAME = (By.NAME, Locators.username_input) # Locator for the username input
    PASSWORD = (By.NAME, Locators.password_input)  # Locator for the password input
    LOGIN_BUTTON = (By.XPATH, Locators.login_btn)  # Locator for the login button
    DASH_BOARD = (By.XPATH, Locators.Admin) # Locator for the Dashboard

    def login(self, username, password):
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)





