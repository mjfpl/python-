__author__ = 'computer'
a = ['11','22','33','33']
b = ['55','11','22']
# set 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素
# b = set(a)
# print(b)
a_s = set(a)
b_s = set(b)
# 求两个集合的交集 用 & 但是需要先把集合用set 转换一下
print(a_s & b_s)
print(a_s.intersection(b_s))
# 并集
print(a_s | b_s)
print(a_s.union(b_s))
# 求差集  就是两个集合共有的元素去除掉 剩下自己特有的
print(a_s - b_s)
print(b_s - a_s)
print(a_s.difference(b_s))
# 补集合  就是两个集合放到一块减去共有的部分剩下的集合就是补集
# 下面是两种不同的表现形式 都可以
print(a_s.symmetric_difference(b_s))
print(a_s ^ b_s)

c_s = []
for item in a:
    if item in b :
        c_s.append(item)
print(c_s)

