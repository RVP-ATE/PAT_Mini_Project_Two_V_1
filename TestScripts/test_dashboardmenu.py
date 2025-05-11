import time
from PageObjects.login_page import LoginPage
from PageObjects.dashboardpage import DashboardPage
from Configuration.conftest import driver
from TestData.data import Data


def test_dashboard_menus(driver):
    driver.get(Data.url)
    # Perform login using valid credentials
    LoginPage(driver).login("Admin", "admin123")

    # Initialize the DashboardPage object
    dashboard = DashboardPage(driver)

    # Temporary wait to ensure the dashboard page loads (consider replacing with WebDriverWait)
    time.sleep(5)

    # List of menu items to check on the dashboard
    menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "Myinfo", "Performance", "Dashboard"]

    # Loop through each menu item and assert if it's clickable
    for menu in menus:
        # Assert that the menu is clickable; print status accordingly
        assert dashboard.is_menu_clickable(menu), f"[❌ ERROR] Menu '{menu}' is not clickable."
        print(f"[✅ CHECKED] Menu '{menu}' was checked and is clickable.")
