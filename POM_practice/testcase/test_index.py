from POM_practice.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_register().register('我是直接进来的')

    def test_login(self):
        register_page = self.index.goto_login().goto_registry().register('我是从二维码页面进来的')
        print(register_page.get_error_message())
        print("|".join(register_page.get_error_message()))
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
