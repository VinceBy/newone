class Cat(object):
	def __init__(self):
		self.__name = 'abc'
	def run(self):
		print('------pao----')
	def __test(self):
		print('asdsgsdf')
class Bosi(Cat):
	def test(self):
		#父类的私有方法以及属性无法被子类调用
		#self.__test()
		#print(self.__name)
		pass

class Jiafeimao(Cat):
	pass



bosi = Bosi()

bosi.run()

bosi.test()
		
	
