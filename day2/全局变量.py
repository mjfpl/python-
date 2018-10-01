__author__ = 'computer'
# 集合 交集 并集 差集  补集

name = ['张三','李四','王五','二狗','狗蛋']
name1 = ['张三','李四','王五','哈哈','嘻哈']

N_s = set(name)
N_s1 = set(name1)
# 交集
print(N_s & N_s1)
# 并集
print(N_s | N_s1)
# 差集
print(N_s - N_s1)
# 补集
print(N_s ^ N_s1)

hello = "你好：%(name)s 我今年：%(age)d" %{'name':'杰克','age':10}
print(hello)
# while 循环
b = 5
while b<10 :
    print("111")
    b+=1

# def east_food(name):
#     if name == "张三" :
#         print("今天吃米线")
#     else:
#         print("今天吃肉肉")
#     return name
# print(east_food("李四"))
#  定义全局变量

name = "你很=帅"

def name_l():
    global name # 这样就可以修改全局变量 修改的变量的值在全局都适用
    name = "李四"
    print("名字是：%s" %name)
name_l()
print(name)
