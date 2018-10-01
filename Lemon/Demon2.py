__author__ = 'computer'
# 九九乘法表
for m in range(1,10):
    for n in range(1,m+1):
        print("%s * %s = %s "%(m,n,m*n),end='')  # end = '' 用来中段print()
    print()