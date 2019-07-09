#coding = utf-8
from pymysql import *

try:
    name = input("请输入用户名:")
    conn = Connect(host='localhost',port=3306,user='root',passwd='chuanzhi',db='python3',charset='utf8')
    cursorl = conn.cursor()
#    sql = 'insert into students values(5,"过小儿")'
#    sql = 'update students set sname="王二小" where id = 5'
#    sql = 'delete from students where id = 5'
    params = [6,name]
    sql = 'insert into students values(%s,%s)'
#    cursorl.execute(sql)
    cursorl.execute(sql,[6,name])
    conn.commit()
    cursorl.close()
    print("ok")
except Exception as e:
    print('exception',e)

