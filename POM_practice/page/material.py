import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from POM_practice.page.base_page import BasePage


class Material(BasePage):
    def goto_image_import(self, image_path):
        self.find((By.CSS_SELECTOR, '#profile_navigation>ul>li:nth-child(3)>a')).click()
        self.find((By.LINK_TEXT, '添加图片')).click()
        self.find((By.CSS_SELECTOR, '#js_upload_input')).send_keys(image_path)
        time.sleep(3)
        self.find((By.LINK_TEXT, '完成')).click()

