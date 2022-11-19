from urllib.request import build_opener
from requests import Session
from ujson import loads
opener = build_opener()
session = Session()


def urllib_test():
    content = opener.open("https://httpbin.org/get")
    print(loads(content.read()))


def requests_test():
    content = session.get("https://httpbin.org/get")
    print(loads(content.text))


print("Urllib:")
urllib_test()
print("Requests:")
requests_test()
