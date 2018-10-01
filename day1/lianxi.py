__author__ = 'computer'
a=[1,2,'6','summer']
if 'i' in a:
    print(True)
else:
    print('不在')

dict_1={"class_id":45,'num':1}

if dict_1['num']>=5:
   print("课堂人数大于五")
else:
    print("不大于5")
# print(dict_1['num']>=5)

# 列表
name = ["张三","李四","王五"]
# 取列表中的值 用 列表名[这个要取得值的位置] name[0]  取name列表中的第一个值
for item in name:
    print(item)
    #获取列表的长度
    print(len(name))
# print(name[0])
# 字典 遍历字典中的键值对
zidian = {"name":"李四","age":12}
# 这样子出来是元祖的形式
for item in zidian.items():
    print(item)

# 还可以用key value 遍历
for key,val in zidian.items():
    print(key,val)

