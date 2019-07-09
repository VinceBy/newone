import re
num = re.compile('\d+')
print(num.match('123'))
a = num.match('\u0661\u0662\u0663')
print(a)
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'star大'
print(pat.match(s))

print(s.upper())