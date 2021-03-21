from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from POM_practice.page.base_page import BasePage
from POM_practice.page.contact import Contact
from POM_practice.page.material import Material
from POM_practice.page.message import Message


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def download(self):
        pass

    # 主页-导入通讯录
    def import_user(self, path):
        self.find((By.CSS_SELECTOR, '.index_service .index_service_cnt a:nth-child(2)')).click()
        self.find((By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask')).send_keys(path)
        self.find((By.CSS_SELECTOR, '[class="qui_btn ww_btn ww_btn_Large ww_btn_Blue ww_fileImporter_submit"]')).click()
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Big.ww_btn_Blue')))
        self.find((By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Big.ww_btn_Blue')).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ['aaa', 'bbbb']

    def add_member(self):
        # WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.index_service_cnt.js_service_list a:nth-child(test_qiyeweixin)')))
        self.find((By.CSS_SELECTOR, '.index_service_cnt.js_service_list a:nth-child(test_qiyeweixin)')).click()
        return Contact(self._driver)

    # 主页-前往管理-素材库
    def goto_tool_material(self):
        self.find((By.CSS_SELECTOR, '#menu_manageTools')).click()
        print(11)
        self.find((By.CSS_SELECTOR, '#js_manageTools_index>div>ul>li:nth-child(5)>a')).click()
        return Material(self._driver)

    # 主页-消息群发
    def goto_send_qun_message(self):
        self.find((By.CSS_SELECTOR, '.index_service_cnt.js_service_list a:nth-child(4)')).click()
        return Message(self._driver)
