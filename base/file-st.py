'''
# 读文件
f = open(filename, 'w')
r:读
w:写   # 记得加换行符 \n
+ 读写，w+会截断真个文件，r+不会

# 基本方法
read()   # 可以指定读多少的字节
write()  # 可以指定写入多少字节
readline()   # 读取一行
readlines()  # 读取所有行，并以列表形式返回
writelines() # 写入一个列表

readline()每次只读取一行，通常比 .readlines()慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用.readline()

writeline()是输出后换行，下次写会在下一行写。write()是输出后光标在行末不会换行，下次写会接着这行写

# 建议用多线程来读写文件

# 读写完要 f.close()

# tell()  返回文件当前位置，用于多线程边读边写
# flush() 刷新文件缓冲区
# next()  返回文件下一行
'''

import sys
with open('filename') as f:
    while True:
        line_str = f.readLine()
        if not line_str:
            break
        print(line_str)
f.close()

f = open('filename', 'r')
list_str = f.readLines()
print(list_str)
f.close()