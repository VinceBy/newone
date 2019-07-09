#列表去重，集合只是确保数据的不重复，但是不能保证元素之间的顺序
a = [1,1,2,3,3,4,5,6]
b=set(a)
c=list(b)
print(c)

# 可哈希
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
print(list(dedupe(a)))

# 不可哈希
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [{'x':1,'y':2},{'x':1,'y':5},{'x':1,'y':2},{'x':2,'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))

