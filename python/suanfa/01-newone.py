#如果　a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数)，如何求出所有的ａ，ｂ，ｃ可能的组合
# import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c==1000 and a**2+b**2 ==c**2:
#                 print('a,b,c:%d,%d,%d'%(a,b,c))
# end_time = time.time()
# print('time:%d'%(end_time-start_time))
# print('finished')
import time
start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 -a -b
        if a+b+c==1000 and a**2+b**2 ==c**2:
            print('a,b,c:%d,%d,%d'%(a,b,c))
end_time = time.time()
print('time:%0.8f'%(end_time-start_time))
print('finished')
