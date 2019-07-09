import matplotlib.pyplot as plt#约定俗成的写法plt
#首先定义两个函数（正弦&余弦）
import numpy as np
fig,ax = plt.subplots()
plt.xlabel('distance')
plt.ylabel("Magnetic intensity")
X=[29,25,21,18,14,11,9,8,7,6,5,4]
C=[0x56,0x55,0x53,0x4f,0x46,0x34,0x06,0x03,0xce,0x86,0x80,0x1d]
plt.plot(X,C)

#在ipython的交互环境中需要这句话才能显示出来
plt.show()