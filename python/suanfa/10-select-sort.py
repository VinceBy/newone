def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1):# j: 0 ~ n-2
        for i in range(j+1,n):
            if alist[j] > alist[i]:
                alist[i], alist[j] = alist[j], alist[i]

if __name__ == "__main__":
    li = [324,23,4,3452,3453,45,6,45,325,23,54,523,534,6856,62,4,53,5,2]
    # print(li)
    select_sort(li)
    print(li)

