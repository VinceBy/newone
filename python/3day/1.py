#99乘法表
#记录乘法表的长度
i=9
j=1
n=1
while j<=i:
    m=1
    while m<=j:
        n=j*m
        print('%d*%d=%-2d'%(m,j,n),end=" ")
        m=m+1    
    print('\n')
    j=j+1
