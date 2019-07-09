def test1():
    while True:
        print("---1---")
        yield None

def test2():
    while True:
        print("---2---")
        yield None

#协程
t1 = test1()
t2 = test2()
while True:
     t1.__next__()
     t2.__next__()
