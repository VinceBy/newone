def test():
    print('-----1-1----')
    print(num)
    print('-----1-2----')

def test2():
    print('-----2-1----')
    test()
    print('-----2-1----')

def test3():
    try:
        print('-----3-1----')
        test()
        print('-----3-2----')
    except Exception as result:
        print('捕获到了异常%s'%result)

test3()
