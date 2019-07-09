#coding=UTF-8
import pygame
from pygame.locals import *

#接下来要做的任务:
#1.实现飞机在你想要的位置显示
#2.实现控制飞机的显示
#3.实现按下空格键 显示一颗子弹

class HeroPlane(object):

	def __init__(self,screen):

		#设置飞机的默认位置
		self.x = 230
		self.y = 600
 		
		#设置显示内容的窗口
		self.screen = screen

		self.imageName = './feiji/hero.gif'
		self.image = pygame.image.load(self.imageName).convert()
		
		#用来存储英雄飞机发射的所有子弹
		self.bulletList = []

	def heroplaneDisplay(self):	
		self.screen.blit(self.image,(self.x,self.y))

		for bullet in self.bulletList:
			bullet.bulletDisplay()
			bullet.move()

		#修改所有子弹的位置
		# for bullet in self.bulletList:
		# 	bullet.y-=2
			

	def moveLeft(self):
		self.x-=10

	def moveRight(self):
		self.x+=10

	def moveUp(self):
		self.y-=10

	def moveDown(self):
		self.y+=10

	def sheBullet(self):
		newBullet = Bullet(self.x,self.y,self.screen)
		self.bulletList.append(newBullet) 

class Bullet(object):
	def __init__(self,x,y,screen):
		self.x = x+40
		self.y = y-15
		self.screen = screen
		self.imageName = './feiji/bullet-3.gif'
		self.image = pygame.image.load(self.imageName).convert()
		

	def bulletDisplay(self):
		
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y-=0.1

	#判断子弹是否越界
	def judgeOut(self):
		
		if self.y<0:
			return 0
		else:
			return 1

class EnemyPlane(object):

	def __init__(self,screen):

		#设置飞机的默认位置
		self.x = 0
		self.y = 0
 		
		#设置显示内容的窗口
		self.screen = screen

		self.imageName = './feiji/enemy-1.gif'
		self.image = pygame.image.load(self.imageName).convert()
		
		#用来存储敌人飞机发射的所有子弹
		self.bulletList = []

	def enemyplaneDisplay(self):	
		self.screen.blit(self.image,(self.x,self.y))

		
		



if __name__ == "__main__":
	
    #1.创建一个窗口,用来显示内容
	screen = pygame.display.set_mode((480,890),0,32)

	#2.创建一个和窗口大小的图片,用来充当背景
	background = pygame.image.load('./feiji/background.png').convert()
	
	#3.创建一个飞机对象
	heroPlane = HeroPlane(screen)

	#4.创建一个敌人飞机
	enemyPlane = EnemyPlane(screen)

	

	#5.把背景图片放到窗口中显示
	while True:
		screen.blit(background,(0,0))
		
		heroPlane.heroplaneDisplay()
		enemyPlane.enemyplaneDisplay()
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
					heroPlane.sheBullet()
					

		pygame.display.update()
