import requests


# 将接口请求的过程 定义成函数 -- 只考虑get请求、post请求
def send_reqeust_and_get_resp(method, url, datas):
    if method == "get":
        resp = requests.get(url, datas)
    else:
        resp = requests.post(url, datas)

    return [resp.status_code, resp.text]

#get  发送一个get请求，接收它的返回值
#用一个变量来接收返回值
#测试数据 - 成功注册
# url = "http://120.79.176.157:8080/futureloan/mvc/api/member/register"
# params = {"mobilephone":"18655220004","pwd":"1234567890"}
#
# # #发送一个get请求
# # response = requests.get(url,params)
# # #获取响应数据
# # print(response)
# # #获取 响应数据
# # print(response.text)
# # #获取响应状态 码
# # print(response.status_code)
#
# print(send_reqeust_and_get_resp("get",url,params))
# print("=========================================")


# #测试数据 --成功 - 带昵称
# url_1 = "http://120.79.176.157:8080/futureloan/mvc/api/member/register"
# params_1 = {"mobilephone":"18655220001","pwd":"1234567890","nickname":"hello"}
# # resp = requests.post(url_1,params_1)
# #
# # print(resp)
# # #获取 响应数据
# # print(resp.text)
# # #获取响应状态 码
# # print(resp.status_code)
# print(send_reqeust_and_get_resp("post",url_1,params_1))


# #测试数据 - 注册失败  - 手机号码没有11位
# url_1 = "http://120.79.176.157:8080/futureloan/mvc/api/member/register"
# params_1 = {"mobilephone":"186552200","pwd":"1234567890"}
#
# resp = requests.post(url_1,params_1)
#
# print(resp)
# #获取 响应数据
# print(resp.text)
# #获取响应状态 码
# print(resp.status_code)

datas = [
    {
        "method":"get",
        "url":"http://120.79.176.157:8080/futureloan/mvc/api/member/register",
        "req_data":{"mobilephone":"18655220001","pwd":"1234567890","nickname":"hello"}
     },
    {
        "method":"get",
        "url":"http://120.79.176.157:8080/futureloan/mvc/api/member/register",
        "req_data":{"mobilephone":"1865522","pwd":"1234567890","nickname":"hello"}
    }

]

for item in datas:
    res = send_reqeust_and_get_resp(item["method"],item["url"],item["req_data"])
    print(res)


