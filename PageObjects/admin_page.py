import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import keys_to_typing

from PageObjects.base_page import BasePage
from TestLocator.locators import Locators


class AdminPage(BasePage):
    ADMIN_MENU = (By.XPATH, Locators.Admin)
    ADD_USER_BUTTON = (By.XPATH, Locators.add_user_button)
    USER_ROLE = (By.XPATH, Locators.user_role)
    USER_SELECT = (By.XPATH, Locators.user_select)
    USER_ADMIN = (By.XPATH, Locators.user_admin)
    USER_DROPDOWN = (By.XPATH, Locators.user_dropdown)
    STATUS = (By.XPATH, Locators.status)
    STATUS_SELECT = (By.XPATH, Locators.status_select)
    STATUS_ENABLED = (By.XPATH, Locators.status_enabled)
    EMPLOYEE_NAME = (By.XPATH, Locators.employee_name)
    USERNAME_FIELD = (By.XPATH, Locators.username_field)
    PASSWORD_FIELD = (By.XPATH, Locators.password_field)
    CONFIRM_PASSWORD_FIELD = (By.XPATH, Locators.confirm_password_field)
    SAVE_BUTTON = (By.XPATH, Locators.save_button)
    LOGOUT = (By.XPATH, Locators.logout)

    def navigate_to_admin(self):
        """
        Navigates to the Admin page by clicking the Admin menu item.
        """
        self.click(self.ADMIN_MENU)

    def create_user(self, username, password, employee):
        """
        Creates a new user in the Admin section using provided username, password, and employee name.
        """
        self.click(self.ADD_USER_BUTTON)

        # Click on the 'Add' button to add a new user

        time.sleep(5)  # Static wait for UI stability (can be replaced with better waits)

        # Select 'Admin' from the User Role dropdown
        self.click(self.USER_ROLE)
        time.sleep(2)

        element = self.find_element(self.USER_SELECT)
        element.send_keys(Keys.DOWN)
        time.sleep(2)

        element = self.find_element(self.USER_ADMIN)
        element.send_keys(Keys.ENTER)
        time.sleep(2)

        # Select 'Enabled' from the Status dropdown
        self.click(self.STATUS)
        time.sleep(2)

        # Select status from dropdown
        status_select = self.find_element(self.STATUS_SELECT)
        status_select.send_keys(Keys.DOWN)
        time.sleep(2)

        # Confirm selection
        status_enabled = self.find_element(self.STATUS_ENABLED)
        status_enabled.send_keys(Keys.ENTER)
        time.sleep(2)

        # Enter employee name and select from auto-suggestion

        self.enter_text(self.EMPLOYEE_NAME, employee)
        time.sleep(2)

        employee_name_field = self.find_element(self.EMPLOYEE_NAME)
        if employee_name_field:
            employee_name_field.send_keys(Keys.DOWN)
            time.sleep(1)
            employee_name_field.send_keys(Keys.ENTER)
        time.sleep(2)

        # Fill in username and password fields
        self.enter_text(self.USERNAME_FIELD, username)
        time.sleep(2)
        self.enter_text(self.PASSWORD_FIELD, password)
        time.sleep(2)
        self.enter_text(self.CONFIRM_PASSWORD_FIELD, password)
        time.sleep(2)

        # Click the Save button to create the user
        self.click(self.SAVE_BUTTON)

    def logout(self):
        try:
            # Wait and click on user dropdown
            self.click(self.USER_DROPDOWN)
            time.sleep(2)
            # Wait and click on logout button
            self.click(self.LOGOUT)
            time.sleep(5)

        except Exception as e:
            print(f"Logout failed: {e}")



