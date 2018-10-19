'''
# 服务端：与客户端不同之处在于，服务端需要先bind，然后才能接受新的客户端连接
'''
import socket,os,hashlib,time,json

FILE_PATH = '/Users/xfz/mywork/AI/python_study/sockect_demo/server_files/'

def get(conn, filename):
  if os.path.exists(filename) and os.path.isfile(filename):
    f = open(filename, 'rb')
    m = hashlib.md5()
    file_size = os.stat(filename).st_size
    conn.send((str(file_size)).encode())
    conn.recv(1024)
    for line in f:
      m.update(line)
      conn.send(line)
    f.close()
    print('md5:', m.hexdigest())
    time.sleep(0.5)
    conn.recv(1024)
    conn.send(m.hexdigest().encode())
    print('send done')
  else:
    conn.send('0'.encode())

def put(conn, filename):
  if os.path.exists(filename):
    conn.send('0'.encode())
    conn.close()
  else:
    f = open(filename, 'wb')
    send_size = conn.recv(1024)
    file_size = int(send_size.decode())
    re_size = 0
    conn.send('xfz'.encode())
    cm = hashlib.md5()
    while re_size < file_size:
      if file_size - re_size > 1024:
        size = 1024
      else:
        size = file_size - re_size
      data = conn.recv(size)
      re_size += len(data)
      f.write(data)
      cm.update(data)
    sm = conn.recv(1024)
    if cm.hexdigest() == sm.decode():
      conn.send('1'.encode())
    print('recvie over...')
    f.close()

def _get_filename(filename):
  return FILE_PATH + filename

def ls(conn):
  cm = conn.recv(1024)
  res = os.listdir(FILE_PATH)
  res = json.dumps(res)
  conn.send(res.encode())

def main():
  server = socket.socket()
  port = 8888
  server.bind(('localhost', port))
  print('server start...')
  while True:
    server.listen()
    conn, addr = server.accept()
    print('addr:', addr)
    while True:
      data = conn.recv(1024)
      print(data)
      if not data:
        print('client has closed')
        break
      cmd, filename = data.decode().split()
      filename = _get_filename(filename)
      if cmd == 'get':
        get(conn, filename)
      elif cmd == 'put':
        put(conn, filename)
      elif cmd == 'ls':
        ls(conn)
  server.close()

if __name__ == '__main__':
  main()