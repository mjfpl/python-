__author__ = 'computer'
#函数 def 函数名（）：
#       代码块
#函数的参数
#1.位置参数/形参，函数可以有多个参数 也可以没有参数
#2.定函数的时候 有几个传参数 那好 那么调用就要传递几个参数！不要多也不要少
#3.默认参数 必须放在位置参数的后面，如果有默认参数，这个参数就可以不用传递 （默认参数如果不进行赋值的话，会输出默认的值）
#4.默认参数可以有多个
#5.函数调用要按顺序给参数赋值
#6.调用函数的时候，可以有一个返回值 return 加一个变量
#7.return 也可以看做是函数的结尾
#6.调用函数的时候可以强制指定参数，也就是不用考虑参数的位置 例子：
def people(name,age):
    print("你好%s，今年%d岁"%(name,age))
people(age=20,name="张三")

#正常的函数
def people(name,age):
    print("你好%s，今年%d岁"%(name,age))
people('张三',20)

#计算1-100的总数
n = 0
for i in range(101):
     n =n+i
print(n)

def sum(x):
    n = 0 #储存总和的一个变量
    for i in range(x+1):
     n =n+i
    return n
sum(100)

# login_info={"username":"admin","passwd":"123456"}
# print(login_info['username'])
#
# user = input("请输入用户名：")
# if user != login_info['username'] or user=="":
#     print("请输入正确的用户名")
# else:
#     print("成功")