def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1,n):
        # j : [1,2,3....,n-1]
        # i : 代表内存循环的起始值
        i = j
        #执行从右边的无序序列中去除第一个元素，即ｉ位置的元素，然后将其插入到正确的位置中
        while i>0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break

if __name__ == "__main__":
    alist = [31,24,34,523,4,53,4,5,23,532,52,34,6,546,76,5,77,6,75]
    print(alist)
    insert_sort(alist)
    print(alist)

