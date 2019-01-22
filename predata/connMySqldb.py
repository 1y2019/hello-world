#Python-MySQL数据库连接
import mysql.connector

#创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="runoob_db"
)

#创建游标
mycursor = mydb.cursor()
#如果sites表存在删除
mycursor.execute("drop TABLE IF EXISTS sites ")
#创建表
mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
#插入数据SQL 语句
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
#变量赋值
val = [
  ("RUNOOB", "https://www.runoob.com"),
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/'),
  ("Zhihu", "https://www.zhihu.com")
]

#删除数据
sqldel = "DELETE FROM sites "
mycursor.execute(sqldel)

#执行插入
mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

#查询打印
mycursor.execute("SELECT * FROM sites  ")
for row in mycursor.fetchall():
    name=row[1]
    url=row[2]
    print("name=%s,url=%s" %(name,url))

#关闭游标
mycursor.close()
#关闭数据库连接
mydb.close()







