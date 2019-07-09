from operator import itemgetter
rows = [
    {'fname':'Brain','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':1000}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_fname1 = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

print('rows_by_fname:',rows_by_fname)
print('rows_by_fname1:',rows_by_fname1)
print('rows_by_uid:',rows_by_uid)
print('rows_by_lfname:',rows_by_lfname)
print('rows_by_fname1-min:',min(rows, key=itemgetter('uid')))