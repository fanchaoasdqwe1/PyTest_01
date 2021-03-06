import json
import logging

import yaml
from jsonpath import jsonpath
from requests import Request


class BaseApi:
    # json代码布局美化版本   .两种写法。   indent=2表示缩进2
    @classmethod
    def format(cls, r):
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    # 封装jsonpath，可以避免频繁的导入它
    def jsonpath(self, r, path):
        return jsonpath(r, path)

    # 数据驱动的方法
    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            request: Request = None
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