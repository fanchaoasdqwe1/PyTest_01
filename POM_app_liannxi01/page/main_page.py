from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from POM_app_liannxi01.page.base_page import BasePage
from POM_app_liannxi01.page.profile_page import ProfilePage
from POM_app_liannxi01.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search_page(self):
        self.find(MobileBy.ID, 'home_search').click()
        return SearchPage(self._driver)

    def goto_profile(self):
        self.find(By.XPATH, '//*[@text="我的"]').click()
        return ProfilePage(self._driver)




