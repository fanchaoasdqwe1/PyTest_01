
from Requests_lianxi.test_qiyeweixin.api.tag import Tag


class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    # 获取标签
    def test_get(self):
        r = self.tag.get()

    # 添加一个标签
    def test_add(self):
        r = self.tag.add('demo_01')
        assert r["errcode"] == 0

    # 删除一个标签，断言是否成功
    def test_delete(self):
        name = 'demo_01'
        # 获取所有标签，使用jsonpath定位到想要删除的标签的id
        r = self.tag.get()
        tag_id = self.tag.jsonpath(r, f"$..tag[?(@.name=='{name}')]")[0]['id']
        # 调用删除方法
        self.tag.delete(tag_id)
        assert r["errcode"] == 0



