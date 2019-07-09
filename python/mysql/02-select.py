#encoding=utf8
import pymysql

try:
    conn = pymysql.Connect(host='localhost',port=3306,db='python3',user='root',passwd='chuanzhi',charset='utf8')
    cur=conn.cursor()
    #查询一条数据
   # cur.execute('select * from students where id =4 ')
   # result = cur.fetchone()
   #查询多条数据
    cur.execute('select * from students')
    result = cur.fetchall()
    print(result)
    cur.close()
    conn.close()
except Exception as e:
    print(e)
