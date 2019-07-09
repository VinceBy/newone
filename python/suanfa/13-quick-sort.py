def quick_sort(alist,first,last):
    if first>=last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        #high的游标左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        #low 右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    #从循环退出时ｌｏｗ＝　ｈｉｇｈ
    alist[low] = mid_value

    #对ｌｏｗ　左边的列表执行快速排序
    quick_sort(alist,first,low-1)

    #对ｌｏｗ　右边的列表排序
    quick_sort(alist,low+1,last)




if __name__ == "__main__":
    alist = [12,343,235,23,54,54,523,523,532,5]
    print(alist)
    n = len(alist)-1
    quick_sort(alist, 0, n)
    print(alist)

