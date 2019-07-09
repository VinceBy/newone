# collections 模块中的ｃｏｕｎｔｅｒ类　　ｍｏｓｔ＿ｃｏｍｍｏｎ（）
from collections import Counter
words = ['look','into','my','eyes','look','into','my','eyes',
         'the','eyes','the','eyes','the','eyes','not','around',
         'the','eyes',"don't",'look','around','the','eyes','look','into','my',
         'eyes',"you're",'under']
word_counts = Counter(words)#可以对数组里面出现的可哈希对象进行计数
print(word_counts)
top_three = word_counts.most_common(3)
print(top_three)
print(word_counts['not'])
word_counts.update(['eyes'])#放在里面的是数组，增加
print(word_counts)
#counter 特性
a = Counter({'look','into','my','eyes','look','into','my','eyes'})
b = Counter({'the','eyes','the','eyes','the','eyes','not','around'})
#combine counts
c = a+b
print('c:',c)
#Subtract counts
d = a-b
print('d:',d)
