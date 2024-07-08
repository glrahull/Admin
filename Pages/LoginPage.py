
from Library import ConfigReader
from selenium.webdriver.common.by import By
from Decorators.Slow import slow_down

class LoginClass:


    def __init__(self,obj):
        global driver
        driver = obj



    @slow_down(3)
    def enter_username(self,username):
        driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "username_name")).send_keys(username)

    @slow_down(3)
    def enter_password(self,password):
        driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "username_password")).send_keys(password)

    @slow_down(3)
    def click_signin(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "signin_button_xpath")).click()



    @slow_down(3)
    def is_login_successful(self):
        try:
            driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","success_indicator_xpath"))
            return True
        except:
            return False