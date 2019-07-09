import time
def test1():
    num = 100
    print(num)

def test2():
    num = 200
    print(num)

    time.sleep(2)

    num = num+100

    print(num)
#在函数里面的变量就叫做局部变量
#
test1()
test2()
