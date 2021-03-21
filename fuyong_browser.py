from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemoClass_01:
    def test_demo_01(self):
        # 使用已经存在的浏览器进程
        # 命令行需要输入的语句，端口号可以随便写，但是不能被使用：chrome --remote-debugging-port=9222
        chrome_options = Options()
        # self.options.add_argument("--headless")  # 过程无窗口显示
        # 这个写法报错  chrome_options.add_experimental_option('debuggerAddress', '127.0.0.test_qiyeweixin:9222')
        chrome_options.debugger_address = '127.0.0.test_qiyeweixin:9222'      # 复用浏览器
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.find_element_by_id('menu_contacts').click()

        # 上面那种需要额外导包。这种不需要
    def test_demo_02(self):
        chrome_options_02 = webdriver.ChromeOptions()
        chrome_options_02.debugger_address = '127.0.0.test_qiyeweixin:9222'
        self.driver = webdriver.Chrome(options=chrome_options_02)
        # todo 解决浏览器缩放后定位不准的问题。 用js 注意引号中别输错，括号也好注意
        self.driver.execute_script('arguments[0].click();', self.driver.find_element_by_css_selector('.index_service_cnt.js_service_list a:nth-child(test_qiyeweixin)'))
        # self.driver.find_element_by_css_selector('.index_service_cnt.js_service_list a:nth-child(test_qiyeweixin)').click()