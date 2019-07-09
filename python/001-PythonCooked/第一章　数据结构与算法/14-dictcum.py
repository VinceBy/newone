prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
#zip创建了一个迭代器，只能使用一次
min_price = min(zip(prices.values(), prices.keys()))
print("min_price:",min_price)
max_price = max(zip(prices.values(), prices.keys()))
print("max_price:",max_price)

print('==========================')
print(min(prices.values()))
print(max(prices.values()))

print("2222222222222222222222222222")
print(max(prices,key=lambda k:prices[k]))
print(min(prices,key=lambda k:prices[k]))

