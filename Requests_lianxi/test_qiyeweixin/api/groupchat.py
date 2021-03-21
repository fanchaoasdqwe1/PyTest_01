import requests

from Requests_lianxi.test_qiyeweixin.api.wework import WeWork


class GroupChat(WeWork):
    secret = "Yk-zuf3-um8wJYr0V9CwhPSRdxbf6PzpY9-pfkBSWi8"

    def list(self, limit, **kwargs):
        json = {"limit": limit}
        print(json)
        json.update(kwargs)
        print(json)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(url,
                          params={"access_token": self.get_token(self.secret)},
                          json=json)
        self.format(r)
        print(r.url)
        return r.json()

    def get(self, chat_id):
        url1 = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(url1,
                          params={"access_token": self.get_token(self.secret)},
                          json={"chat_id": chat_id})
        self.format(r)
        return r.json()
