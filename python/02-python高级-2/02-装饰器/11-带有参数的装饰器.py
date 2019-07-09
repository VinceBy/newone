def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志---arg=%s---"%arg)
            if arg == "hello":
                functionName()
                functionName()
            else:
                
                functionName()

        return func_in
    return func

#1.先执行func_arg("heiehi")函数,这个函数return的结果是func的引用
#2.@func
#3.使用@func对test进行装饰

@func_arg("hello")
def test():
    print("-----test1----")

#带有参数的装饰器能够起到不同的功能
@func_arg("haha")
def test2():
    print("-----test2----")

test()
test2()
