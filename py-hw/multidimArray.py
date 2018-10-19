"""
第四节课  python numpy 介绍：
作业1：
设计一个类，该类可以初始化一个多纬数组，指定维度，然后用随机数初始化。提供三个接口：
①计算这个多维数组所有元素等总和
②将这个多维数组里面的所有元素乘以一个值，返回副本
③将这个多维数组的元素计算sin值打印出来
"""
import numpy as np

# 多维数组类
class  multidimArray(object):
    
    # 构造函数
    """
    shape为维度参数，输入表示维度的元组，默认为0维
    例如： 
    shape = (2,3) , 秩为2，2*3的二维数组
    shape = (2,3,3,4)  秩为4，2*3*3*4的四维数组
    """
    def __init__(self, shape = None):
        self.ma = np.random.random_sample( shape) 
    
    #计算元素总和
    def sum(self):
        pass
    
    # 乘一个值返回副本
    def multiplication(self, num):
        return self.ma * num
    
    # sin
    def sin(self):
        return np.sin(self.ma)
    
    # 打印自己的信息
    def print(self):
        print( '%d 维数组：' % self.ma.ndim )
        print(self.ma)
        
# for test
obj = multidimArray( (2,3,4) )
obj.print()
print('--------')
print( obj.sin() )
print('--------')
print(obj.multiplication(4))
obj.print()