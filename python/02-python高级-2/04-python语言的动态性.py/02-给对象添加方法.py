import types
class P(object):
    def __init__(self, newName,newAge):
        self.name = newName
        self.age = newAge

    def eat(self):
        print("------%s正在吃-----"%self.name)

def run(self):
    print("------%s正在跑-----"%self.name)

p = P('p',10)
p.eat()
p.run = types.MethodType(run, p)
p.run()

