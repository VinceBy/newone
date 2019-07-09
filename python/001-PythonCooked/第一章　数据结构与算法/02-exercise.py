from collections import *

# deque(maxlen=3)可以创建一个固定长度的队列，先进先出，当有多余的数进入时，会冲刷掉最先进入的
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

#deque()也可以创建一个任意长度的队列，无界限
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
q.appendleft('qqq')
print(q)
print(q.pop())
print(q)
print(q.popleft())
