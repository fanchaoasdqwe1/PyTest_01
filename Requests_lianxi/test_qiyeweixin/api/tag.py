import requests

from Requests_lianxi.test_qiyeweixin.api.base_api import BaseApi
from Requests_lianxi.test_qiyeweixin.api.wework import WeWork


class Tag(WeWork):
    secret = "Yk-zuf3-um8wJYr0V9CwhPSRdxbf6PzpY9-pfkBSWi8"

    # 获取所有标签
    def get(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list'
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json={'tag_id': []}
        )
        self.format(r)
        return r.json()

    # 添加一个标签
    def add(self, name):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag'
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json={
                'group_id': 'eti6UeCAAA7HHXZCZR1zb8krhrj021pQ',
                'tag': [
                    {'name': name}
                ]}
        )
        self.format(r)
        return r.json()

    def update(self):
        pass

    # 删除一个标签 根据tag_id或者group_id删除
    def delete(self, tag_id=[], group_id=[]):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json={
                'group_id': group_id,
                'tag_id': tag_id}
        )
