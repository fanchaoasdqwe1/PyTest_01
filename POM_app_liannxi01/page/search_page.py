from appium.webdriver.common.mobileby import MobileBy

from POM_app_liannxi01.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, search_text='123'):
        self.find(MobileBy.ID, 'search_input_text').send_keys(search_text)
        self.find(MobileBy.ID, 'search_input_text').click()  # 解决输入搜索内容后有时不会自动获取联想内容的情况
        self.find(MobileBy.ID, 'name').click()
        self.find(MobileBy.XPATH, '//*[contains(@text,"取消")]').click()

        # todo 代表传参为str类型，返回值为float类型
    def aaa(self, shujv: str) -> float:
        pass
