__author__ = 'computer'
class enginner:
    skill = 'java'
    age = 20
    name = '李四'
    # 会啥技能
    def object_enginner(self,en_gae):
        print("今年%s岁"%(en_gae))
        #print(self.skill)
    # 努力工作
    def nuli_work(self,en_skill):
        print('%s很厉害'%(en_skill))
    # java很厉害
    def good_work(self,en_name):
        print('名字是%s'%(en_name))
    def work(self,*args):
        for item in args:
            print(item)
en = enginner()
en.object_enginner(30)
en.good_work('java')
en.nuli_work('李四')
en.work('奶茶','阔落')