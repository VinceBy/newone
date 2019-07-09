#定义一个猫类
class Cat:
    #属性
    #当创建完一个对象后，立马会立刻调用
    def __init__(self,newColor,newWeight,NewWeiba):
        self.color = newColor
        self.weight = newWeight
        self.weiba = NewWeiba
        print('hahaha')

    #方法
    def eat(self):
        print('-----吃-----')
    
    def drink(self):
        print('-----喝-----')

    def play(self):
        print('-----玩-----')

    def happy(self,a,b):
        print('-----乐-----')
        print('a=%d,b=%d'%(a,b))

    def printInfo(self):
        print(self.weiba)



#创建一个猫 对象
xiaohuamao = Cat('花色'，5,'有')
xiaohuamao.eat()
xiaohuamao.drink()
xiaohuamao.play()
xiaohuamao.happy(11,12)


#给xiaohuamao对象添加属性
xiaohuamao.color = '花色'
xiaohuamao.weight = 5
xiaohuamao.weiba = '有'

#获取小花猫的的数据
a = xiaohuamao.color
print(a)
print(xiaohuamao.weight)
print(xiaohuamao.weiba)

#注意：如果属性 还要访问 会产生异常
xiaohuamao.printInfo()
