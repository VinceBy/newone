#生成1-n个随机数
import random

def test(n):
    newList = []
    while len(newList)<n:
        num = random.randint(1,n)
        if num not in newList:
            newList.append(num)

    return newList
result = test(10)
print(result)
