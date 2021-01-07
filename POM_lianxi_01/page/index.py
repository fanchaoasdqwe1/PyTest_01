import time

from selenium.webdriver.common.by import By

from POM_lianxi_01.page.base_page import BasePage


class Index(BasePage):
    def search(self):
        self._driver.find_element(By.CSS_SELECTOR, '#searchText').send_keys('数学')
        self._driver.find_element(By.CSS_SELECTOR, '.search-module input:nth-child(2)').click()



