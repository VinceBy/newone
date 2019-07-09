def func(functionName):
    print("----func-----1-----")
    def func_in():
        print("----func--in---1-----")
        ret =  functionName()#保存返回来的haha
        print("----func--in---1-----")
        return ret#把haha返回到17行处的调用

    print("----func-----2-----")
    return func_in

@func
def test():
    print("-----test------")
    return 'haha'

ret = test()
print("test return value is:%s"%ret)
