import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestXueQiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "123123123"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
        # caps["automationName "] = "uiautomator2"    # 默认使用uiautomator2
        caps["android:exported"] = True
        caps["noReset"] = True
        # caps["ensureWebviewsHavePages"] = True
        caps["dontStopAppOnReset"] = True   # 的如果app已经启动，不杀掉它
        # caps["unicodeKeyBoard"] = True  # 输入非英文
        caps["resetKeyBoard"] = True    # 输入完成后重置输入法
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_aaa(self):
        print(111 + '--' + "element.text")

        # self.driver.find_element(By.XPATH, '//*[@text="下次再说"]').click()





















