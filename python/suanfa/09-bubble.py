def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0,n-1-j):
            #班长从头走到尾
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count+=1
        if count == 0:
            return
# i 0 ~ n-1 range(0, n-1) j=0
# i 0 ~ n-2 range(0, n-1-1) j=1
# i 0 ~ n-3 range(0, n-1-2) j=2
if __name__ == "__main__":
    li = [324,23,4,3452,3453,45,6,45,325,23,54,523,534,6856,62,4,53,5,2]
    print(li)
    bubble_sort(li)
    print(li)
