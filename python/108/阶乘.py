#1*2*3.....*100
def subl():
    num = int(input('请输入你要阶乘的数字:'))
    i = 1
    result = 1
    while i<=num:
        result*=i
        i+=1
    print("%d!=%d"%(num,result))
subl()

