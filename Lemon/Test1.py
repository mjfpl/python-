__author__ = 'computer'
# 运算符
#算术运算符 + - * /  % 取余就是计算商
# 取余运算
print(6 % 2 )
#比较运算符： < > >= <= != ==
# 运算结果是布尔值 True False
# 例子
a = 8
b = 10
print(a == b)

# 赋值运算符 += -= +
a += 1
a = a+1

# 逻辑运算符 and  or
# and 必须两个条件都成立
# or 一个条件符合就成立

#成员运算符 in not in
c = 'hello'
b = 'll'
print(c in b )

# if 条件分支语句
# if 条件表达式：
    # 代码块
num = 10
if num > 0:
    print("你很厉害")
else:
    print("嫌弃")

color = 'red'
if color == 'red':
    print('红灯停')
elif color == 'yellow':
    print('黄灯等一等')
else:
    print('绿灯行')

# else 后面不能加条件
# elif 后面必须跟条件

#如果数据为空 就是 false
# 不为空就是true
a = []
if a :
    print("打印")
else:
    print("不打印")

# for item in datas  语法
# 用for循环取字典里的数据 用items() 这个方法可以获取字典里面的键跟值  。value获取值
name = {'name':'李四','age':20}
for key,val in name.items():
    print(key,val)
for val in name.items():
    print(val)
for key in name: # 获取键
    print(key)
for val in name.values(): # 获取值
    print(val)
# rang(m.n,k) m开始 n 结束 K步长  去m的值但是取不到n的值  俗称取左不取右
for item in range(1,5):
    print(item)

# 倒序输出列表
L=[1,2,3,4]
n = [1,2,3,4]
L.reverse() # 把列表转成倒序 这个只能把列表转成倒序
for item in L:
    print(item)
for i in range(-1,-5,-1):
    print(n[i])
# 双重for循环
# 九九乘法表
for m in range(1,10):
    for i in range(1,m+1):
        print("%s * %s = %s"%(m,i,m*i),end='')
    print()