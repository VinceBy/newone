try:
   # print(abd)

   open('sdfsd.txt')
except (NameError,FileNotFoundError) as result:
    print("产生一个异常......%s"%result)

