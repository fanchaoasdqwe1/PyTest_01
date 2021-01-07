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

    def teardown(self):
        time.sleep(5)
        print('quit')
        self.driver.quit()

    # 滑动界面方法
    def test_scroll(self):
        # 获取界面尺寸
        print(self.driver.get_window_rect())
        asd = self.driver.get_window_rect()
        for i in range(5):
            TouchAction(self.driver).long_press(x=asd['width']*0.5, y=asd['height']*0.8)\
                .move_to(x=asd['width']*0.5, y=asd['height']*0.2).release().perform()
        # assert float(a) >= 100

    # android-uiautomator定位。滑屏小技巧
    def test_scroll02(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("2小时前").instance(0));'
        )
        self.driver.find_element(*scroll_to_element).click()

    def test_caozuo(self):
        # app放到后台
        #self.driver.background_app(5)
        self.driver.lock(10)    # 模拟锁屏
        #self.driver.unlock()   # 模拟解锁

    # 作业2   打开搜索，输入内容，点击第一个，点击股票
    def test_zuoye2(self):
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, 'search_input_text').click()  # 解决输入搜索内容后有时不会自动获取联想内容的情况
        self.driver.find_element(MobileBy.ID, 'name').click()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="股票"]').click()
        # xpath定位练习
        aaa = self.driver.find_element(MobileBy.XPATH,
                                        '//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]')
        # 打印resourceid 使用get_attribute方法
        print(aaa.get_attribute('resourceid'))
        print(aaa.get_attribute('class'))
        print(aaa)
        print(aaa.text)
        assert float(aaa.text) >= 200

    # 作业3   打开搜索，输入内容，点击第一个，点击股票，加入自选股，重新进入上述操作，然后判断是否添加成功
    def test_zuoye3(self):
        bianhao = 'BK2466'
        self.driver.find_element(MobileBy.ID, 'home_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.ID, 'search_input_text').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                         '//*[contains(@resource-id,"listview")]/android.widget.RelativeLayout[1]')))
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@resource-id,"listview")]/android.widget.RelativeLayout[1]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.TextView[@text="股票"]').click()
        button01 = self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='%s']/../../../android.widget.LinearLayout[last()]/android.widget.TextView" % bianhao)
        state01 = button01.get_attribute('text')
        if state01 == '加自选':
            button01.click()
            time.sleep(5)
            self.driver.find_element(MobileBy.XPATH,
                                     '//*[@text="取消"]').click()
            self.driver.find_element(MobileBy.ID, 'home_search').click()
            self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
            self.driver.find_element(MobileBy.ID, 'search_input_text').click()
            self.driver.find_element(MobileBy.XPATH,
                                     '//*[contains(@resource-id,"listview")]/android.widget.RelativeLayout[1]').click()
            self.driver.find_element(MobileBy.XPATH,
                                     '//android.widget.TextView[@text="股票"]').click()
            button02 = self.driver.find_element(MobileBy.XPATH,
                                              "//*[@text='%s']/../../../android.widget.LinearLayout[last()]/android.widget.TextView" % bianhao)
            state02 = button02.get_attribute('text')
            assert state02 == '已添加'
        elif state01 == '已添加':
            assert state01 == '已添加'
        else:
            print('没有这个值')

    # 内嵌H5
    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="A股开户"]').click()
        phone = (MobileBy.XPATH, "//*[@text='获取验证码']/../android.view.View[1]/android.widget.EditText")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(phone))
        self.driver.find_element(*phone).click()
        self.driver.find_element(*phone).send_keys("17600621582")
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='获取验证码']/../android.widget.EditText").send_keys('123456')
        # 解决输入法遮挡界面的问题，点击某个元素或点击某个像素位置
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"开户服务由东方财富")]').click()
        TouchAction(self.driver).press(x=444, y=666).perform()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="立即开户"]').click()
        print(self.driver.find_element(MobileBy.XPATH, '//*[@text="获取验证码"]/../android.view.View[5]/android.view.View').text)
        asd = self.driver.get_window_rect()
        for i in range(3):
            TouchAction(self.driver).long_press(x=asd['width'] * 0.5, y=asd['height'] * 0.8) \
                .move_to(x=asd['width'] * 0.5, y=asd['height'] * 0.2).release().perform()
        self.driver.find_element(MobileBy.ID, 'action_back').click()

















