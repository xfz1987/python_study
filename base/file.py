# 文件管理类

import os, time

class FileManager(object):
    # 检查目录后文件是否存在
    def _is_exist(self, path):
        return os.path.exists(path)
    
    # 将time转化为显示时间
    def _time_toString(self, timestrap):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestrap)) 
        
    # 获取指定目录下的文件总数(包括文件和目录)
    def get_file_total(self, path):
        if self._is_exist(path):
            return len(os.listdir(path))
        else:
            print('%s 不存在' % path)
            
    # 删除指定目录下的指定普通文件
    def delete_file(self, path, filename):
        if not path[-1] == '/':
            path += '/'
        
        file = path + filename
        
        if self._is_exist(file):
            os.remove(path + filename)
            print('【删除成功】')
        else:
            print('【删除失败】%s 文件不存在' % (file))
            
    # 获取指定目录的指定文件或目录的最后修改时间
    def get_last_modify_time(self, path, filename):
        if not path[-1] == '/':
            path += '/'
        
        file = path + filename
        
        if self._is_exist(file):
            timestrap = os.path.getmtime(file)
            return self._time_toString(timestrap)
        else:
            print('%s 不存在' % (file))

fm = FileManager()
file_count = fm.get_file_total('/Users/xfz/Desktop/my_test')
print(file_count)
fm.delete_file('/Users/xfz/Desktop/my_test', '1.txt')
last_time = fm.get_last_modify_time('/Users/xfz/Desktop/my_test', '2.txt')
print(last_time)
