__author__ = 'computer'
class User:
    def __init__(self,first_name,last_name,age,hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
    def describe_user(self):
        print('你好我姓%s,叫%s,今年%d岁，爱好是：%s'%(self.first_name,self.last_name,self.age,self.hobby))

    def greet_uesr(self,name):
         print('很个性的问候：哈喽你好啊%s'%(name))

u = User('上官','老虎',20,'足球')
u.describe_user()
u.greet_uesr('王五')
