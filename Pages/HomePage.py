from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Library import ConfigReader
from Decorators.Slow import slow_down

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @slow_down(3)
    def click_users_button(self):
        try:
            users_button_xpath = ConfigReader.fetchelementLocators("HomePage", "users_button")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, users_button_xpath))
            ).click()
            print("Clicked on Users button")
        except Exception as e:
            print(f"Failed to click on Users button: {e}")
            raise  # Re-raise the exception to mark the test as failed

    @slow_down(3)
    def click_add_user(self):
        try:
            add_user_xpath = ConfigReader.fetchelementLocators("HomePage", "add_user")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, add_user_xpath))
            ).click()
            print("Clicked on Add User button")
        except Exception as e:
            print(f"Failed to click on Add User button: {e}")
            raise  # Re-raise the exception to mark the test as failed

    # Add additional methods to interact with elements on the HomePage as needed
