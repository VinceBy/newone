import random
while True:
#1，提示用户并获取一个数字
    player =int(input("请选择数字1：拳头 0：剪刀 2：布\n"))
    if (player > 2)and(player!=886):
        print("请重新输入")
        continue
    if player ==886:
        break
#2,让电脑产生一个数字
    computer = random.randint(0,2)
    print("computer=%d"%computer)
#3, 判断输赢，并产生相应数字
    if (player==0 and computer==2)or(player==1 and computer==0)or(player==2 and computer==1):
         print("赢了，走，，，喝一杯")
        
    elif computer==player:
        print("平局，不要走，决战到天亮")
    else:
        print("输了，洗洗手再来")
