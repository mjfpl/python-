__author__ = 'computer'
import sys
login_info={"username":"admin","passwd":"123456"}
flag0=0
flag1=1
while True:
#提示用户输入用户名
    usr=input("enter username:")
    if usr==login_info["username"]:
    #输入用户名正确则进入到输入登录密码阶段
        #判断输错登录密码次数
        while flag0<3:
            password=input("enter password:")
            if password==login_info["passwd"]:
            #若密码输入不正确则登录成功因而跳出循环
                print("Success Login!")
                flag1=1
                sys.exit(0)
            else:
            #计算输错次数，每输错一次flag加1
                flag0 +=1
                if flag0 <3:
                    print("Wrong Password,enter again!")
            #输错三次跳出输入扥路密码环节重新进行用户名的输入，相应的flag也要归零
            if flag0==3:
                break
            # flag0=0
                print("You have tried three times,login aggin!")
    else:
        flag0 +=1
        if flag0 <3:
            print("Wrong userName,enter again!")
    if flag0 ==3:
        break
        print("You have tried three times,login again")