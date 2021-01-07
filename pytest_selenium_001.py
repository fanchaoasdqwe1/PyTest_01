import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Testbrowser:
    # unittest中的设置方法，该方法在每个方法执行前都会执行一次,可将一些浏览器配置写在该方法
    def setup_method(self):
        # 实例化浏览器  打开谷歌浏览器
        self.driver = webdriver.Chrome()
        # 全屏方式打开
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)
        print('setup_method')

    # unittest中的设置方法，该方法在每个方法执行后都会执行一次
    def teardown_method(self):
        time.sleep(10)
        print('teardown_method')
        self.driver.quit()

    def test_demo01(self):
        # 打开网址
        self.driver.get('https://www.wenduedu.com/')
        # 获得当前浏览器窗口的句柄current_window_handle      返回所有窗口句柄window_handles
        zhuye = self.driver.current_window_handle
        print(zhuye)
        # 使用By方法需要导包
        self.driver.find_element(By.CSS_SELECTOR, '#btnlogin').click()
        # 切换至iframe框，三种写法，可转到方法实现查看。1.name属性    2.下标    3.属性名定位
        self.driver.switch_to.frame('layui-layer-iframe1')
        self.driver.find_element_by_css_selector('#PassportName').send_keys('17600621582')
        self.driver.find_element_by_css_selector('#Password').send_keys('Uu222222')
        # 显示等待，判断登陆按钮是否可以点击
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btnExeLogin')))
        self.driver.find_element(By.CSS_SELECTOR, '#btnExeLogin').click()
        # 等待3秒，鼠标悬停在帐号位置展开下拉列表退出登陆
        time.sleep(3)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('.have-login.top-dropDown')).perform()
        time.sleep(1)
        self.driver.find_element_by_css_selector('.acount-operate a:nth-child(4)').click()
        # 新开窗口打开页面，然后切换浏览器窗口        显示等待 需导两个包
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, '考研精品试听')))
        self.driver.find_element(By.LINK_TEXT, '考研精品试听').click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        # 键盘事件，需导包
        time.sleep(1)
        self.driver.find_element_by_link_text('选课中心').send_keys(Keys.SPACE)
        self.driver.find_element_by_link_text('选课中心').send_keys(Keys.SPACE)
        self.driver.find_element_by_link_text('选课中心').send_keys(Keys.SPACE)


    def test_demo02(self):
        self.driver.get('https://www.baidu.com/')
        list02 = self.driver.find_elements_by_css_selector('#hotsearch-content-wrapper li a span:nth-child(1)')
        a = 1
        while a == 1:
            for i in list02:
                if i.text == '18':
                    i.click()
                    # self._driver.save_screenshot('qwer.png')
                    a = 2
            self.driver.find_element_by_id('hotsearch-refresh-btn').click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_demo03(self):
        self.driver.get('https://www.baidu.com')
        # 显示等待，当这个元素可以被点击时
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#wrapper .mnav.s-top-more-btn a')))
        # 鼠标悬停在该元素
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('#wrapper .mnav.s-top-more-btn a')).perform()
        self.driver.find_element_by_css_selector('#s-top-more [name="tj_mp3"]').click()
        # TODO 当新开页面后，要想操作新页面，必须必须必须切换窗口！！！！！！！
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.tracklist-box.clearfix div:nth-child(1)')))
        self.driver.find_element(By.CSS_SELECTOR, '.tracklist-box.clearfix div:nth-child(1)').click()

