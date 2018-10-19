'''
# 客户端
# 上传文件：指定文件名发送给服务器，不能重复上传
# 下载文件: 指定文件名下载，不能重复下载
# 基于MD5或则
'''
import socket,os,hashlib,time,json

FILE_PATH = '/Users/xfz/mywork/AI/python_study/sockect_demo/local_files/'

def ls(client, filename):
  client.send('ls'.encode())
  res = client.recv(1024)
  data = json.loads(res.decode())
  for i in data:
    print(i)

def put(client, filename):
  f = open(filename, 'rb')
  m = hashlib.md5()
  file_size = os.stat(filename).st_size
  client.send((str(file_size)).encode())
  client.recv(1024)
  for line in f:
    m.update(line)
    client.send(line)
  f.close()
  time.sleep(0.5)
  client.send(m.hexdigest().encode())
  resul = client.recv(1024)
  if resul.decode() == '1':
    print("send successed")
  else:
    print("send fail")

def get(client, filename):
  if os.path.exists(FILE_PATH + filename):
    print('文件本地已经存在')
  else:
    ser_respondse = client.recv(1024)
    client.send('ready recv'.encode())
    if ser_respondse.decode() != '0':
      file_size = int(ser_respondse.decode())
      f = open(FILE_PATH + filename, "wb")
      re_size = 0
      cm = hashlib.md5()
      while re_size < file_size:
        if file_size - re_size > 1024:
          size = 1024
        else:
          size = file_size - re_size
        data = client.recv(size)
        re_size += len(data)
        f.write(data)
        cm.update(data)
      client.send('xfz'.encode())
      sm = client.recv(1024)
      if cm.hexdigest() == sm.decode():
        print("load success")
      f.close()
    else:
      print("no this file..")

def _get_filename(filename):
  return FILE_PATH + filename

def main():
  client = socket.socket()
  client.connect(('localhost', 8888))
  while True:
    msg = input('请输入操作:').strip()
    print(msg)
    if len(msg) == 0:
      continue
    client.send(msg.encode())
    cmd, filename = msg.split()
    if cmd == 'get':
      get(client, filename)
    elif cmd == 'put':
      filename = _get_filename(filename)
      put(client, filename)
    elif cmd == 'ls':
      ls(client, filename)
  client.close()

if __name__ == '__main__':
    main()