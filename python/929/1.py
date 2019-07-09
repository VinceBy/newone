import random
#1。定义一个列表，嵌套的列表
rooms = [[],[],[]]
#2。有一个列表，保存了8名老师的名字
teacher = ['A','B','C','D','E','F','G','H']
#3。随机把8名老师的名字加到第一个列表中
for name in teacher:
    num = random.randint(0,2)
    rooms[num].append(name)
i=1
#print(rooms)
for room in rooms:
    num = len(room)
   # print(num)
    print("第%d个办公室的老师：%d个"%(i,num))
    for name in room:
        print(name,end='')
    i=i+1
    print('')

