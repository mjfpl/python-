__author__ = 'computer'
import sys

# 冒泡排序
j = 0
i = 0
nums = [1,7,4,89,34,2]
for j in range(0,len(nums) - 1):
        for i in range(0,len(nums)):
                if i < len(nums) - 1:
                        if nums[i] > nums[i + 1]:
                                nums[i],nums[i + 1]=nums[i + 1],nums[i]
                i += 1
        j += 1

print("冒泡排序调整%s次"%(i))

print("冒泡排序调整后的序列为：%s"%nums)

# 九九乘法表
for i in range(1,10):  #计算行数
    for j in range(1,i+1):  #计算列数
        print("%s * %s = %s"%(i,j,i*j),end="")
    print()
# 足球
# num = 0
# while num < 10:
#     print("Hi,你好欢迎加入足球队，请到旁边填表")
#     sex = input("你的性别是m或f：")
#     if sex == "m" :
#         print("欢迎你小男孩")
#     else:
#         print("欢迎你小女孩")
#     age  = int(input("请说出你的年龄："))
#     if age >= 10 and age <= 12:
#         print("欢迎加入足球队")
#     else:
#         print("很遗憾")
#     num += 1
# print("入围的有%d人"%num)

#第四题
login_info={"username":"admin","passwd":"123456"}
num = 0
num1 = 1
count = 3
while True:
    name = input("请输入用户名：")
    if name == login_info["username"] :
        while num < 3:
            pwd = input("请输入密码：")
            if pwd == login_info["passwd"] :
                print("登陆成功")
                num1 = 1
                sys.exit(0)
            else:
                num += 1
                if num < 3:
                    count2=count - num
                    print("密码错误，你还有%d次机会"%count2)
            if num == 3:
                print("密码输入错误超过三次，青您稍后登录")
            break
        break
    else:
        print("用户名错误")