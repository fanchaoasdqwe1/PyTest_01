import pytest
import yaml

from POM_app_liannxi01.page.app import App


class TestSearch:
    def setup(self):
            self.mainpage = App().start().main()

    def test_search(self):
        print(1)
        self.mainpage.goto_search_page().search('阿里巴巴')

    @pytest.mark.parametrize('text', (
        '华为',
        '百度'
    ))
    # 参数化
    def test_searches(self, text):
        print(1)
        self.mainpage.goto_search_page().search(text)

    @pytest.mark.parametrize('text', yaml.safe_load(open(r"D:\Fc_xiangmu\PyTest_01\POM_app_liannxi01\files\data.yaml")))
    # 数据驱动
    def test_searches02(self, text):
        print(1)
        self.mainpage.goto_search_page().search(text)

    # 测试搜索-添加自选-判断是否添加
    def test_select(self):
        assert "已添加" in self.mainpage.goto_search_page().search('阿里巴巴').add_select().get_msg()

