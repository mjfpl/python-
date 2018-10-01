__author__ = 'computer'
# # 列表里面可以放任何类型对的数据 元素与元素之间用逗号隔开
num_1 = ['你好',1]
# # 索引下标从零开始
print(num_1[0])
# #split() 根据传入指定的字符去进行切割,切割完成后的数据类型就是列表
# .split(指定的字符，指定切割次数)
# name = 'zhangsan,lisi,wangwu'
# names = name.split(',')  不指定切割次数，就默认全部切割
# print(names)
name = '22 22 2 2 '
print(name.split( ))
# strip() 去除头和尾指定的字符，只能去除字符串头跟尾不能去除中间的
name1 = "lisi"
print(name1.strip("l"))
print(name1.strip("i"))
#字符串拼接用+拼接 只能拼接字符串，类型不同不能拼接
name3 =name+name1
print(name3)
# srt() 这个函数可以把变量转换成字符串类型
# int() 只能转整型 可以把数字类型的字符串转换成整型
# 格式化字符串输出
people = 'xiaoqiang'
age = 20
float1 = 99.0000
# 格式化多个字符串 %f 浮点型(默认精确到后六位) %.2f 这样意思是小数点保留两位
print('我是%s今年%d岁%.2f'%(people,age,float1))
print("我是{},今年{}".format(people,age))
# format() 格式化输出字符串  需要用{}来占位  .format() 这样来格式化 里面放变量 {}里面的变量可以随意指定但是不能越界
print("我是{0},今年{1}".format(people,age))
print("我是{0},今年{0}".format(people,age))
print("我是{1},今年{1}".format(people,age))
# {} 不指定的话默认按顺序输出，也可以指定输出。但是不能超过变量的数量，下标从0开始
# {} 这个不指定的{} 要跟后面的变量数量一致
print('我是{}今年{}岁'.format(people,age))
# 列表里面可以放任何类型的数据 关键字list 标志[]
# 列表可以用 .append() 添加元素 .insert(指定的位置，value) 插入指定位置  .extend() 合并列表
# .pop()默认删除列表最后一个元素
# .clear() 删除列表里面的所有元素
# 还能给列表重新赋值
name = ['name']
name.append("你好") #这个是默认追加在列表的末尾
name.insert(0,"李四") # 可以再指定的位置插入值 .insert(索引,插入的值)
print(name.extend(num_1)) # 合并两个列表
name.pop(0)
name.pop() # 默认删除最后一个值
name.clear() #清楚列表的所有值
print(name)
# 嵌套列表 取值
num = [[1,2,1],[2,2,2]]
# 第一次取值[1,2,1] 第二次从[1,2,1]这里面取值
print(num[1][2])
# 元祖里面的值不能修改 元祖必须有两个值 否则构不成元祖
name4 = (1,2,2,3)
# name = (1) 这样子是错误的类型不会是元祖
#name5 =(1) 这样写出来的元祖是错的
name6 = (1,) # 元祖最少必须两个字符
# 字典
name5 = {"name":'李四',"age":20}
# 增加
name5['work']='test'
# 修改
name5['name']='王五'
# 删除
name5.pop('name')
print(name5)

str = "helloword"

print(str[1:2])
print(str[-1])
print(str[1:])
print(str[:5])


str.upper()
str.replace('h','k')
str.lower()
str.find("h")
str.split() #字符串切割
str.strip() # 去头去尾
# 列表 字典的怎删改  .append() 增加  .insert() 插入  .extend() 合并列表  .pop()删除列表数据  .clear() 清除列表全部数据库