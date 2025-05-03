from selenium.webdriver import Chrome, Firefox
from Library import ConfigReader

driver = None  # Declare globally

def startBrowser(url_key='Application_URL'):
    global driver
    browser = ConfigReader.readConfigData('Details', 'Browser')
    url = ConfigReader.readConfigData('Details', url_key)

    if browser == 'chrome':
        driver = Chrome()
    elif browser == 'firefox':
        driver = Firefox()
    else:
        driver = Chrome()

    driver.get(url)
    driver.maximize_window()
    return driver

def closeBrowser():
    global driver
    if driver:
        driver.quit()
