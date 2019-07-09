from multiprocessing import Pool
import os
import random
import time

def work(num):
    for i in range(5):
        print("----pid=%d--num=%d--"%(os.getpid(),num))
        time.sleep(1)

pool = Pool(3)

for i in range(10):
    print("-----i=%d----"%i)
    pool.apply(work,(i,))

pool.close()
pool.join()
