__author__ = 'computer'
import random
# 第一题目
# num = 0
# for i in range(0,10):
#     sex = str(input("你的性别是："))
#     age = int(input("你的年龄是："))
#     if 10<= age <= 12:
#         num += 1
#         print("恭喜你")
#     else:
#         print("很遗憾你没能通过")
#print("一共通过了%s"%num)

# 第二题
number1 = int(input("请输入一个四位的整数:"))
a = (number1/1000+5)%10
b = ((number1-a*1000)/100+5)%10
c = ((number1-a*1000-b*100)/10+5)%10
d = (number1%10+5)%10
new_num = d*1000+c*100+b*10+a
print(int(new_num))
#第三题
# print("这件商品多少钱")
# money = int(input("服务员："))
# if  50<= money <= 100:
#     money = money - money*(1/10)
#     print("这件商品打折后为：%s，折扣为%d%% " %(money,float(1/10) * 100))
# elif money > 100:
#     money = money - money*(2/10)
#     print("这件商品打折后为：%s，折扣为%d%% " %(money,float(2/10) * 100))
# else:
#     print("这件商品不打折")

# 第四题
# rm = random.randint(1, 9)
# print(rm)
# print("咱们来玩猜拳吧 ！")
# num = int(input("请输入:"))
# if num > rm :
#     print("bigger")
# elif num < rm :
#     print("less")
# else:
#     print("equal")