import time

from appium.webdriver.common.mobileby import MobileBy

from POM_app_liannxi01.page.base_page import BasePage


class SearchPage(BasePage):
    # 搜索功能，普通po封装
    def search(self, search_text):
        self.find(MobileBy.ID, 'search_input_text').send_keys(search_text)
        time.sleep(2)
        self.find(MobileBy.ID, 'search_input_text').click()  # 解决输入搜索内容后有时不会自动获取联想内容的情况
        self.find(MobileBy.ID, 'name').click()
        # self.find(MobileBy.XPATH, '//*[contains(@text,"取消")]').click()
        return self

    # 搜索功能，数据驱动方式的写法
    def search_shujvqudong(self, search_text):
        self._params = {}
        self._params["key"] = search_text
        self.steps("../files/search.yaml")
        return self

        # todo 代表传参为str类型，返回值为float类型
    def aaa(self, shujv: str) -> float:
        pass

    def add_select(self):
        element = self.find_by_text("加自选")
        element.click()
        print(1)
        return self

    def get_msg(self):
        print(3)
        time.sleep(3)
        element = self.find_and_get_text(MobileBy.ID, 'followed_btn')
        print(element)
        return element
