#1，提示并获取用户名
UserName = input("请输入用户名：")

#2,提示并获取密码
passwd = input("请输入密码：")

#3,判断用户名和密码都相等，根据判断的结果显示信息
if UserName=="baiyu" and passwd=="123456":
    print("登录成功，欢迎进入系统")
else:
    print("密码或用户名不正确")




