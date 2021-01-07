import pytest

from POM_app_liannxi01.page.app import App


class TestSearch:
    def setup(self):
            self.mainpage = App().start().main()

    def test_search(self):
        print(1)
        self.mainpage.goto_search_page().search('阿里巴巴')

    @pytest.mark.parametrize('text', (
        '华为',
        '百度',
        '腾讯',
        '白酒'
    ))
    def test_searches(self, text):
        print(1)
        self.mainpage.goto_search_page().search(text)

