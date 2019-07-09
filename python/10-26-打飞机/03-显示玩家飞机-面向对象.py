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
		self.bullet = []
	def heroplaneDisplay(self):	

		self.screen.blit(self.image,(self.x,self.y))

	def moveLeft(self):
		self.x-=10

	def moveRight(self):
		self.x+=10

	def she(self,bullet):
		bullet.bulletDisplay(self.x,self.y) 

class Bullet(object):
	def __init__(self,screen):
		self.screen = screen
		self.imageName = './feiji/bullet.png'
		self.image = pygame.image.load(self.imageName).convert()
		

	def bulletDisplay(self,x,y):
		print(x,y)
		self.screen.blit(self.image,(x,y))


		



if __name__ == "__main__":
	
    #1.创建一个窗口,用来显示内容
	screen = pygame.display.set_mode((480,890),0,32)

	#2.创建一个和窗口大小的图片,用来充当背景
	background = pygame.image.load('./feiji/background.png').convert()
	
	#3.1.创建一个飞机对象
	heroPlane = HeroPlane(screen)

	#3.2.创建一个子弹对象
	bullet = Bullet(screen)

	#4.把背景图片放到窗口中显示
	while True:
		screen.blit(background,(0,0))
		
		heroPlane.heroplaneDisplay()
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
					

				elif event.key == K_SPACE:
					print('space')
					heroPlane.she(bullet)
					

		pygame.display.update()
