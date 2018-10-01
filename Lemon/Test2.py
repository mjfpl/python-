__author__ = 'computer'
#冒泡排序
a = [1,2,3,9,5,4,0]
for i in range(0,len(a)-1):
    for j in range(0,len(a)):
        if j < len(a)-1:
            if a[j] >a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            j += 1
        i += 1
print(a)

# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d "%(i,j,i*j),end='')
    print()

# 登录

name = "admin"
passwd = "123456"
num =1
count = 4
while True:
    name = input("请输入用户名：")
    if name == "admin" :
        while num < 4 :
            pwd = input("请输入密码：")
            if pwd == "123456":
                print("登录成功")
                break
            else:
                num += 1
                if num < 4:
                    count2 =count-num
                    print("密码错误，还剩%d次机会"%count2)
            if num == 4:
                print("次数用完，请稍后登陆")
        break
        break
    else:
        print("用户名错误")



