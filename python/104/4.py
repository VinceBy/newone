def three_Sum(a,b,c):
    return a+b+c
def three_Average(a,b,c):
    return (a+b+c)/3
num1 = int(input('请输入第一个数'))
num2 = int(input('请输入第二个数'))
num3 = int(input('请输入第三个数'))
summ = three_Sum(num1,num2,num3)
#summ1 = sum(num1,num2,num3)
average = three_Average(num1,num2,num3)
print('这三个数的和：%d'%summ)
print('这三个数的平均数：%d'%average)


