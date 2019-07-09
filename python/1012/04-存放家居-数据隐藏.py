#在一个类当中，获取另一个类里面的值时，
#最好时在另一个类当中能够用一个方法来返回值。
#不要直接去获取这个值，因为这样的封装性不好。
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
                #msg += temp.name+','
                msg += temp.getName() + ','

            msg = msg[:-1]
        
            
        return msg

        #添加一个新物品到家里面
    def addItem(self,item):
        needArea = item.getArea()
        #if self.area >item.area
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea

class Bed:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        msg = self.name + '床的面积' + str(self.area)
        return msg

    def  getName(self):
        return self.name

    def getArea(self):
        return self.area
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

