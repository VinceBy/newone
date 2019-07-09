#打印一条横线
#1.
def print_Line(n):
    i=0
    while i<=n:
        print_Line_2()
        i+=1
def print_Line_2():
    print('-'*30)
num = int(input('请输入要打印线的数量'))
print_Line(num)

    
