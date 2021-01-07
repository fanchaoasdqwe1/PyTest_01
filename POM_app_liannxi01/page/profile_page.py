from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from POM_app_liannxi01.page.base_page import BasePage


class ProfilePage(BasePage):
    def login_by_password(self, phone, passport):
        # WebDriverWait(self._driver).until(EC.element_to_be_clickable((By.XPATH, '//*[@text="帐号密码登录"]')))
        # self.find(By.XPATH, '//*[@text="帐号密码登录"]').click()
        self.find(By.ID, 'rl_login').click()

        self.find(By.ID, 'login_account').send_keys(phone)
        self.find(By.ID, 'login_password').send_keys(passport)
        self.find(By.ID, 'button_next').click()
        msg = self.find(By.ID, 'md_content').text
        self.find(By.ID, 'md_buttonDefaultPositive').click()
        return msg
