import yaml


class TestYAML:
    def test_yaml(self):
        print(yaml.load("""
        - a
            - a1
            - a2
            - a3
        - b
        - c
        """))
