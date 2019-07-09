#异步不确定什么时候去做
#同步是指一件事一件事的做

from multiprocessing import Pool
import time
import os

def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"

def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

pool = Pool(3)
pool.apply_async(func=test,callback=test2)#回调ｃａｌｌｂａｃｋ test 传给ｔｅｓｔ２

i = 0
while i<10:
    time.sleep(1)
    print("----主进程-pid=%d----"%os.getpid())
    i+=1
