__author__ = 'computer'
# 字符串拼接 %s 代表传递的值是字符串 不用逗号隔开 直接 % +要拼接的字符串就好 也可以拼接 数字 列表
# %.4s 截取字符串 数字可以随意改变
print('I am %.2s my hobby is lanqiu' % 'jason')
print('I am %s my hobby is lanqiu' % 'jason')
print('I am %s my hobby is lanqiu' % 1)
# %d 数值类型必须是 数字
print('I am %s my hobby is lanqiu' %500)
# 打印浮点数 小数 .2 是后面保留几位小数 f表示小数
float1 = "打印浮点数：%.2f" %99.00000
print(float1)
# 打印出 % h号
float1 = "打印浮点数：%.2f %%" %99.00000
print(float1)
# 如果后面的值是一个字典咋的取值呢
people_info = "名字：%(name)s 年龄: %(age)d" % {"name": "jason", "age": 20}
print( people_info )