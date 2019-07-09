import re
s = ' 　　　　hello world 　　\n'
print(s)
# 可以用来从字符串的开始和结尾处去掉字符
a = s.strip()
print(a)
# 从左边开始执行去掉字符的操作
print(s.lstrip())
# 从右边开始执行去掉字符的操作
print(s.rstrip())

t = '-------hello======='
print(t.lstrip("-"))
print(t.rstrip("="))
print(t.strip("-="))

s = ' hello   world   \n'
s = s.strip()
print(s)
s1 = s.replace(' ', '')
print(s1)

a = re.sub('\s+', ' ', s)
print(a)

