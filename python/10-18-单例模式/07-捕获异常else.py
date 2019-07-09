try:
    #如果产生了一个异常,但是except没有捕获,那么就会按照这个异常默认的处理方式进行
    open('aaa.txt')
    a = 1
    print(a)

except NameError:
    #如果在try中的代码产生一个NameError时,才会执行的异常处理
    print('捕获到了一个异常')
#在try中的代码都没有产生异常的时候,才会执行的代码
else:
    print('------1-------')
