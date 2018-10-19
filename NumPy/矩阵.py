import numpy as np
import numpy.matlib

# 返回一个新的空矩阵,但不是初始化元素
a = np.matlib.empty((2,1), 'float64')
print(a)
'''
[[0.00000000e+000]
 [2.68156175e+154]]
'''

# zeros和ones
a = np.matlib.ones((2,2), 'float64')
print(a)
'''
[[1. 1.]
 [1. 1.]]
'''
a = np.matlib.zeros((2,2), 'float64')
print(a)
'''
[[0. 0.]
 [0. 0.]]
'''

# eye(n=行数, M=列数, k=0, dtype='float64'): 返回对角线为1，其他位置为0的矩阵
# k表示 对角线的起始位置
a = np.matlib.eye(n=3, M=4, k=0, dtype='float64')
print(a)
'''
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]
'''
a = np.matlib.eye(n=4, M=4, k=1, dtype='float64')
print(a)
'''
[[0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]
 [0. 0. 0. 0.]]
'''


# rand(m,n) 返回mxn矩阵，随机数填充
a = np.matlib.rand(3,3)
print(a)
'''
[[0.1773171  0.21144999 0.13272415]
 [0.47931822 0.82849146 0.56691419]
 [0.47998563 0.50190955 0.71817041]]
'''
