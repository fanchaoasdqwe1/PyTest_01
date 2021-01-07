from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        # 如果是一个元组
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)


