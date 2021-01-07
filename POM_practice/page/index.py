from selenium.webdriver.common.by import By

from POM_practice.page.base_page import BasePage
from POM_practice.page.login import Login
from POM_practice.page.register import Register


class Index(BasePage):
    _base_url = 'https://work.weixin.qq.com/'

    def goto_register(self):
        self.find(By.LINK_TEXT, '立即注册').click()
        return Register(self._driver)

    def goto_login(self):
        self.find((By.LINK_TEXT, '企业登录')).click()
        return Login(self._driver)