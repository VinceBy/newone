def creatNum():
    print("--------start--------")
    a,b=0,1
    for i in range(5):
        print('----1------')
        yield b
        print("----2----")
        a,b = b,a+b
        print("----3----")
    print("-------stop----------")

#创建一个生成器对象
a = creatNum()

for num in a:
    print(num)
ret = next(a) #让这个生成器对象开始执行,如果是第一次执行那么就从creatNum的开始部分执行
#如果是之前已经执行过的,那么就从上一次停止的位置开始执行

ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
