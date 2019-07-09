class Home:
    def __init__(self,area):
        self.area = area
        self.light = 'on'
        self.containsItem = []

    def __str__(self):
        msg = '家当前可用面积'+str(self.area)
        
        if len(self.containsItem)>0:
            msg += '\t'
            msg += '家里的物品有：'
            #msg +=','.join(self.contains)

            for temp in self.containsItem:            
                #msg += temp.name+','
                msg += temp.getName() + ','

            msg = msg[:-1]
            if self.light == 'on':
                msg += '\t' + '当前灯是开着的，所有的物品都是可见的'
            else:
                msg += '\t' + '当前灯是关着的，所有的物品都是看不见的'
            
        return msg

        #添加一个新物品到家里面
    def addItem(self,item):
        needArea = item.getArea()
        #if self.area >item.area
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea

    def turnoff(self):
        self.light = 'off'
        #修改所有的物品可见度
        for temp in self.containsItem:
            temp.turnoff()
class Bed:
    def __init__(self,name,area):
        self.name = name
        self.area = area
        self.light = 'on'

    def __str__(self):
        msg = self.name + '床的面积' + str(self.area) +'当前的可见度为：'+self.light
        return msg

    def  getName(self):
        return self.name

    def getArea(self):
        return self.area

    def turnoff(self):
        self.light = 'off'


#创建一个家对象
home = Home(128)
print(home)

#创建一个床对象
bed = Bed('席梦思',4)
print(bed)
home.addItem(bed)
print(home)

bed2 = Bed('硬板床',3)
print(bed2)
home.addItem(bed2)
print(home)

print('========================分割=======================')
home.turnoff()
print(bed)
print(bed2)