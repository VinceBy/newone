#coding=utf-8
num = int(input("请输入人员的数目:"))
name = {}
i=1
while i<=num:
    name[i] = input('第%d的人名:'%i)
    i+=1
print(name)
insertName = input('需要比对的名字:')
findflag = 0
i=1
while i<=num:
    if name[i]==insertName:
        findflag = 1
        break
    i=i+1
print(findflag)
if findflag == 1:
    print("找到了")
else:
    print("没有这个人")
