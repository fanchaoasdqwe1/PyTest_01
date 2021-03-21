import requests
from pprint import pprint

from requests import Session, Response

proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888"
}
url_get = "http://httpbin.testing-studio.com/get"


def test_get():
    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      data={
                          "a": 1,
                          "b": 2,
                          "c": "asd"
                      }, headers={"Content-Type": "application/fanfanfanfan"}
                      , cookies={"name": "fanchaoaaaaaaaaaa"})
    print(r.json())
    print(1)
    print(r.headers["Content-Type"])
    assert r.status_code == 200


def test_post1():
    r = requests.post("https://httpbin.testing-studio.com/post", data={"a": 123, "b": 321, "c": "abcde"},
                      params={"a": 1, "b": 2, "c": "ccccc"})
    print(r.json())
    assert r.status_code == 200


# 文件上传
def test_upload():
    r = requests.post("http://httpbin.testing-studio.com/post",
                      files={"file": open("__init__.py", "rb")}, )
    print(r.json())
    assert r.status_code == 200


def test_session():  # session要导包
    s = Session()
    s.proxies = proxies
    s.verify = False
    s.get(url_get)

def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):  # Response要导包
        #r.content = "OK HOOK HAHAHA "
        r.demo = "demodemodemodemodemodemodemodemodemodemodemodemo"
        return r
    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccccc"
                     }, hooks={"response": [modify_response]})
    print(r.json())
    print(r.demo)
    assert r.status_code == 200


def test_upload111():
    r = requests.get(
        "http://study-test.wendu.com/api/studyrecord/latestlessoninfobycappid?cappid=100016&ver=1.0&appid=100016&sign=a046cca1788d050dcdd8ad45c4467613&time=20210320225342&userid=2016761&platform=1")
    print(r.json())
