import pickle
import os
from importlib.metadata import files

from PageObjects.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration.conftest import driver
from TestData.data import Data


COOKIE_PATH = "cookies.pkl"

def test_login_and_save_cookie(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    with open(COOKIE_PATH, "wb") as file:
        pickle.dump(driver.get_cookies(),file)

    assert os.path.exists(COOKIE_PATH)

def test_cookie_login(driver):
    driver.get(Data.url)  # You must open the domain before adding cookies
    driver.delete_all_cookies()

    if os.path.exists(COOKIE_PATH):
        with open(COOKIE_PATH, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Failed to add cookie: {cookie['name']}, error: {e}")

        driver.refresh()

        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url.lower()
    else:
        raise FileNotFoundError("cookies.pkl not found. Run test_login_and_save_cookie first.")