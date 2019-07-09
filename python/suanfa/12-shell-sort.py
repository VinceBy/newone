def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n//2
    #gap　变化到０之前插入算法执行的次数
    while gap>=1:
    #希尔算法，与普通的插入算法的区别就是ｇａｐ步长
        for j in range(gap,n):
            i = j
            while i>0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        #缩短ｇａｐ步长
        gap //=2
if __name__ == "__main__":
    alist = [789,1,5234,532,523,53,5,3,54,352,35,23,34]
    print(alist)
    shell_sort(alist)
    print(alist)