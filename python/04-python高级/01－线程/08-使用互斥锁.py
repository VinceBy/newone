from threading import Thread,Lock
import time

g_num = 0

def test1():
    global g_num    
    #这个线程和ｔｅｓｔ２线程都在抢着
    mutex.acquire()
    for i in range(1000000):
        g_num +=1
    print("-----test1-----g_num=%d"%g_num)

    #解锁
    mutex.release()

def test2():
    global g_num
    mutex.acquire()
    for i in range(1000000):
        g_num += 1
    print("----test2----g_num=%d"%g_num)
    mutex.release()

#创建一把锁　默认是开的
mutex = Lock()

p1 = Thread(target=test1)
p1.start()

#time.sleep(3) #取消屏蔽之后　再次运行注释，结果会不一样．
p2 = Thread(target=test2)
p2.start()

print("---:wq-g_num=%d----"%g_num)
