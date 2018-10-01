__author__ = 'computer'
class student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_course(self):
        n1 = self.score[0]
        n2 = self.score[1]
        n3 = self.score[2]
        max_num = 0
        if n1 > n2:
            max_num = n1
            if n1 > n3:
                max_num = n1
            else:
                max_num = n3
        else:
            max_num = n2
            if n2 > n3:
                max_num = n2
            else:
                max_num = n3
        print('最高成绩是：%d'%(max_num))
s = student('zhangming',20,[69,88,100])
s.get_name()
s.get_age()
s.get_course()