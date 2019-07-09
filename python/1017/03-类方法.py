class Test(object):
    #类属性
    num = 0
    #实例属性
    def __init__(self):
        #实例属性
        self.age = 1
    
    def test(self):
        print(self.age)

    #类方法
    #可以由类名直接调用类属性或更改类属性
    #也可以由类的对象调用
    @classmethod
    def setNum(cls,newNum):
        cls.num = newNum
    
    #静态方法
    #可以由类直接调用不需要参数也可以由对象调用
    @staticmethod
    def printTest():
        print('当前这个程序,是验证Test类的')


Test.printTest()

a = Test()
print(Test.num)


#a.setNum(200)
Test.setNum(300)
print(Test.num)

a.printTest()

#不允许使用类名访问实例属性
#print("Test.age")
#Test.printTest
