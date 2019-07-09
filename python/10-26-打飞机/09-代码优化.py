#coding=UTF-8
import pygame
from pygame.locals import *
import time
import random

#接下来要做的任务:
#1.实现飞机在你想要的位置显示
#2.实现控制飞机的显示
#3.实现按下空格键 显示一颗子弹
class Base(object):
	"""docstring for """
	def __init__(self,screen,name):
		self.name = name		
		#设置显示内容的窗口
		self.screen = screen
		

class Plane(Base):
	
	def __init__(self,screen,name):
		super().__init__(screen,name)		
		self.image = pygame.image.load(self.imageName).convert()		
		#用来存储英雄飞机发射的所有子弹
		self.bulletList = []

	def display(self):	
		#更新飞机的位置,
		self.screen.blit(self.image,(self.x,self.y))
		#判断一下子弹的位置时候越界,如果是,那么就要删除这颗子弹
		#
		#这种方法会漏掉很多要删除的数据666
		# for i in self.bulletList:
		# 	if i.y<0:
		# 		self.bulletList.remove(i)
		#存放需要删除的信息
		needDelItemList = []
		for i in self.bulletList:
			if i.judgeOut():
				needDelItemList.append(i)
		for i in needDelItemList:
			self.bulletList.remove(i)
		#更新这架飞机发射出的所有子弹的位置
		for bullet in self.bulletList:
			bullet.bulletDisplay()
			bullet.move()
		#修改所有子弹的位置
		# for bullet in self.bulletList:
		# 	bullet.y-=2
	def sheBullet(self):
		newBullet = PublicBullet(self.x,self.y,self.screen,self.name)
		self.bulletList.append(newBullet) 



class HeroPlane(Plane):
	def __init__(self,screen,name):
		#设置飞机的默认位置
		self.x = 230
		self.y = 600

		self.imageName = './feiji/hero.gif'	
		super().__init__(screen,name)
			
	def moveLeft(self):
		self.x-=10

	def moveRight(self):
		self.x+=10

	def moveUp(self):
		self.y-=10

	def moveDown(self):
		self.y+=10


class EnemyPlane(Plane):

	#重写父类的__init__方法
	def __init__(self,screen,name):
		#设置飞机的默认位置
		self.x = 0
		self.y = 0
		self.imageName = './feiji/enemy-1.gif'
		#调用父类的__init__方法
		super().__init__(screen,name)
		self.direction = 'right'	

	def move(self):
		#如果碰到了右边的边界,那么就往左走,相反,同理.
		if self.direction == 'right':
			self.x +=0.5
		elif self.direction =='left':
			self.x -=0.5
		if self.x>480-50:
			self.direction = 'left'
		elif self.x<0:
			self.direction = 'right'

	def sheBullet(self):
		num = random.randint(1,100)
		if num == 88:
			super().sheBullet()


class PublicBullet(Base):
	def __init__(self,x,y,screen,planeName):
		super().__init__(screen,planeName)
		
		if self.name == 'hero':
			self.x = x+40
			self.y = y-15			
			imageName = './feiji/bullet-3.gif'			
		elif self.name == 'enemy':
			self.x = x+20
			self.y = y+30			
			imageName = './feiji/bullet-1.gif'
		self.image = pygame.image.load(imageName).convert()
		

	def bulletDisplay(self):		
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		if self.name == 'hero':
			self.y-=1
		elif self.name == 'enemy':
			self.y+=1
			
	def judgeOut(self):
		#判断子弹是否越界
		if self.y>890 or self.y<0:
			return 1
		else:
			return 0

if __name__ == "__main__":
	
	#1.创建一个窗口,用来显示内容
	screen = pygame.display.set_mode((480,800),0,32)

	#2.创建一个和窗口大小的图片,用来充当背景
	background = pygame.image.load('./feiji/background.png').convert()
	
	#3.创建一个飞机对象
	heroPlane = HeroPlane(screen,'hero')

	#4.创建一个敌人飞机
	enemyPlane = EnemyPlane(screen,'enemy')	

	#5.把背景图片放到窗口中显示
	while True:

		screen.blit(background,(0,0))		
		heroPlane.display()
		enemyPlane.move()
		enemyPlane.sheBullet()
		enemyPlane.display()
		

		#判断是否点击了退出按钮   
		for event in pygame.event.get():
			if event.type == QUIT:
				print('exit')
				exit()

			elif event.type == KEYDOWN:
				if event.key ==K_a or event.key == K_LEFT:										
					print('left')
					#控制飞机向左移动
					heroPlane.moveLeft()


				elif event.key ==K_d or event.key == K_RIGHT:
					print('right')
					#控制飞机向右移动
					heroPlane.moveRight()
				
				elif event.key ==K_w or event.key == K_UP:
					print('up')
					#控制飞机向上移动
					heroPlane.moveUp()

				elif event.key ==K_s or event.key == K_DOWN:
					print('down')
					#控制飞机向右移动
					heroPlane.moveDown()

				elif event.key == K_SPACE:
					print('space')
					#控制飞机发射子弹
					heroPlane.sheBullet()

		
		time.sleep(0.01)
		pygame.display.update()
