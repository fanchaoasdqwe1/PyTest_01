import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from POM_app_liannxi01.page.base_page import BasePage
from POM_app_liannxi01.page.main_page import MainPage


class App(BasePage):
    _appPackage = "com.xueqiu.android"
    _appActivity = "com.xueqiu.android.view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "123123123"
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            caps["android:exported"] = True
            # caps["noReset"] = True
            caps["dontStopAppOnReset"] = True  # 的如果app已经启动，不杀掉它
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            print(self._driver)
            # todo: kill app     start app
            self._driver.start_activity(self._appPackage, self._appActivity)

        return self

    def main(self) -> MainPage:
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source
            if "我的" in source:
                return True
            if "同意" in source:
                return True
            return False
        WebDriverWait(self._driver, 30).until(wait_load)
        return MainPage(self._driver)


