from Requests_lianxi.test_qiyeweixin.api.groupchat import GroupChat
from Requests_lianxi.test_qiyeweixin.api.wework import WeWork

# 客户群接口
class TestWeWork:
    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()

    # 获取客户群列表
    def test_groupchat_get(self):
        r = self.groupchat.list(limit=10)
        r["errcode"] == 0

    # 获取客户群列表，随便加参数
    def test_groupchat_get_gai(self):
        r = self.groupchat.list(limit=10, fanchao="fanchao")
        r["errcode"] == 0

    # 获取客户群详情
    def test_groupchat_detail(self):
        r = self.groupchat.list(limit=10)
        r["errcode"] == 0
        chat_id = r["group_chat_list"][0]["chat_id"]
        r = self.groupchat.get(chat_id)
        print(r)


