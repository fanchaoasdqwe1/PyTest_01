from selenium.webdriver.common.by import By

from POM_practice.page.base_page import BasePage


class Register(BasePage):
    def register(self, corpname):
        self.find(By.CSS_SELECTOR, '#corp_name').send_keys(corpname)
        self.find(By.CSS_SELECTOR, '#iagree').click()
        self.find(By.CSS_SELECTOR, '#submit_btn').click()
        return self

    def get_error_message(self):
        result = []
        for element in self.finds((By.CSS_SELECTOR, '.js_error_msg')):
            result.append(element.text)
        return result


