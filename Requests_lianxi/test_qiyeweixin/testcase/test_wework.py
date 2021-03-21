from Requests_lianxi.test_qiyeweixin.api.wework import WeWork


class TestWeWork:
    @classmethod  # 装饰器        获取token
    # todo 注：开启代理工具后请求https接口报错
    def setup_class(cls):
        cls.token = WeWork.get_token()

    def test_get_token(self):
        r = WeWork.get_access_token(WeWork.secret)
        print(r)

    def test_get_token_exist(self):
        assert self.token is not None