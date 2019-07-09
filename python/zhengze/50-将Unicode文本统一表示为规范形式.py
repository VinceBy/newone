import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1==s2)
print(len(s1),len(s2))
t1 = unicodedata.normalize("NFC",s1)
t2 = unicodedata.normalize("NFC",s2)
print(t1==t2)
print(ascii(t1))
t3 = unicodedata.normalize("NFD",s1)
t4 = unicodedata.normalize("NFD",s2)
print(t3==t4)
print(ascii(t3))
s = '\ufb01'
print(s)
an4 = unicodedata.normalize('NFKD',s)
print(s)
# 文本中去除所有音符标记
t1 = unicodedata.normalize('NFD',s1)
a = ''.join(c for c in t1 if not unicodedata.combining(c))
print(a)
