from multiprocessing import Pool
import os
import random
import time

def work(num):
    for i in range(5):
        print("----pid=%d--num=%d--"%(os.getpid(),num))
        time.sleep(1)

#3表示 线程池中最多有三个进程一起执行
pool = Pool(3)

for i in range(10):
    print("-----i=%d----"%i)
    #向进程池中添加任务
    #注意:如果添加的任务超过了 进程池中的进程的个数的话,那么不会导致添加不进去
    #   添加到进程中的任务 如果还没有被执行的的话 那么此时 他们会等待进程池中的
    #   添加完成一个任务之后,会自动的去用刚刚的那个进程 完成当前的新任务
    pool.apply_async(work,(i,))

#关闭进程池相当于不能添加新任务了
pool.close()
#主进程 创建/添加 任务后默认不会的等待进程池中的任务执行完后才结束
#而是  当进程的的任务做完之后 立马结束 ,,,,如果这个地方没join,会导致进程池中的任务不会执行
pool.join()
