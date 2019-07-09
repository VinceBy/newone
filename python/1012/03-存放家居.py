class Home:
    def __init__(self,area):
        self.area = area
        self.containsItem = []

    def __str__(self):
        msg = '家当前可用面积'+str(self.area)
        
        if len(self.containsItem)>0:
            msg += '\t'
            msg += '家里的物品有：'
            #msg +=','.join(self.contains)

            for temp in self.containsItem:            
                msg += temp.name+','

            msg = msg[:-1]
        
            
        return msg

        #添加一个新物品到家里面
    def addItem(self,item):
        if self.area>item.area:
            self.containsItem.append(item)
            self.area -= item.area

class Bed:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = self.name + '床的面积' + str(self.area)
        return msg
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

