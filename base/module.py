# 模块
# import 文件名
# from 文件名 import 函数/类
# from AAA import getMyFuc as my
# 全局变量都抽取到一个公共的py,然后通过import引入

# os模块 import os
# os.getcwd() 获取当前工作目录, (list)
# os.listdir(os.getcwd()) 活泉当前目录下所有的文件和目录 (list)
# os.path.getsize('/Users/xfz/Desktop/test.html') 获取文件大小

# heap 实际上是一个最小堆，主要用于实现优先级队列，堆顶元素 a[0] 永远是最小的
# heappush(heap,x), 往堆里面push一个元素x 
# heapify(heap) 让列表heap具有堆特性，(它被描绘成一个二叉树结构，实际存储的还是数组, 根结点i表示，左节点 2*i+1 右节点2*i+2，i对应的是数组的索引号)
# heappop(heap) 从堆里弹出最小堆元素
# heapreplace(heap,x) 弹出最小元素，并且将x压入堆
from heapq import *
list_heap = [5,4,3,6,99,1]
heapify(list_heap)
print(list_heap) # [1, 4, 3, 6, 99, 5]
heappush(list_heap, -9)
print(list_heap) # [-9, 4, 1, 6, 99, 5, 3]
print(heappop(list_heap)) # -9
print(list_heap) # [4, 1, 6, 99, 5, 3]
print(heapreplace(list_heap, -100)) # 1
print(list_heap) # [-100, 4, 3, 6, 99, 5]

# 队列
from collections import deque
d = deque()
d.append(5)
d.append(4)
d.append(3)
d.append(2)
print(d) # deque([5, 4, 3, 2])
d.popleft()
print(d)

# time
import time
print(time.time())

import sys
# import moduleA
from moduleA import test, fuck

# print(sys.path)

# moduleA.test()

test()
fuck()

# dir(模块) 在python中 可以查看模块的提供内容

#绝对值
print abs(-10)#10
#比较函数
print cmp(1,2)#-1

# return 多个值
import math
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y + step * sin.cos(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)

# 可变参数
def calc(*number):
	sum = 0
	for n in number:
		sum = n * n
	return sum
calc(1, 2) # 5
calc() # 0

def person(name, age, **other):
	pass

# def func(a, b=0, *args, **other):
# 	print 'a:',a,'b:',b,'args:',args,'other:',other
# func(1)#a = 1 b = 0 args = () kw = {}
# func(1,2)#a = 1 b = 2 args = () kw = {}
# func(1,2,'a','b')#a = 1 b = 2 args = ('a','b') kw = {}
# func(1,2,'a','b',x=99)#a = 1 b = 0 args = ('a','b') kw = {x:99}
# func(1,2,x=99)#a = 1 b = 0 args = () kw = {x:99}
# args = (1, 2, 3, 4)
# kw = {'x': 99}
# func(*args, **kw)#a = 1 b = 2 args = (3,4) kw = {x:99}


'''
random 模块
from random import *
a = random() # [0,1)

for i in range(0, 1):
  a = uniform(1, 100) # 返回一个a-b的随机数，注意：如果一个数特别大，如果多线程在处理，会出问题，因此尽量在单线程使用该函数
'''