from urllib.request import build_opener
from requests import Session
from ujson import loads
opener = build_opener()
session = Session()


def urllib_test():
    opener.addheaders.append(("test", "Testing urllib"))
    content = opener.open("https://httpbin.org/post", data=b"test")
    print(loads(content.read()))


def requests_test():
    content = session.post("https://httpbin.org/post", data="test", headers={"test": "Testing requests"})
    print(loads(content.text))


print("Urllib:")
urllib_test()
print("Requests:")
requests_test()
