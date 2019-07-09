class Ma:
    def pao(self):
        print('=======100km/h====跑=====')

    def jiao(self):
        print('=======马再叫--========')

class Lv:
    def tuowupin(self):
        print('======托物品====')
    def jiao(self):
        print('=======驴在叫===========')

class Luozi(Ma,Lv):
    pass

luozi = Luozi()
luozi.pao()
luozi.tuowupin()
luozi.jiao()
print(Luozi.__mro__)

