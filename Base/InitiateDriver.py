import time

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader


def startBrowser():
    global driver
    if ((ConfigReader.readConfigData('Details', 'Browser')) == 'chrome'):
        driver = Chrome()

    elif ((ConfigReader.readConfigData('Details', 'Browser')) == 'firefox'):
        driver = Firefox()
    else:
        driver = Chrome()
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver


def closeBrowser():
    driver.close(10)
