'''
python链接mysql
1.设置编码模式
2.用完记得关闭
'''
import MySQLdb
db = MySQLdb.connect('localhost', 'username', 'password', 'dbname', 'tablename', charset='utf8')
cursor = db.cursor()
cursor = execute('select * from tablename')
data = cursor.fetchone()
print(data)
db.close()

'''
# Mysql连接池设计
1.在内部对象池维护一定数量的数据库连接
2.对外部暴露数据库连接获取和返回方法
3.外部使用者通过 getConnection 方法获取连接，使用完毕后再通过 releaseConnection
4.方法将连接返回，注意此时连接并没有关闭，而是由连接池管理器回收，并为下一次使用做准备
5.由系统维护两个队列：busy和free队列，初始化放入free中，每取一个(检查free是否为空，设置一个size,如果为空，需要线程等待)放入busy一个，用完后再放回到free队列（还要检查free的size）

'''