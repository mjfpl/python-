
num = 1
# while循环 %d 十进制整数
while num <= 3:
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name == ("root") and pwd == ("123456"):
        print("胜利")
        break
    else:
        print("请重新输入还有%d次机会"%(3-num))
    num += 1