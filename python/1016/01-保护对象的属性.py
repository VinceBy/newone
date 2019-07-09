class Person():

	def __init__(self,name,age):
		#只要属性名前面有两个下划线,那么就表示私有的属性
		#所谓私有,不能在外部使用 对象名.属性名获取
		#
		#原来没有__的属性,默认是 公有
		self.__name = name
		self.__age = age

	def setNewAge(self,newAge):
		if newAge>0 and newAge<=100:
			self.__age = newAge
	def getAge(self):
		return self.__age

	def __test(self):
		print('-------------sdff------------')

	

laowang = Person('laowang',30)
laowang.setNewAge(31)
age = laowang.getAge()
print(age)
#私有方法无法访问
#laowang.__test()	
	
