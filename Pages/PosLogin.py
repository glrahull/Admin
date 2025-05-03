from Library import ConfigReader
from selenium.webdriver.common.by import By
from Decorators.Slow import slow_down
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PosLoginNumber:

    def __init__(self, driver):
        self.driver = driver


    @slow_down(3)
    def click_login(self):
        self.driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Poslogin","login_button_xpath")).click()
    @slow_down(5)
    def click_on_mobile_no_box(self,mobile_no):
        self.driver.find_element(by=By.ID,value=ConfigReader.fetchelementLocators("Poslogin","mobile_no_input_id")).send_keys(mobile_no)
    @slow_down(5)
    def click_on_get_otp(self):
        self.driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Poslogin", "get_otp_button_xpath")).click()
    @slow_down(5)
    def enter_otp(self,otp):
        self.driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Poslogin","enter_otp_xpath")).send_keys(otp)
    @slow_down(5)
    def term_condiation(self):
        self.driver.find_element(by=By.ID,value=ConfigReader.fetchelementLocators("Poslogin","terms_condiation_id")).click()
    @slow_down(5)
    def click_on_submit(self):
        self.driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Poslogin","submit_button_xpath")).click()