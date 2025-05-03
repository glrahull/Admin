
from Library import ConfigReader
from selenium.webdriver.common.by import By
from Decorators.Slow import slow_down

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginClass:


    def __init__(self,obj):
        global driver
        driver = obj



    @slow_down(3)
    def enter_username(self,username):
        driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "username_name")).send_keys(username)


    @slow_down(5)
    def enter_password(self,password):
        driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "username_password")).send_keys(password)

    @slow_down(5)
    def click_signin(self):
        driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "signin_button_xpath")).click()

    @slow_down(5)
    def is_login_successful(self):
        try:
            wait = WebDriverWait(driver, 10)  # wait for max 10 seconds
            wait.until(EC.visibility_of_element_located((
                By.XPATH, ConfigReader.fetchelementLocators("Login", "success_indicator_xpath")
            )))
            print("Login Successful")
            return True
        except Exception as e:
            print(f"Login unsuccessful. Reason: {e}")
            return False

    # @slow_down(5)
    # def mis_button(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","mis_button_xpath")).click()
    #
    # @slow_down(20)
    # def advisory_box(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","advisor_xpath")).send_keys("9944280809")
    #
    # @slow_down(20)
    # def select_advisor(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login", "select_advisor_xpath")).click()
    #
    # @slow_down(3)
    # def product_select(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","product_xpath")).click()
    #
    # @slow_down(3)
    # def select_product(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","select_product_xpath")).click()
    #
    # @slow_down(5)
    # def subproduct_dropdown(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","subproduct_xpath")).click()
    #
    # @slow_down(10)
    # def select_subproduct(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","select_subproduct_xpath")).click()
    #
    # @slow_down(10)
    # def vehicletype_dropdown(self):
    #     driver.find_element(by=By.XPATH,
    #                         value=ConfigReader.fetchelementLocators("Login", "vehicletype_xpath")).click()
    #
    # @slow_down(10)
    # def select_vehicletype(self):
    #     driver.find_element(by=By.XPATH,
    #                         value=ConfigReader.fetchelementLocators("Login", "select_vehicletype_xpath")).click()
    #
    # @slow_down(10)
    # def business_type(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","businesstype_xpath")).click()
    #
    # @slow_down(10)
    # def select_business(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","select_businesstype_xpath")).click()
    #
    # @slow_down(10)
    # def f_name(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","first_name_name")).send_keys("Rahul")
    #
    # @slow_down(10)
    # def l_name(self):
    #     driver.find_element(by=By.NAME, value=ConfigReader.fetchelementLocators("Login", "last_name_name")).send_keys("Kumar")
    #
    # @slow_down(10)
    # def previous_insurance_select(self):
    #     driver.find_element(by=By.XPATH, value=ConfigReader.fetchelementLocators("Login", "previous_insurance_company_xpath")).click()
    #
    # @slow_down(10)
    # def select_prev_insurance_company(self):
    #     driver.find_element(by=By.XPATH, value=ConfigReader.fetchelementLocators("Login", "select_prev_insurance_company_xpath")).click()
    #
    # @slow_down(10)
    # def policy_plan(self):
    #     driver.find_element(by=By.NAME, value=ConfigReader.fetchelementLocators("Login","policy_plan_name")).send_keys("Comprehensive")
    #
    # @slow_down(10)
    # def previous_policy_num(self):
    #     driver.find_element(by=By.NAME, value=ConfigReader.fetchelementLocators("Login", "prev_policy_number_name")).send_keys("COMP3843874")
    #
    # @slow_down(10)
    # def current_policy_num(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "current_policy_number_name")).send_keys("COMP384939493874")
    #
    # @slow_down(10)
    # def policy_pickup(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","policy_pick_up_date_xpath")).send_keys("26/07/2024")
    #
    # @slow_down(10)
    # def policy_issue_date(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "policy_issue_date_name")).send_keys("26/07/2024")
    #
    # @slow_down(10)
    # def policy_start_date(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "policy_start_date_name")).send_keys("26/07/2024")
    #
    # @slow_down(10)
    # def policy_expiry_date(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login", "policy_expiry_date_name")).send_keys("25/07/2025")
    #
    # @slow_down(5)
    # def mobile_number(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","mobile_number_name")).send_key("9053267217")
    #
    # @slow_down(5)
    # def email_address(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","email_address_name")).send_keys("rahul@gmail.com")
    #
    # @slow_down(5)
    # def payment_mode(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","payment_mode_xpath")).click()
    #
    # @slow_down(5)
    # def payment_mode_select(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","payment_mode_select_xpath")).click()
    #
    # @slow_down(5)
    # def policy_pickup(self):
    #     driver.find_element(by=By.XPATH,value=ConfigReader.fetchelementLocators("Login","tranction_date_xpath")).send_keys("19/07/2024")
    #
    # @slow_down(5)
    # def tranction_number(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","tranction_id_name")).send_keys("TRANC342552")
    #
    # @slow_down(5)
    # def enter_bank_name(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","type_bank_name")).send_keys("State Bank Of India")
    #
    # @slow_down(5)
    # def enter_ncb(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","enter_ncb_name")).send_keys("25")
    #
    # @slow_down(5)
    # def enter_od_amount(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","enter_od_amount_name")).send_keys("500")
    #
    # @slow_down(5)
    # def enter_tp_amount(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","enter_tp_amount_name")).send_keys("500")
    #
    # @slow_down(5)
    # def enter_net_amount(self):
    #     driver.find_element(by=By.NAME,value=ConfigReader.fetchelementLocators("Login","enter_net_premium_name")).send_keys("1000")