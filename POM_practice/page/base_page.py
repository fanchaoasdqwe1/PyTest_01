from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ''
    # _driver: WebDriver   不写的话close类中无法找到driver方法            reuse:是否复用已有的浏览器进程
    def __init__(self, driver: WebDriver = None, reuse=False):
        # index页面会使用这个
        if driver is None:
            # 如果reuse为true，复用已有浏览器，否则新开浏览器
            if reuse:
                # 命令行需要输入的语句，端口号可以随便写，但是不能被使用：chrome --remote-debugging-port=9222
                chrome_options = webdriver.ChromeOptions()
                chrome_options.debugger_address = '127.0.0.1:9222'
                self._driver = webdriver.Chrome(options=chrome_options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
        # login与register等页面需要用这个办法
        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator=''):      # 星号元组或列表可以拆分数据     可穿两个参数或传一个元组类型的参数
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def finds(self, locator):      # 星号元组或列表可以拆分数据
        return self._driver.find_elements(*locator)

    def close(self):
        sleep(20)
        self._driver.quit()
