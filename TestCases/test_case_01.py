import time
from Library import ConfigReader
from selenium.webdriver.common.by import By
from Base import InitiateDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages import LoginPage, HomePage
import pytest
import openpyxl
from DataGenerate import DataGen
from Decorators import Slow


@pytest.mark.parametrize('data', DataGen.dataGenerator())

def test_validatelogin(data):
    driver = InitiateDriver.startBrowser()

    login = LoginPage.LoginClass(driver)
    login.enter_username(data[0])
    login.enter_password(data[1])
    login.click_signin()
    HomePage.c

    try:
        WebDriverWait(driver,30).until(
            EC.visibility_of_element_located((By.XPATH,"/html/body/div/div[1]/div/ul/li[2]/div/div[2]/span"))
        )
        print("login successful!")

        # Instantiate HomePage class
        home_page = HomePage(driver)

        # Use methods from HomePage instance with explicit waits
        home_page.click_users_button()
        print("Clicked on Users button")

        home_page.click_add_user()
        print("Clicked on Add User button")

        # Add assertions or further actions as needed after clicking the buttons

    # Add assertions or further actions as needed after clicking the buttons

    except AssertionError as ae:
        print(f"AssertionError: {ae}")
    except Exception as e:
        print(f"Login or clicking buttons failed: {e}")

    finally:
        pass