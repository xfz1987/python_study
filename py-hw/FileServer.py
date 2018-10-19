"""
第三节课 python功能介绍及应用编程作业：
实现一个客户端和一个服务器传输文件的程序 要求指定文件名由客户端发送给服务器，客户端可以从服务器下载文件，不能重复下载和重复上传同一文件（基于MD5或者CRC等摘要校验），可以发送截图或者源码，必须附运行效果截图。
"""

"""
服务端
"""
import socket,os,hashlib
server = socket.socket()
server.bind(('0.0.0.0',9999))
server.listen()
while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("server on....")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename): #是否是文件
            f = open(filename,"rb")
            m = hashlib.md5() #创建md5校验
            file_size = os.stat(filename).st_size #获取文件大小
            conn.send(str(file_size).encode()) #发送文件大小
            conn.recv(1024) #等待ACK交互防止粘包
            for line in f:
                m.update(line) #递增加密文件
                conn.send(line)
            print("file md5",m.hexdigest()) #打印16进制md5
            f.close()
            conn.send(m.hexdigest().encode())
        print("send done")
server.close()