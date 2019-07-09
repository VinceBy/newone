#coding=utf-8
from MysqlHelper import *
#修改
#name = input('请输入学生姓名')
#id1 = input('请输入学生编号')
#sql = 'update students set sname=%s where id=%s'
#params = [name,id1]

#sqlhelper = MysqlHelper('localhost',3306,'python3','root','mysql')

#sqlhelper.cud(sql,params)

#查询
sql = 'select id, sname from students where id < 3'
sqlhelper = MysqlHelper('localhost',3306,'python3','root','mysql')
result = sqlhelper.all(sql)
print(result)

