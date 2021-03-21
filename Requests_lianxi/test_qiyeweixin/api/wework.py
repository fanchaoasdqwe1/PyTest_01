import json
from datetime import datetime

import requests

from Requests_lianxi.test_qiyeweixin.api.base_api import BaseApi


class WeWork(BaseApi):
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww9ab1cc08be938ac6"
    token = dict()
    token_time = dict()
    secret = "Yk-zuf3-um8wJYr0V9CwhPSRdxbf6PzpY9-pfkBSWi8"

    @classmethod
    def get_token(cls, secret=secret):
        if secret is None:
            # 制度发生变化，在这个地方决定是否重新获取
            return cls.token[secret]
        # 获取token 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
            cls.token_time[secret] = datetime.now()
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(cls.token_url, params={"corpid": cls.corpid, "corpsecret": secret})
        cls.format(r)
        return r.json()



