'''
# 安装numpy: python3 -m pip install numpy
# 数组的算数和逻辑运算
# 计算函数（正玄函数、线性代数、随机数等）
'''

'''
# 多维数组 ndarray
  ndarray中的每个数据类型必须一样
  数据类型对象 dtype
  可以通过切片提取任何元素
  先放行，再放列

# 方法
  ndarray.ndim     获取数组的维数
  ndarray.shape    获取几行几列
  ndarray.size     数组的元素个数
  ndarray.itemsize 数组中每个元素的大小
'''
import numpy as np
a = np.arange(15).reshape(3,5) # 0-14 3行5列的2维数组
print(a)
"""
[
  [ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]
]
"""
print(a.ndim)  # 2
print(a.shape) # (3, 5)
print(a.size)  # 15
print(a.itemsize) # 8

# 动态创建多维数组
b = np.array([2, 3, 4])
print(b.dtype)  # 'int64'
print(b.ndim)   # 1

# 数组上的减法运算
a = np.array([20, 30, 40, 50])
b = np.array([10,11,23,11])
c = a - b
print(c)
# [10, 19, 17, 39]

# 数组上的乘法
d = 3
c = a * d
print(c)
# array([60, 90, 120, 150])

'''
# ndarray 对象的内容可以通过索引或切片来访问和修改
slice(start, stop, step) 不包含stop
此slice对象被传递给数组来提取数组的一部分
'''
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])   # [2, 4, 6]
print(a[2:5]) # [2, 3, 4]

'''
# 高级索引
  基于N维索引来获取数组中任意元素，每个整肃数组表示该维度的下标值
'''
x = np.array([[1,2], [3,4], [5,6]])  # 2维数组
y = x[[0,1,2], [0,1,0]]
print(y)
"""
1,2    0, 1, 2,
3,4.   0, 1, 0
5,6

(0,0) 第0行0列 
(1,1) 第1行1列
(2,0) 第2行0列
[1, 4, 5]
"""

'''
#ones、zeros 函数
 ones返回特定大小，以1来填充
 zeros返回特定大小，以0来填充
'''
x = np.ones(5)
print(x) # [1,1,1,1,1]
y = np.zeros(3)
print(y) # [0,0,0]


'''
# linspace 函数
  类似于arange函数，指定了范围之内的均匀间隔数量，注意：不是步长
  numpy.linspace(start, stop, num, endpoint, retstep,dtype)
   * start     序列的起终值
   * end       序列的终止值，如果endpoint为true，该值包含于序列中
   * endpoint  序列中是否包含num要生成的样例数量，默认为50
   * retstep   如果为true，返回样例，以及连续数字之间的步长
   * dtype     输出ndarray的数据类型
   * 步长 = (end - start) / (num - 1)
'''
x = np.linspace(10,20,5)
print(x) # [10, 12.5, 15, 17.5, 20]

y = np.linspace(10,20,11) # [10,11,12,13,14,15,16,17,18,19,20]


'''
# 位操作
  bitwise_and   对数组元素执行位 与 操作   1&1 -> 1  1&0 -> 0  0&0 -> 0  两个都是1才是1
  bitwise_or    对数组元素执行位 或 操作   1|1 -> 1  1|0 -> 1  0|0 -> 0  有一个是1就是1
  left_shift    向左移动二进制表示的位     0011 向左移1位，用0来补位  1100  1100000 左移1位 1000000  顶部1位丢弃掉
  right_shift   向右移动二进制表示的位     1100 向右移1位，用0来补位  0110  0000011 右移1位 0000001  尾部1位丢弃掉了 
'''
a = 2  # 10
b = 3  # 11
print(np.bitwise_and(a, b)) # 10 -> 1*2的1次方 + 0*2的0次方 -> 2
print(np.bitwise_or(a, b)) # 11 -> 1*2的1次方 + 1*2的0次方  -> 3 
print(np.left_shift(a, 1)) # 10 左移动1位  0100  -> 4
print(np.left_shift(a, 2)) # 10 左移动2位  1000  -> 8
print(np.right_shift(a, 1)) # 10 右移动1位  01  -> 1

'''
# 字符串函数
  add()        两个str或Unicode数组的逐个字符串连接
  replace()    替换
  split()      分割
  title()      返回输入字符串的按元素标题替换版本，其中每个单词的首字母都大些
  multiply()   返回按元素多重连接后的字符串
'''
print(np.char.multiply('hello ', 3)) # hello hello hello
print(np.char.title('hello xfz'))    # Hello Xfz


'''
# 算数函数
  正弦函数
  余弦函数
  正切函数
'''
a = np.array([0, 30, 45])
print(np.sin(a*np.pi/180)) # sin0 sin30° sin45°  [0, 0.5, 0.70710678]
print(np.cos(a*np.pi/180)) # [1, 0.8660254, 0.70710678]   sin60° = √3/2
print(np.tan(a*np.pi/180)) # [0, 0.57735027, 1]  tan30 = sin30/cos30 = 1/2÷√3/2=√3/3


# 四舍五入
a = np.array([1.0, 5.56, 12])
print(np.around(a))  # [ 1,6,12]
print(np.around(a, decimals=1)) # [1, 5.7, 12]
print(np.floor(a)) # [1, 5, 12]
print(np.ceil(a)) # [1, 6, 12]

# 加、减、乘、除
a = np.arange(9).reshape(3,3)
print(a)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
b = np.array([10, 9, 8])
print(np.add(a,b))
'''
[[10 10 10]
 [13 13 13]
 [16 16 16]]
'''
print(np.subtract(a,b))
'''
[[-10  -8  -6]
 [ -7  -5  -3]
 [ -4  -2   0]]
'''
print(np.multiply(a,b))
'''
[[ 0  9 16]
 [30 36 40]
 [60 63 64]]
'''
print(np.divide(a,b))
'''
[[0.         0.11111111 0.25      ]
 [0.3        0.44444444 0.625     ]
 [0.6        0.77777778 1.        ]]
'''

# 倒数
a = np.array([1,2.0,4.0])
print(np.reciprocal(a)) # [1.   0.5  0.25]

# power(底数，幂数)
a = np.array([1,2,3])
b = np.array([2,3,3])
print(np.power(a,b)) # [1,8,27]






