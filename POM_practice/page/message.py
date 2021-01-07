import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from POM_practice.page.base_page import BasePage


class Message(BasePage):
    def send(self, app='', content='', group='', title='', author=''):
        self.find((By.LINK_TEXT, "选择需要发消息的应用")).click()
        self.find((By.CSS_SELECTOR, '.ww_bubble[data-name*="%s"]' % app)).click()
        self.find((By.LINK_TEXT, "确定")).click()
        self.find((By.LINK_TEXT, "选择发送范围")).click()
        actions = ActionChains(self._driver)
        element = self.find((By.CSS_SELECTOR, "body"))
        actions.move_to_element(element).perform()
        # element = self._driver.find_elements_by_css_selector(By.CSS_SELECTOR, '.ww_searchInput_text')[-1]
        # element.send_keys(group)
        # self.find((By.ID, "memberSearchInput")).click()
        # self.find((By.ID, "memberSearchInput")).send_keys()
        self._driver.find_element(By.ID, "memberSearchInput").click()
        self._driver.find_element(By.ID, "memberSearchInput").send_keys(group)
        self.find((By.CSS_SELECTOR, '#searchResult li:nth-child(1)')).click()
        self.find((By.LINK_TEXT, "确认")).click()
        self.find((By.CSS_SELECTOR, '.ww_editorTitle.js_announcement_title.ww_compatibleTxt_ipt')).send_keys(title)
        ifream = self._driver.find_element_by_tag_name('iframe')
        self._driver.switch_to.frame(ifream)
        self.find((By.CSS_SELECTOR, '.view.msg_noticeEditor_frameBody p')).send_keys(content)
        time.sleep(3)
        self._driver.switch_to.default_content()
        self.find((By.CSS_SELECTOR, '.qui_inputText.ww_inputText.msg_input_WidthNoBorder.js_amrd_sendName')).send_keys(author)
        self.find((By.LINK_TEXT, "发送")).click()
        self.find((By.LINK_TEXT, "确定")).click()








       # self.find((By.CSS_SELECTOR, "#1688850822758488_anchor")).click()



    def get_history(self):
        pass