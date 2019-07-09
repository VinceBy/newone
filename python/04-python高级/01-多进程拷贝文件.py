import os
from multiprocessing import Pool,Manager 

def copyFileTask(name,oldFolderName,newFoldername,queue):
    "完成copy一个文件的功能"
    fr = open(oldFolderName+"/"+name)
    fw = open(newFoldername+"/"+name,'w')
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()
    queue.put(name)
def main():

    #0.获取用户要copy的文件夹的名字
    oldFolderName = input("请输入文件夹的名字")
   
    #1,创建一个文件夹
    newFoldername = oldFolderName+"-附件"
   
    #print(newFoldername)
    os.mkdir(newFoldername)
    
    #2,获取old文件夹中的所有的文件名字
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)

    #3,使用多进程的方式copy 源文件夹中所有文件到新的文件夹中
    pool = Pool(5)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFoldername,queue))
    num = 0
    allnum = len(fileNames)
    while True:
        queue.get()
        num +=1 
        copyRate =  num/allnum
        print("\rcopy的进度是%.2f%%"%(copyRate*100), end="")
        if num == allnum:
            print('已完成ＣＯＰＹ')
            break

if __name__ == "__main__":
    main()
