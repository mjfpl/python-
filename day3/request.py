__author__ = 'computer'
import requests

url =requests.get("http://www.baidu.com")
print(url.status_code)
print(url.text)
print(url.encoding)