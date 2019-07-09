from collections import OrderedDict
import json
#OrderedDict()　当对字典做迭代时，它会严格按照元素的初始化添加顺序进行
#OrderDict　是双向链表　是一般字典的两倍多，会造成额外的内存开销
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 6
d['grok'] = 4
for key in d:
    print(key,d[key])
#当想构建一个映射结构以便稍后对其做序列化或编码成另一种格式时，就需要使用到OrderedDict()
print(json.dumps(d))
