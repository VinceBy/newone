from functools import reduce
print('='*30)
print('对map的操作')
#map(f,l1,l2)分别表示 f:函数 l1:操作数1 l2:操作数2

def f1(x,y):
	return (x,y)
l1 = [0,1,2,3,4,5,6]
l2 = ['sun','M','T','W','T','F','S',]
l3 = map(f1,l1,l2)
print(list(l3))
print("="*30)

print("对filter的操作")
#filter(f,l) 分别表示 f:函数 True l:操作数
#过滤
a = filter(lambda x: x%2,[1,2,3,4,5,6,7])
print(list(a))
print('='*30)


print('对reduce的操作')
b = reduce(lambda x,y:x+y,['a','b','c','d'],'f')
print(str(b))
c = reduce(lambda x,y:x+y,[1,2,3,4,5,7],8)
print(int(c))
print("="*30)


print("对sort的操作")
a = [112,43,34,545,4,57,3,23,25,656,78,45]
a.sort()
print('正序'+str(a))
a.sort(reverse = True)
print('倒序'+str(a))
d = sorted([1,23,4,5,6,78,],reverse = 1)
print(d)
print("="*30)
#集合set
#去重
print("利用集合set去重方法")
print('原列表:')
a = [12,3,34,34,65,23,542,35,45,23]
print(a)
print("转换成集合:")
b = set(a)
print(b)
print("把集合转换成列表:")
a =list(b)
print(a)
print("="*30)
print('集合的交并差补')
a = 'abcdef'
b = set(a)
print(b)
A = 'bdf'
B = set(A)
print(B)
print("交集")
print(B&b)#交集
print('并集')
print(B|b)#并集
print('差集')
print(b-B)#差
print("对称差集")
print(b^B)



