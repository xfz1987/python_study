"""
第二节课 python功能介绍及应用编程作业：
设计一个文件管理类，提供三个功能接口：
获取指定目录下的文件总数目（包括普通文件和目录），
删除指定目录下的指定普通文件，
获取指定目录下的指定文件或者目录的最后修改时间（以UTC时间打印出来）。
"""

# 文件类
import os, sys, datetime
class MyFile(object):
    def __init__(self):
        pass
    
    # 功能接口1.获取指定目录下的文件总数(包括普通文件和目录）
    def file_number(self, path = None):
        if path is None :    # 如果没有传入路径就默认读取当前路径
            path = os.getcwd()
        print('count:%d' %len( os.listdir( path ) ) )  #得到目录下的文件总数
    
    # 删除指定目录下的指定普通文件
    def del_file(self,pathname):
        os.remove(pathname)
    
    # 获取制定目录下的指定文件或者目录的最后修改时间（UTC）
    def get_filetime(self, pathname):
        tm =  os.path.getmtime(pathname)   # 获取文件最后修改的时间戳
        date = datetime.datetime.fromtimestamp(tm)  #时间戳转datetime类型
        print( date.strftime('%Y-%m-%d %H:%M:%S') )  # 格式化输出时间

# for test
obj = MyFile()
obj.file_number()
obj.get_filetime( os.getcwd() )
obj.del('./aaa.txt')