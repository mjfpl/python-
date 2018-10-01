__author__ = 'computer'

# 字典
ni_info = {'name':'哈哈','work':'test','age':18}
# 往字典添加值
ni_info['city'] = "南京"
# 往字典里面更新值
ni_info.update({"身高":180})
# 更新字典里面的值
ni_info['name'] = "张三"
print(ni_info['name'])
len(ni_info)
print(ni_info)
# for 循环
for item in ni_info:
    print(item)
# 元祖 值不可以更改 通过下标来取值
yuna_zu = ('name',1)
print(yuna_zu[1])
list = [1,2,3,4]
# if else 分支
if 2 in list:
    print('beautiful')
else:
    print("将2添加进去")
    list.append(2)
    print()

# 多个条件 if else
name = "娃娃"
num = 2
if num >= 3 and name == '娃娃':
    print('很好')
elif num >=2 :
    print('非常好')
else:
    print('不好')

name = ['lisi','zhangsan','hha']

for item in name:
    print(item)
    if item == 'zhangsan':
      print('张三你好啊')
      break
# 函数 range(起始数，终止数，每次递增的数) range(0,10,2) 只能试数字 range(5) #[0,1,2,3,4]
for item in range(5):
    print(item)
# 利用range 来遍历列表
for item in range(len(name)):
   # print(item)
    print(name[item])
# 遍历字典
for key,value in ni_info.items():
      print(key,value)
# 函数
'''
 def 函数名称（）
    #实现功能的代码
'''
def cup():
    print("放水")

cup()
# 定义函数 函数一定要有返回值 通过print来调用函数
def sum(a,b):
    temp = a + b
    return temp

print(sum(1,2))



# OPENPYXL  requests  函数的传参