import pytest
from selenium.common import NoSuchElementException

from Pages import PosLogin
from Base import InitiateDriver
from DataGenerate import PosLoginData

@pytest.mark.parametrize("PosData", PosLoginData.dataGenerator())
def test_pos_login(PosData):
    driver = InitiateDriver.startBrowser('Application_URL2')
    login = PosLogin.PosLoginNumber(driver)

    login.click_login()
    login.click_on_mobile_no_box(PosData[0])
    login.click_on_get_otp()
    login.enter_otp(PosData[1])
    login.term_condiation()
    login.click_on_submit()

    InitiateDriver.closeBrowser()
