class Dog:
    def __init__(self,newcolor):
        self.color = newcolor
    def bak(self):
        print('----汪汪叫----')
    def printColor(self):
        print('颜色为：%s'%self.color)
def test(AAA):
    AAA.printColor()
wangcai = Dog('白')
wangcai.printColor()

xiaoqiang = Dog('黑')
xiaoqiang.printColor()

test(wangcai)
