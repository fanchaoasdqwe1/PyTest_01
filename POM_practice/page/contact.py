import time

from selenium.webdriver.common.by import By

from POM_practice.page.base_page import BasePage


class Contact(BasePage):
    def add_member(self):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        # .ww_radio+span:contains("女")
        gender_locator = (By.CSS_SELECTOR, '.member_edit_formWrap>div:nth-child(test_qiyeweixin) .member_edit_item_Radios label:nth-child(2)')
        mobile_locator = (By.NAME, 'mobile')
        self.find(name_locator).send_keys('1qwe')
        self.find(acctid_locator).send_keys('1qwe')
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, '.ww_telInput_zipCode_input_arrowWrap')).click()
        self.find((By.CSS_SELECTOR, 'li[data-index = "229"]')).click()
        self.find(mobile_locator).send_keys('17678787878')