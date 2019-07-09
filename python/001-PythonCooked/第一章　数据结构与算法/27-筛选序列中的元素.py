import math
from itertools import compress
mylist = [1,4,-5,-10,-7,2,3,-1]#列表推倒式
a = [n for n in mylist if n>0]
b = [n for n in mylist if n<0]
print('a：',a)
print('b:',b)
pos = (n for n in mylist if n>0)
for x in pos:
    print(x)
values = ['1','2','-3','-','4','N/A','5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

s = [math.sqrt(n) for n in mylist if n>0]
print(s)

clip_neg = [n if n>0 else 0 for n in mylist ]
print('clip_neg:',clip_neg)
clip_pos = [n if n<0 else 0 for n in mylist]
print('clip_pos',clip_pos)

address = [
    '5412 N CLARK',
    '4801 N BROADWAY',
    '5800 E 58TK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '2122 N CLARK',
    '5148 N CLARK',
    '1039 W GRANVILLE'
]

counts = [0,3,10,4,1,7,6,1]

more5 = [n > 5 for n in counts]
print(more5)
a = list(compress(address,more5))
print(a)

