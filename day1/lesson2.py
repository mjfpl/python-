__author__ = 'computer'

team = ['大胖','小胖','中胖']
print('张三' in team)
# 列表里面的数据是有序的、可以被修改
# 网列表里面追加数据用.append
team.append('李四')
print(team)
# 根据下标来list里面取值 下标从0开始
print(team[1])
# 重新赋值列表里面的值
team[1] = '小胖子'
print(team[1])
print(team[1:])
# 往list里面插入数据
team.insert(1,'你好')
print(team)
# 获取列表的长度
len(team)
print(len(team))
# 取最后一个值
team[-1]
print(team[-1])

# in not in 的用法 在或不在那个集合里面
print(1 in team)


# 算术运算符 = + - * / %取余
# 逻辑运算符 == >= <= !=
# in not  boolean 布尔类型  or and
# += -=

count = 30
count = count +50 # 相当于 count += 30

print(count)