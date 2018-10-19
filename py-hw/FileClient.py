"""
第三节课 python功能介绍及应用编程作业：
实现一个客户端和一个服务器传输文件的程序 要求指定文件名由客户端发送给服务器，客户端可以从服务器下载文件，不能重复下载和重复上传同一文件（基于MD5或者CRC等摘要校验），可以发送截图或者源码，必须附运行效果截图。
"""

"""
客户端
"""

import socket
import hashlib
client = socket.socket()
client.connect(('localhost',9999))
while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0:continue
    if cmd.startswith("get"): #是否以get开头
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server respoense:",server_response)
        client.send(b"ready to recv file")　　#发送ACK确认，交互防止send粘包
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new","wb")
        m = hashlib.md5() #使用md5加密
        while received_size < file_total_size:　　#判断总数据比递增接收数据大就成立
            if file_total_size - received_size > 1024: #数据比recv大就成立
               size = 1024
            else: #最后一次，还剩多少
               size = file_total_size - received_size　　#求出剩余recv数值
               print("last receive:",size) #最后一次收了多少
            data = client.recv(size)
            received_size += len(data)　　#递增接收数据
            m.update(data) #递增接收数据并加密md5
            f.write(data)
            #print(file_total_size,received_size) #每次发送大小
        else:
            new_file_md5 = m.hexdigest()
            print("file recv done",received_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print("server file md5:",server_file_md5)
        print("client file md5:",new_file_md5)
client.close()