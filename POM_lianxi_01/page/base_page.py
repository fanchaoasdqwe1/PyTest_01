from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.get('https://www.wenduedu.com/')
            self._driver.maximize_window()
        else:
            self._driver = driver
        self._driver.implicitly_wait(5)

    def close(self):
        self._driver.quit()

