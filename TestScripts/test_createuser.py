import time

from PageObjects.login_page import LoginPage
from PageObjects.admin_page import AdminPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.conftest import driver
from TestData.data import Data

def test_create_and_login_with_new_user(driver):
    driver.get(Data.url)
    # Step 1: Admin logs in
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")
    time.sleep(5)

    # Step 2: Navigate to Admin section and create user
    admin_page = AdminPage(driver)
    admin_page.navigate_to_admin()
    time.sleep(5)
    name = "R"
    new_username = "Pavan"
    new_password = "Pavan@223"
    admin_page.create_user(new_username, new_password, name)
    time.sleep(10)

    # Step 3: Log out
    admin_page.logout()
    time.sleep(10)

    # Step 4: Login with new user
    login_page = LoginPage(driver)  # Re-initiate after logout
    login_page.login(new_username, new_password)
    time.sleep(5)

    # Step 5: Assert dashboard reached
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()