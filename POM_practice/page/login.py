from selenium.webdriver.common.by import By

from POM_practice.page.base_page import BasePage
from POM_practice.page.register import Register


class Login(BasePage):
    def scan_qrcode(self):
        pass

    def goto_registry(self):
        self.find((By.LINK_TEXT, '企业注册')).click()
        return Register(self._driver)