import requests

from Requests_lianxi.test_qiyeweixin.api.wework import WeWork


class Department(WeWork):
    secret = 'iBrL4ecsU-uA6UemBwhlIhMx7Hb5-D3xBBbw6fkDU8k'

    def create(self, name, parentid, **kwargs):
        data = {'name': name, 'parentid': parentid}
        data.update(kwargs)
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(base_url, params={'access_token': WeWork.get_token(self.secret)}, json=data)
        return r.json()

    def update(self, id, **kwargs):
        data = {'id': id}
        data.update(kwargs)
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        r = requests.post(base_url, params={'access_token': WeWork.get_token(self.secret)}, json=data)
        return r.json()

    def delete(self, id):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(base_url, params={'access_token': WeWork.get_token(self.secret), 'id': id})
        return r.json()

    def get(self, id=1):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r = requests.get(base_url, params={'access_token': WeWork.get_token(self.secret), 'id': id})
        return r.json()