__author__ = 'computer'
class TestWork:
    name = '李四'
    age = 20
    def jineng(self,language):
        print(self.name+'会做%s自动化测试'%(language))
    def TestSys(self):
        print('会做系统测试')
    def work(self):
        print('今年%d岁'%(self.age))
tt = TestWork()
tt.jineng('java')
tt.TestSys()
tt.work()