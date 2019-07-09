from collections import ChainMap

a = {'x':1,'z':3}
b = {'y':1,'z':4}

c = ChainMap(a,b)
print(c['x'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.items()))#如果有重复会在用第一个映射中对应的值
c['z'] = 12#修改映射的操作总是会作用在列出的第一个映射结构上
c['w'] = 40
print(a)
print('--------------------华丽的分割线--------------------------')
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents
print(values['x'])
values = values.parents
print(values['x'])
print('----------------------------------------------')
#ChainMap 把字典合并以后再操作字典　值会发生改变
merged = ChainMap(a,b)
print(merged["x"])
a['x'] = 43
print(merged['x'])