#通过ｐｙｔｈｏｎ链接数据库实现一些增删改查的操作
from pymysql import *

class mysql:
    def __init__(self,host,db,user,passwd,charset='utf8',port=3306):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def open(self):
        self.conn = Connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.cursor.close()

#进行增删改操作
    def cud(self,sql,params=[]):
        try:
            print(sql,params)
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
            print("ok")
        except Exception as e:
            print(e)

#进行查所有数据操作
    def all(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql)
            self.conn.commit()
            result =  self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)

#进行查单个数据操作
    def one(self,sql,params=[]):
        try:
            self.open()
            self.cursor.execute(sql,params)
            self.conn.commit()
            result = self.cursor.fetchone()
            self.close()
            return result
        except Exception as e:
            print(e)

def main():
    name = input('请输入学生的姓名：')
    passwd = input('请输入密码：')

    sqlhelper = mysql('localhost','python3','root','mysql')
    params=[passwd]
    print("================")
    #增
    sql1 = "insert into lianxi(name,passwd) values(%s,%s)"
    #改
    sql1 = 'update lianxi set name=%s where id=%s'
    #删
    sql1 = 'delete from lianxi where id = %s'    
    print(sql1)
    #sqlhelper.cud(sql1,params)
    #查询全部
    sql2 = 'select * from lianxi'
    result = sqlhelper.all(sql2)
    print(result)
    sql3 = 'select * from lianxi where id =%s'
    id = input('请输入要查询的ＩＤ') 
    result = sqlhelper.one(sql3,[id])
    print(result)

        
main()
