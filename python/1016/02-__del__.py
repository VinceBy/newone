class Person():

	def __init__(self,name,age):
		#只要属性名前面有两个下划线,那么就表示私有的属性
		#所谓私有,不能在外部使用 对象名.属性名获取
		#
		#原来没有__的属性,默认是 公有
		self.__name = name
		self.__age = age

	def __del__(self):
		print('----------del---------')

	
	

laowang = Person('laowang',30)
laozhang = laowang
print(laozhang)
print(laowang)
print('------1------')

del laowang 
#因为老王这个对象已经被删除
#print(laowang)
print('-----0----')
del laozhang 
print('------2----')


	
