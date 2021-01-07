from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

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
            caps["noReset"] = True
            caps["dontStopAppOnReset"] = True  # 的如果app已经启动，不杀掉它
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            print(self._driver)
            # todo: kill app     start app
            self._driver.start_activity(self._appPackage, self._appActivity)

        return self

    def main(self) -> MainPage:
        return MainPage(self._driver)


