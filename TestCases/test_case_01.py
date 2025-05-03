
import pytest
from Pages import LoginPage
from Base import InitiateDriver
from DataGenerate import DataGen
import allure



# @pytest.mark.parametrize('data', DataGen.dataGenerator())
# def test_combined(data):
#     # Run the first test case
#     driver = InitiateDriver.startBrowser()
#
#     # Test login functionality


@pytest.mark.parametrize('data', DataGen.dataGenerator())

def test_validatelogin(data):
    driver = InitiateDriver.startBrowser()

    login = LoginPage.LoginClass(driver)
    login.enter_username(data[0])
    login.enter_password(data[1])
    login.click_signin()

    assert login.is_login_successful()

    # Wait for some time if needed
    # time.sleep(2)

    # Now, run the second test case without closing the browser
    # login.mis_button()
    # login.advisory_box()
    # login.select_advisor()
    # login.product_select()
    # login.select_product()
    # login.subproduct_dropdown()
    # login.select_subproduct()
    # login.vehicletype_dropdown()
    # login.select_vehicletype()
    # login.business_type()
    # login.select_business()
    # login.f_name()
    # login.l_name()
    # login.previous_insurance_select()
    # login.select_prev_insurance_company()
    # login.policy_plan()
    # login.previous_policy_num()
    # login.current_policy_num()
    # login.policy_pickup()
    # login.policy_issue_date()
    # login.policy_start_date()
    # login.policy_expiry_date()
    # login.email_address()
    # login.payment_mode()
    # login.payment_mode_select()
    # login.enter_bank_name()
    # login.enter_ncb()
    # login.enter_od_amount()
    # login.enter_tp_amount()

    driver.quit()