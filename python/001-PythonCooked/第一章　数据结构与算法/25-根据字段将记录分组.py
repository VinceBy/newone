from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows = [
    {'address':'5412 N CLARK', 'date': '07/01/2012'},
    {'address':'5148 N CLARK', 'date': '07/04/2012'},
    {'address':'5800 E 58TK', 'date': '07/02/2012'},
    {'address':'2122 N CLARK', 'date': '07/03/2012'},
    {'address':'5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address':'1060 W ADDISON', 'date': '07/02/2012'},
    {'address':'4801 N BROADWAY', 'date': '07/01/2012'},
    {'address':'1039 W GRANVILLE', 'date': '07/04/2012'}
]

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
for address in rows:
    print('\''+str(address['address'])+'\''+',')
#Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('',i)
print('--------------------------华丽的分割线----------------------------')
#在这个例子中　我们不需要考虑字典中同一类数据的顺序问题
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
for r in rows_by_date['07/01/2012']:
    print(r)
