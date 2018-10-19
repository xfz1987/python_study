# 内置函数
'''
求绝对值的函数abs: abs(-10) #10
比较函数cmp(x, y) 如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
数据类型转换
    int('123')     #==> 123
    int(12.34)     #==> 12
    float('12.34') #==> 12.34
    unicode(100)   #==> u'100'
    bool(1)        #==> True
    bool('')       #==> False
函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
sb = abs
sb(-1)  #==> 1
'''

# 函数
'''
def 函数名 (参数列表) :
	函数体
	如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
'''
def hello( str ):
	print('hello: %s' %(str))
hello('xfz') # hell: xfz

def f1( a, b ):
	return a + b
print(f1( 3, 4 )) # 7

def f2(a = 1, b = 2):
	return a + b
print(f2()) # 3
print(f2(2)) # 4

# 空函数
'''
如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
	pass
实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
if age >= 18:
	pass  
'''
if 20 >= 18:
	pass # 缺少了pass，代码运行就会有语法错误

# 变量作用域
'''
L 局部作用域
E 闭包函数外的函数中
G 全局作用域
B 内建作用域
由内而外查找
'''
x = int(32) # 内建作用域
g_a = 0 # 全局作用域
def f3():
	o_c = 2 # 闭包函数外的函数中
	def f4():
		i_b = 1 # 局部作用

#参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('bad operand type')
#	if x >= 0:
#		return x
#	else:
#		return -x

#返回多个值
#Python的函数返回多值其实就是返回一个tuple
#只不过是把括号省略了
# import math
# 
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print x, y
# 结果 151.961524227 70.0
# 这只是个假象，其实是(151.961524227, 70.0) tuple 

#函数的参数
#除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
# 1.默认参数（必选参数在前，默认参数在后）
#   def power(x):
#   	return x*x
#
#   计算x的n次方
#   def power(x,n=2):
#   	s = 1
#   	while n>0:
#   		n -= 1
#   		s *= x
#   	return s
#  注意：默认参数必须指向不变对象！
#  def add_end(L=None):
#  	  if L is None:
#  	  	L = []
#  	  L.append('END')
#  	  return L

# 可变参数
# 传入的参数个数是可变的，>=0个
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号
# 在函数内部，参数numbers接收到的是一个tuple
# def calc(*numbers):
# 	sum = 0
# 	for n in numbers:
# 		sum += n*n
# 	return sum
# 	calc(1,2)    #==> 5
# 	calc()       #==> 0
# 如果已经有一个list或者tuple，调用可变参数
# nums = [1,2,3]
# calc(*nums)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 它可以扩展函数的功能
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
# 用**
#    def person(name, age, **other):
#    	 print 'name:',name,'age:',age,'other',other
#    kw = {'city': 'Beijing', 'job': 'Engineer'}
#    person('Jack', 24, **kw)

# 参数组合
# 用必选、默认、可变和关键字参数，可以一起使用，或只用其中某些
# 注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
#  def func(a,b=0,*args,**other):
#  	   print 'a:',a,'b:',b,'args:',args,'other:',other
#  func(1) #==> a = 1 b = 0 args = () kw = {}
#  func(1,2) #==> a = 1 b = 2 args = () kw = {}
#  func(1,2,'a','b') #==> a = 1 b = 2 args = ('a','b') kw = {}
#  func(1,2,'a','b',x=99) #==> a = 1 b = 0 args = ('a','b') kw = {x:99}
#  func(1,2,x=99) #==> a = 1 b = 0 args = () kw = {x:99}
#  args = (1, 2, 3, 4)
#  kw = {'x': 99}
#  func(*args, **kw)#a = 1 b = 2 args = (3,4) kw = {x:99}

# 递归函数
# n! = 1 x 2 x 3 x ... x n
# def fact(n):
# 	 if n == 1:
# 	 	return 1
# 	 return n * fact(n - 1)
# fact(3)     #==> 6
# fact(1000)  #==>栈溢出