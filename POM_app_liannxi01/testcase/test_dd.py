from POM_app_liannxi01.page.app import App
from POM_app_liannxi01.page.base_page import BasePage


class TestDD:
    def test_dd(self):
        base = BasePage()
        # base.steps("../files/steps.yaml")
        base.steps(r"D:\Fc_xiangmu\PyTest_01\POM_app_liannxi01\files\steps.yaml")

    def test_search(self):
        App().start().main().goto_search_page().search_shujvqudong("tengxun")