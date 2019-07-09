def test(num):
    if num>1:
        return num*test(num-1)
    else:
        return 1
    

num = int(input("输入要阶乘的数"))
result=test(num)
print(result)

