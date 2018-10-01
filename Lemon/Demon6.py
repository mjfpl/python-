__author__ = 'computer'
import sys

#计算投币的金额
def count_money(money):
    drink_money =[]
    count = 0
    for item in money:
        drink_money.insert(0,item)
    for item in drink_money:
        count = count+item
    return count

pop1 ={'橙汁':3,'椰汁':4,'矿泉水':2,'早餐奶':4}
#存钱的列表
money = []
# 存放果汁的列表
count_gj = []
print("我们去买果汁吧")
while True:
    money1 = input('请投币：')
    if money1.isdigit():
        if int(money1) != 1 and int(money1) != 5 and int(money1) != 10:
            print("只接受1,5,10元的纸币，退出：%d"%(int(money1)))
        else:
            money2 =int(money1)
            money.insert(0,money2)
            count_money =count_money(money)
            print("一共投了%d钱"%(count_money))
            drink = input('请选择饮料（橙汁，椰汁，矿泉水，早餐奶）：')
            money3 =pop1[drink]
            count1 = count_money -money3
            if count1 == 0:
                print("请收好您的%s"%(drink))
            else:
                print("找您%d块钱"%(count1))
                sys.exit(0)
else:
    print('请重新投币')





