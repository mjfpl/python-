__author__ = 'computer'
import sys
import random
# make_shirt()
def make_shirt(size,font):
    print("T 恤的尺码是:%d,样式是:%s"%(size,font))

make_shirt(20,'繁体')

# describe_city()
def describe_city(city,contury="中国"):
    print("%s is in %s"%(city,contury))

contury_city = [{"city":"海南"},{"city":"长安"},{"city":"纽约","contury":"美国"}]
# print(contury_city[2]["contury"])
# describe_city('伦敦',"英国")
n = 1
for item in range(2):
    describe_city(contury_city[item]["city"])
    n += 1
    if n == 3:
        describe_city(contury_city[2]["city"],contury_city[2]["contury"])

# city_country()
def city_country(city,country):
    return [city,country]
country_city = [{"city":"海南","country":"中国"},{"city":"长安","country":"中国"},{"city":"纽约","country":"美国"}]
for item in range(3):
    list = city_country(country_city[item]['city'],country_city[item]['country'])
    print("%s,%s"%(list[0],list[1]))

# make_album()
def make_album(music,album):
    return {"music":music,"album":album}

make_album1 = [{"music":"凉凉","album":"哈哈"},{"music":"三天三夜","album":"你好"},{"music":"不知道","album":"嗯"}]
for item in range(3):
    music = make_album(make_album1[item]['music'],make_album1[item]['album'])
    print(music['music'],music['album'])

# 制作三明治
def make_sandwich(sandwich):
    food = []
    for item in range(len(sandwich)):
        food.append(sandwich[item])
    print("这个三明治的食材有：")
    for item in range(len(food)):
        print("%s " % (food[item]), end="")
    print()
sandwich = ['洋葱','生菜','三文鱼']
make_sandwich(sandwich)

# 初级型题目：
# 小学僧考试
def student_score(score):
    if score <60:
        print("不及格")
    elif score>=60 and score<=80:
        print("良好")
    elif score>=80 and score<=100:
        print('优秀')
    else:
        print("成绩输入有误")

student_score(100)

# 公司发奖金
def bonus_info(money):
        if money <= 100000:
            money = money*1/10
            print("奖金：%d"%(money))
        elif money >100000 and money <= 200000 :
            money =100000*1/10+(money-100000)*3/40
            print("奖金：%d"%(money))
        elif money > 200000 and money<= 400000:
            money =100000*1/10+100000*3/40+(money-200000)*1/20
            print("奖金：%d"%(money))
        elif money > 400000 and money <= 600000 :
            money =100000*1/10+100000*3/40+200000*1/20+(money-400000)*3/100
            print("奖金：%d"%(money))
        elif money > 600000 and money <= 1000000:
            money =100000*1/10+100000*3/40+200000*1/20+200000*3/100+(money-600000)*3/200
            print("奖金：%d"%(money))
        else:
            money =100000*1/10+100000*3/40+200000*1/20+200000*3/100+400000*3/200+(money-1000000)*1/1000
            print("奖金：%d"%(money))
# 调用函数
while True:
    num = input("请输入这个月的利润：")
    if num.isdigit() == True:
        if int(num) > 0:
          bonus_info(int(num))
        sys.exit(0)
    else:
        print("请重新输入")
# 猜拳
def random_num(num):
     num1 = random.randint(1,9)
     if num1 > num:
         print("你猜的小了")
     elif num1 < num:
         print("你猜的大了")
     else:
         print("恭喜你猜对了")
     return num1
# 调用函数
while True:
    num =input("请输入：")
    num1 = random_num(int(num))
    if num1 == int(num):
        print("======")
        print("游戏结束")
        sys.exit(0)

# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
def len_num(length):
    if len(length) > 5:
        print("长度大于5")
    else:
        print("长度小于5")
len_num(['1','2'])

#写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。如果城市是在长沙并且性别为女，
# 则输出姓名、性别、城市，并返回True,否则返回False。
def city_info(name,city,gender="f"):
     if city == "长沙" and gender == "f":
         print("姓名：{0} 性别：{1} 城市：{2}".format(name,gender,city))
         return True
     else:
         return False
info = city_info('李四',"长沙")
print(info)

#写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def str_len(str):
    if len(str) > 2:
        return str[0:2]
    else:
        return "长度小于2"
str = [1,2,1]
str1 =str_len(str)
print(str1)

#定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，
# 如果字符串不在字典中，则添加到字典中，并返回新的字典。
def r_info(str_x,dic):
     if str_x not in dic.values():
        dic[str_x] =str_x
        return dic

str_x = '222'
dic = {'city':11}
dict = r_info(str_x,dic)
print(dict)

# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def num_n(num):
    count = 0
    for x in range(1,num+1):
        for y in range(1,num+1):
            for z in range(1,num+1):
                if(x!=y) and (x!=z) and (z!=y):
                    count += 1
                    print("%d%d%d"%(x,y,z))
    return count
count = num_n(4)

# 足球队
def footbal(num):
    count = 0
    num1 = 0
    while count < num:
        age = int(input("你的年龄是："))
        sex = input('你的新别是,f是女 m是男：')
        if age >= 10 and age <= 12 and sex == "m":
            print('欢迎加入')
            num1 += 1
        else:
            print("不欢迎")
        count += 1
    return num1
shu = footbal(10)
print(shu)




