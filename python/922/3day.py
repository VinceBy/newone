#coding=utf-8
#定义一个列表，用来存储所有的名字
names = []
while True:
    #1.打印提示
    print('='*30)
    print("   欢迎使用白羽的系统 version 6.8")
    print("1：添加一个名字")
    print("2：删除一个名字")
    print("3：修改一个名字")
    print("4：查询一个名字")
    print("5：遍历所有的名字")
    print("0：退出系统")
    print("="*30)

    #2.获取要操作的数字
    key = input('请输入数字：')

    #3.根据提示来做相应的事情
    if key == "1":
        insertName =  input("请输入要添加的名字:")
        names.append(insertName)

    elif key == "2":
        deletName = input("请输入要删除的名字:")
        if deletName in names:
            num= names.index(deletName)
            del names[num]
        else:
             print('不存在')

    elif key == "3":
        removeName = input("请输入要修改的名字:")
        if removeName in names:
           num= names.index(removeName)
           newName = input("请输入要修改后的名字:")
           names[num]=newName
        else:
           print('不存在')

    elif key == "4":
        checkName = input("请输入要查询的名字:")
        if checkName in names:
            print("存在")
        else:
            print("不存在")

    elif key == "5":
        print("-"*30)
        for temp in names:
            print(temp)
    elif key == "0":
        break



