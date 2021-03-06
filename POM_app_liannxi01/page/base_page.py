import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.DEBUG)
    _driver: WebDriver
    # 黑名单
    _black_list = [
        (By.ID, 'tv_agree'),
        (By.XPATH, '//*[@text="确定"]'),
        (By.XPATH, '//*[@text="下次再说"]')
    ]
    _error_max = 10
    _error_count = 0

    # yaml创建空字典，用来存yaml文件中的动态变量
    _params = {}

    # 构造方法，传参，避免反复重建driver
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)

        try:
            # 寻找控件
            # 三步表达式，如果if后面的条件成立就执行if前面的代码，否则执行else后面的代码
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            # # 如果是一个元组   上面是这些代码的简写
            # if isinstance(locator, tuple):
            #     return self._driver.find_element(*locator)
            # else:
            #     return self._driver.find_element(locator, value)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数（找一个元素一直失败的次数）
            self._error_count += 1
            # 对黑名单的情况进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来的正常控件
                    return self.find(locator, value)
            # 如果黑名单也找不到，直接报错
            logging.warn("在黑名单没有找到数据")
            raise e

    def text(self, key):
        return (By.XPATH, '//*[@text="%s"]' % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

    def find_and_get_text(self, locator, value: str = None):
        print("刚进来")
        logging.info(locator)
        logging.info(value)
        try:
            # 寻找控件
            # 三步表达式，如果if后面的条件成立就执行if前面的代码，否则执行else后面的代码
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
            # # 如果是一个元组   上面是这些代码的简写
            # if isinstance(locator, tuple):
            #     return self._driver.find_element(*locator)
            # else:
            #     return self._driver.find_element(locator, value)
            # 如果成功，清空错误计数
            self._error_count = 0
            print(111)
            print("111" + '--' + element.text)
            return element.text
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数（找一个元素一直失败的次数）
            self._error_count += 1
            # 对黑名单的情况进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来的正常控件
                    return self.find_and_get_text(locator, value)
            # 如果黑名单也找不到，直接报错
            logging.warn("在黑名单没有找到数据")
            raise e

    # 数据驱动的方法
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(step)
                print(step)
                if 'by' in step.keys():
                    element = self.find(step["by"], step["locator"])
                if 'action' in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    # 如果action在这个列表里
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        # 进行批量替换，将yaml文件动态化
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)

