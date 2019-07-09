class SweetPotato:
    #用来完成一些初始化的工作
        def __init__(self):
            self.cookedLevel = 0
            self.cookedString = "生的"
            self.condiments = []

        def __str__(self):
            msg = "地瓜的生熟程度为："+self.cookedString
            msg += '\n'+'等级为：'+str(self.cookedLevel)
            if len(self.condiments)>0:
                msg += '\n'+'作料为：'
                for temp in self.condiments:
                    msg += temp + ','
                #第一种方法去掉最后的‘，’
                #msg = msg[:-1]+'\n'
                #第二种方法
                msg = msg.strip(',')
            else:
                msg +='\n'+'当前没有添加任何作料' 
            return msg+'\n'

        def cook(self, times):
            self.cookedLevel += times
            if self.cookedLevel>8:
                self.cookedString = '焦了'
            elif self.cookedLevel>5:
                self.cookedString = '熟了'
            elif self.cookedLevel>3:
            	self.cookedString = '半生不熟'
            else:
                self.cookedString = '生的'
        
        #添加作料
        def addCondiments(self,temp):
            self.condiments.append(temp)
            
digua = SweetPotato()
print(digua)
digua.cook(2)
print(digua)
digua.addCondiments('芥么酱')
print(digua)
digua.addCondiments('番茄酱')
print(digua)
digua.addCondiments('咖喱')
print(digua)
digua.addCondiments('孜然')
print(digua)
digua.cook(3)
print(digua)
digua.cook(2)
print(digua)

