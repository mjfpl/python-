__author__ = 'computer'
import random
class person:
    name = ''
    computer = '电脑人'
    quan = 0 #人出拳
    c_quan = 0 #电脑拳
    win = 0  #赢
    lose = 0  #输
    ping = 0  #平局
    # 选人
    def xuanPerson(self):
        while True:
            self.num = int(input('请选择人物1曹操 2 张飞 3刘备：'))
            if self.num == 1:
                self.name= '曹操'
                break
            elif self.num == 2:
                self.name= '张飞'
                break
            elif self.num == 3:
                self.name = '刘备'
                break
            else:
                print('输入有误，请重新输入')
    # 人出拳
    def caiquan(self):
        while True:
         self.quan = int(input("请出拳1 石头 2剪刀 3布:"))
         if self.quan == 1:
             print('%s出的  --石头'%(self.name))
             break
         elif self.quan == 2 :
             print('%s出的  --剪刀'%(self.name))
             break
         elif self.quan == 3 :
             print('%s出的  --布'%(self.name))
             break
         else:
             print('输入有误请重新输入')

    # 电脑人
    def computer_quan(self):
        self.c_quan = random.randint(1,3)
        if self.c_quan == 1:
            print('%s出的  --石头'%(self.computer))
        elif self.c_quan == 2 :
            print('%s出的  --剪刀'%(self.computer))
        else:
            print('%s出的  --布'%(self.computer))
    # 人机猜拳
    def c_p_game(self):
        while True:
            self.xuanPerson() #选人
            self.caiquan() #人出拳
            self.computer_quan() #电脑人出拳
            if (self.quan == 1 and self.c_quan == 1) or (self.quan == 2 and self.c_quan == 2) or (self.quan == 3 and self.c_quan == 3):
                self.ping += 1
                print('平局')
            elif (self.quan == 3 and self.c_quan == 1) or (self.quan == 2 and self.c_quan == 1) or (self.quan == 3 and self.c_quan == 2):
                self.win += 1
                print("获胜")
            else:
                self.lose += 1
                print('输了')
            # 加个停止的条件
            a = input('是否继续n/y:')
            if a.lower() == 'y':
                print('继续')
                continue
            else:
                break
        print('%s赢了%d局'%(self.name,self.win))
        print('%s输了%d局'%(self.name,self.lose))
        print('平%d局'%(self.ping))

p =person()
p.c_p_game()