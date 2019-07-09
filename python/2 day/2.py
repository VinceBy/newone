print("="*30)
print("早上好，欢迎进入密室，请输入你的身份：",end="")
ID = input()
if ID=="经理" or ID=="副经理":
    print("你已经进入密室")
else:
    print("身份有误，不得进入")


