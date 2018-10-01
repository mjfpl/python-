__author__ = 'computer'

def getmoney_ATM(CardNo,pwd,money):
    if money > 5000 :
        print("家里有矿啊，这么豪！不准取")
        return CardNo
    if len(pwd) < 6 and pwd == "pwd" :
        print("今天真高兴啊去了",money,"钱")
        return CardNo,money
pwd, money = getmoney_ATM("12345","pwd",500)
#print(getmoney_ATM("12345","pwd",500))
print(pwd,money)

number = 10.1
print(type(number))
print(int(number))
int() #转换成整型
str() #转换成字符串
type() #检查变量的数据类型