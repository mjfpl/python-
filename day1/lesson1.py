print("hello world!")

'''
多行注释
'''

# py变量赋值不用加数据类型 自动识别数据类型
name1 = 1
name = "你好"

print('niao'+name)

# 截取字符串 变量名[起始下标：终止下标] - 包含了起始下标对应的值、不包含终止下标对应的值
# 只指明起始 变量名[起始下标：]
# 变量名[：终止下标]
#只取其中一位 变量名[下标] 要去的值的下标就可以
#获取字符串的长度 -- len()
len(name)

print(len(name))

L= [1,2,3,4,5,6,7]
L.reverse() # 倒序
for i in range(len(L)):
    print(L[i])