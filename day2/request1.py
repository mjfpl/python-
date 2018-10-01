__author__ = 'computer'
import requests

def requests__res(method, url, datas):
    if method == "get":
        resp = requests.get(url, datas)
    else:
        resp = requests.post(url, datas)

    return [resp.status_code,resp.text]

parmers = [
    {"method":"get",
     "url":"http://47.106.151.165:8080/futureloan/mvc/api/member/login",
     "parmers":{"mobilephone":"17600151411","pwd":"123456789"}
    },
    {
     "method":"post",
     "url":"http://47.106.151.165:8080/futureloan/mvc/api/member/login",
     "parmers":{"mobilephone":"17600151411","pwd":"123456789"}
    }
]
name = {"name":"你哈"}
print(name)
# for item in parmers:
#     print(requests__res(item["method"],item["url"],item["parmers"]))