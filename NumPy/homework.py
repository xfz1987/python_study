'''
设计一个类，该类可以初始化一个多维数组，指定维度，然后用随机数初始化.提供三个接口
1.计算这个多维数组所有元素的总和
2.将这个多维数组的元素都乘以一个值，返回副本
3.将这个多维数组计算sin值打印出来
'''
import numpy as np

class NArray(object):
  def __init__(self, h, l):
    self.__narray = np.random.randint(0, 10, size=(h,l))
  
  # 创建多维数组
  def get_array(self):
    return self.__narray

  # 计算元素的总和
  def get_sum(self):
    return np.sum(self.__narray)

  # 乘法
  def get_multiply_val(self, n):
    return self.__narray * n

  # 计算sin
  def get_sin_val(self):
    return np.sin(self.__narray * np.pi/180)
    
a = NArray(3, 5)
print(a.get_array())
print(a.get_sum())
print(a.get_multiply_val(2))
print(a.get_sin_val())