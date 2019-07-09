import os
nums = [1,2,3,4,5,6]
s = sum(x*x for x in nums)
print(s)

s = ('ACME', 50, 123.45)
print(','.join(str(x)for x in s))
portfolio = [
     {'name':'GOOG','shares':50},
     {'name':'YHOO','shares':75},
     {'name':'AOL','shares':20},
     {'name':'Scox','shares':65}
 ]
# min_shares = min(s['shares'] for s in portfolio)
min_shares = min(portfolio, key = lambda s: s['shares'])
print(min_shares['shares'])
