import os
import time

ret = os.fork()
if ret==0:
    while True:
        print("ret=%d"%ret)
        print("----1----")
        time.sleep(1)
else:
    while True:
        print("ret=%d"%ret)
        print("---2---")
        time.sleep(1)
