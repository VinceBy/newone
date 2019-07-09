#coding = utf-8

from MysqlHelper import MysqlHelper
from hashlib import sha1

#接收用户输入
name = input("请输入用户名:")
pwd = input("请输入密码:")
#对密码加密
s1 = sha1()
s1.update(pwd.encode())
pwd2 = s1.hexdigest()

#根据用户名查询密码
sql = 'select passwd from users where name = %s'
helper = MysqlHelper('localhost',3306,'python3','root','mysql')
result = helper.all(sql,[name])
if(len(result)==0):
    print("用户名错误")
elif(result[0][0]==pwd2):
    print("登陆成功")
else:
    print("密码错误")
