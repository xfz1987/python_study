#!/usr/bin/env python

import os

# 仅在Linux系列的操作系统上才能运行
print('process (%s) start...' % os.getpid())

pid = os.fork()

if pid == 0:
  print('child process, pid: %s, ppid: %s' % (os.getpid(), os.getppid()))
else:
  print('parent process, pid: %s, child pid: %s' % (os.getpid(), pid))

'''
# windows

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
  print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
  print('Parent process %s.' os.getpid())
  p = Process(target=run_proc, args=('test',))
  print('Child process will start...')
  p.start()
  p.join()
  print('Child process end.')
'''


