try:

   # print(abc)
    open('abc.txt')
except (NameError,FileNotFoundError):
    print('没有定义变量.....')
