from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('jonesy@example.com','2012-10-19')
print(sub,"\n",sub.addr,"\n",sub.joined)
print(len(sub))
addr,joined = sub
print(addr,joined)

# def compute_cost1(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] * rec[2]
#     return total
Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total +=s.shares * s.price
    return total
s = Stock('ACME',100,123.45)
print('s:',s)
s = s._replace(shares=70)
print(s)
print('--------------华丽的分割线----------------')
Stock = namedtuple('Stock',['name','shares','price','date','time'])

#create a prototype instance 初始化
stock_prototype = Stock('',0,0.0,None,None)

#Function to convert a dirtionary to Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name':'ACME','shares':100,'price':123.45}
print(dict_to_stock(a))
b = {'name':'ACME','shares':100,'price':123.45,'date':'12/17/2012'}
print(dict_to_stock(b))
