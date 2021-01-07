from POM_lianxi_01.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_search(self):
        self.index.search()


    def teardown(self):
        self.index.close()