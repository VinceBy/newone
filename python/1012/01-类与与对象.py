class Dog:
    def __init__(self,newcolor):
        self.color = newcolor
    def bak(self):
        print('----汪汪叫----')
    def printColor(self):
        print('颜色为：%s'%self.color)
    # print 输出 treturn 
    def __str__(self):
    	return '当前对象的颜色为：'+self.color
    	
def test(AAA):
    AAA.printColor()
wangcai = Dog('白')
#wangcai.printColor()

xiaoqiang = Dog('黑')
#xiaoqiang.printColor()

#test(wangcai)

print(wangcai)
print(xiaoqiang)
print(id(wangcai))
print(id(xiaoqiang))