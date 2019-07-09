class Test(object):

	#完成创建一个对象
    #当a = Test()执行的时候,是先调用__new__的方法完成创建对象.
    #然后会紧接着调用__init__方法,完成初始化功能.
    def __new__(cls):
     	print('-------new-----------')
     	print(cls)
     	return super().__new__(cls)
   
    #初始化的功能
    #往往是完成对象属性的设置
    def __init__(self):
        self.num = 100
        print('----init----')
     
    def __str__(self):
        return  str(self.num)



a = Test()
print(a.num)
print(a)

