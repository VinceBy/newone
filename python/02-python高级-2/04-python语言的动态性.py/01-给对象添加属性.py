class Person(object):
    def __init__(self,newName,newAge):
        self.newName = newName
        self.newAge = newAge

    def eat(self):
        print("------%s正在吃----"%self.newName)

def run(self):
    print("-------%s正在跑----"%selfnewName)

p1 = Person("p1",10)
p1.eat()
p1.run = run
p1.run()#虽然P1对象中 run属性已经指向了10行的函数...但是这句代码还不正确
        #因为run属性指向的函数是后来添加的,掉p1.run的时候并没有把p1当做第一个参数,导致第10行的函数调用的时候,出现缺少参数的问题
