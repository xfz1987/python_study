'''
# 客户端和服务端
# 服务端：与客户端不同之处在于，服务端需要先bind，然后才能接受新的客户端连接
'''
import socket
# 客户端
s = socket.socket()
host = socket.gethostname()
port = 8888
s.connect((host, port))
print(s.send('hello'))
s.close()

# 服务端
# 1.需要把客户端放在队列里，如果很长时间没有心跳，则关掉它
# 2.协议的可靠性，防止CC攻击，在消息头里面设置（head bodysize:100, bodymd5:xxx，recv(100)计算一个md5，进行对比）
# 
import socket
s = socket.socket()
port = 8888
s.bind('localhost', port)
s.listen(5)   # 设置最多连接5个
print('listen success')
while True:
  c.addr = s.accept()
  print('get a connection\n')
  print(c.recv(24)) # 先接受24字节消息头的内容
  c.close()