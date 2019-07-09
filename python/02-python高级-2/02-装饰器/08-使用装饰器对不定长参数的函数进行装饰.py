def func(functionName):
    print("----func-----1-----")
    def func_in(*argc, **kwargs):#如果a,b没有定义,那么会导致16行的调用失败
        print("----func--in---1-----")
        functionName(*argc,**kwargs)#如果没有把a,b当做实参进行传递,那么会导致调用12行的函数失败
        print("----func--in---1-----")
    print("----func-----2-----")
    return func_in

@func
def test(a,b,c):
    print("-----test----a=%d-b=%d--c=%d"%(a,b,c))

@func
def test2(a,b,c,d):
    print("-----test----a=%d-b=%d--c=%d-d=%d"%(a,b,c,d))

test(11,22,33)
test2(44,55,66,77)
