import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sockshandler import is_ip

from PageObjects.base_page import BasePage
from TestLocator.locators import Locators


class DashboardPage(BasePage):

    # Dictionary mapping menu names to their corresponding XPATH locators
    menu_items = {
        "Admin": (By.XPATH, Locators.Admin),
        "PIM": (By.XPATH, Locators.PIM),
        "Leave": (By.XPATH, Locators.Leave),
        "Time": (By.XPATH, Locators.Time),
        "Recruitment": (By.XPATH, Locators.Recruitment),
        "Myinfo": (By.XPATH, Locators.MyInfo),
        "Performance": (By.XPATH, Locators.Performance),
        "Dashboard": (By.XPATH, Locators.Dashboard)
    }

    def is_menu_clickable(self, menu_name):
        # Wait until the specified menu item is clickable
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_items[menu_name])
        )
        # Return whether the element is displayed
        return element.is_displayed()