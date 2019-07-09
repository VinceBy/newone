def func(functionName):
    print("----func-----1-----")
    def func_in():
        print("----func--in---1-----")
        functionName()
        print("----func--in---1-----")

    print("----func-----2-----")
    return func_in

@func
def test():
    print("-----test------")


#test = func(test)

test()
