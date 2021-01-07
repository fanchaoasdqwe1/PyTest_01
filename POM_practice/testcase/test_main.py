from POM_practice.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member()
        # assert 'aaa' in main.import_user()
        # main.add_member().add_member("xxx")
        # assert 'aaa' in main.import_user().get_message()

    # 导入通讯录功能测试
    def test_import_user(self):
        self.main.import_user('D:\\Fc_xiangmu\\PyTest_01\\POM_practice\\files\\通讯录批量导入模板.xlsx')
        # 断言是否成功
        # assert 'success' in main.get_message()

    # 主页-前往管理-素材库-图片上传测试
    # todo 注意路径要转义！！！！！！！！！      r或者\\
    def test_import_image(self):
        self.main.goto_tool_material().goto_image_import(
            r'D:\Fc_xiangmu\PyTest_01\POM_practice\files\5331179_093221399136_2.jpg')
        # 断言是否成功
    # assert 'success' in main.get_message()

    # 测试主页消息群发功能
    def test_send_qun_message(self):
        self.main.goto_send_qun_message().send(app='公告', group='aa', title='我是标题1号',
                                               content='短的时间款福克斯绝代风华数控刀具粉红色', author='周树人')

    # def test_send_message(self):
    #      # 传入一个文件
    #      main.send_message()
    #      # 断言是否成功
    #      assert 'success' in main.get_message()
