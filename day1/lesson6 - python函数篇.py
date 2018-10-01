#Author: xiaojian
#Time: 2018/8/4 11:21

'''
函数：
1、实现了单一的功能
2、重复使用

定义函数：
def 函数名称():
    #实现功能的代码

调用函数：
函数名称()
'''
#水杯-定义
def cup():
    print("盛水！！！")

#调用 =函数的使用
cup()
#一个小时
cup()
#三个小时
cup()


def add():
    a = 50
    b = 33
    print(a + b)


#ATM机 -- 取钱
'''
输入：
1、银行卡
2、密码
3、金额

几种反应：
1、把钱取出来  ---交易完成   ---输出 ：返回：银行卡、人民币
2、银行卡钱不够  --- 输出：银行卡
'''

#定义一个功能 --指有几个参数要传给我
def getMoney_fromATM(cardNo,passwd="123456",money=1000):
    if money > 5000:
        print("超额了！！不支持,退卡！！")
    elif len(passwd) != 6:
        print("密码长度必须为6位！！")
    else:
        print("卡号：",cardNo,"密码：",passwd ,"   取了：",money,"元钱")
    print("ATM取钱功能")

def getMoney_fromATM_v2(cardNo,passwd="123456",money=1000):
    if money > 5000:
        print("超额了！！不支持,退卡！！")
        return cardNo

    if len(passwd) != 6:
        print("密码长度必须为6位！！")
    else:
        print("卡号：",cardNo,"密码：",passwd ,"   取了：",money,"元钱")
        return [cardNo,money]


#使用功能 ：调用函数
#youyou : 000011112222  123456  2000
#lx : 222233330000    123234    1500
# #位置参数 - 必需传
# getMoney_fromATM("000011112222","123456",2000)  # ---有地方可以让我输入一些数据
# #默认参数
# getMoney_fromATM("222233330000","123234")
# getMoney_fromATM("111155556666")
# #指定参数：  参数名=值
# getMoney_fromATM("000044443300",money=2500)

#主动接收函数的返回值。 --  拿着返回值，有别的用处。
# card_1 = getMoney_fromATM_v2("000000000000","11223",5500)
# print(card_1)
# data = getMoney_fromATM_v2("000000000000","123456",2000)
# print(data)

#len()
#range()
#str() -- 转换成字符串
a = 123456.123
print(type(a))
b = str(a)
print(b)
#判断数据类型  -- type()
print(type(b))

c = [1,2,3,4]
d = {"hello":"world"}
print(type(c))
print(type(d))

f = "1234"
int(f)
float(f)