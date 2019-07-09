'''
def test(a):
    return a+1
aaaa=lambda a:a+1
bbbb=lambda a,b:a+b

print(aaaa(8))
print(bbbb(11,22))
'''
def test(a,b,xxx):
    return xxx(a,b)
result = test(11,22,lambda x,y:x-y)
print(result)
