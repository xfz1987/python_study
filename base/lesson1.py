#!usr/bin/python3

# python是一种解释型语言，运行速度慢，但代码简洁
# 注意: #python语句首尾不能有空格和空行
# 建议使用空格，不建议使用tab键

# 数据类型
"""
Number  正数、负数、0
Float   浮点数（浮点数运算则可能会有四舍五入的误差）
String  字符串
Bool    布尔值 True、False
None    空值   None不能理解为0，因为0是有意义的，而None是一个特殊的空值

Python把 0、空字符串''和 None看成 False,其他数值和非空字符串都看成 True

List    列表
Tuple   元组
Set     集合
Dictionary 字典
"""

'''
int
float
bool
complx (复数)
'''
a = 10
b = 2.3
c = True
d = 'abc'
e = 3 + 4j  # python中复数类型，虚数只能用字母j
type(a) # <class 'int'>
print(e)

# 变量(只有赋值后变量才会被创建，如果只定义 b1，则b1未被创建)
# 变量名必须是大小写英文、数字和_，且不能用数字开头，大小写敏感
a1 = 200
_b1 = 'abc'
a = b = c = 1
a, b, c = 1, 2.5, 'abc'
del a # 删除 a，没有a了

# 运算符
'''
算数运算符
2 ** 3  # 8 幂运算, 2的3次方
7 // 3  # 2 取整余，去掉余数，只要商

# 比较运算符
== != > < >= <=

# 赋值运算符
= += -= *= /= %= **= //=

# 逻辑运算发
(&& || !   # java or js) 
and or not # python

# 位运算符
& | ^ ` << >>

# 成员运算符
in, not in

# 身份运算符
is, is not
is与==的区别：
== 用来比较value是否相同
is 比较的是对象间的唯一标识id，其实可以理解为javascript中的 ===

int/string is 与 list 一样, 因为id相同
a = 1
b = 1
a is b # True
a == b # True

list/set/dic：要看id 
x = y = [1]
z = [1]
x == y == z # True
x is y # True id相同，
x is z # False 因为id不同


# 运算符优先级
最低级别是逻辑运算符
'''

# 字符串（python是没有字符类型的）
# 字符串是不可变对象，list是可变对象
# 将数字转化成字符串 str(123) #==> '123'
# 单引号：输出特殊字符需要转义（注意）
# 双引号：输出特殊字符不需要转义
# 三引号：输出特殊字符不需要转义

a = 'a'
b = "b"
c = """
abcdddeessa
ssssss
"""
str1 = 'abcde'
str1[:3] + '123' + str1[3:]# abc123de ²åÈë
str1.index('b') # 1
str1.rindex('b') # 1 相当于lastIndex
'abcde%d' %(12345)# abcde12345
'abcde%s' %('mzk')
'name: %s, age: %d' %('xfz', 18)# name: xfz, age: 18
# str.find() # 同 index
# str.lower() # 返回 变为小写的字符串
# str.replace('', '') # 注意：不能使用正则表达式
# str.split(',') # 字符串拆分，同js
# join
xsb = ['hello', 'xfz', '!']
hello = ' '.join(xsb)
print(hello)
# 字符串反转
print(hello[::-1]) # ! zfx olleh


# 文件编码
# 文件头部声明 # encodeing=utf8



# 字符串模板
#'Hello %s' % 'world' #==>Hello, world 
#'Hi, %s, you have $%d.' % ('Michael', 1000000)
#  %运算符就是用来格式化字符串的
#  在字符串内部，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
#  %d	表示用整数替换
#  %f	表示用浮点数替换
#  %s	表示用字符串替换
#  %x	表示用十六进制整数替换
#  用%%来表示一个%
#  格式化整数和浮点数还可以指定是否补0和整数与小数的位数
#  '%.2f' % 3.1415926 #==>3.14