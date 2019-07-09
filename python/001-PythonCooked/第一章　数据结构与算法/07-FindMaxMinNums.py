import heapq
#heapq.nlargest(N,Collections)－－－找出集合中的最大的Ｎ个元素
#heapq.nsmallest(N,Collection)－－－找出集合中的最小的Ｎ个元素
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

#这两个函数都可以接受一个参数Ｋｅｙ
portfolio = [
    {'name':"IBM",'share':100,'price':91.1},
    {'name':"ASF",'share':50,'price':532.34},
    {'name':"DF",'share':34,'price':75.56},
    {'name':"FGD",'share':56,'price':34.89},
    {'name':"SDR",'share':89,'price':67.23},
    {'name':"HHN",'share':40,'price':98.3}
]
cheap = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
expensive = heapq.nlargest(3,portfolio,key=lambda s:s['share'])
print('cheap:'+str(cheap)+'\n'+'expensive:'+str(expensive))
print(cheap[1]['name'])

#当我们只是想寻找最小的那个数的时候
#我们可以采用下面的方法，先从转换成列表，然后在利用heapq.heapify()方法形成堆，堆最重要的特性就是heap[0]为最小的那个数
#我们也可以直接对列表进行排序
nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(type(nums))
heap = list(nums)
heapq.heapify(heap)
print(heap)
print("heap:"+str(heap[0]))
#直接排序
nums.sort()
print('nums:'+str(nums[0]))