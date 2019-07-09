a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
#find keys in common
print(a.keys() & b.keys())

#find (key,value) in common
print(a.items() & b.items())

#find keys not in a that are not in b
print(a.keys() - b.keys())

#假设想创建一个新的字典，其中会去掉某些键
c = {key:a[key] for key in a.keys() - {'z','w'}}
print('c:',c)