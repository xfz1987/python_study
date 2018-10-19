# 内置数据结构

'''
List (列表): 是一种有序的集合，可以随时添加和删除其中的元素，可变的
  [var1, var2, var3] 可以看成是数组

Tuple (元组): 有序列表,即元组,只读的，不可改变（一旦初始化就不能修改）
  (var1, var2, var3)
  不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

Set (集合): 无序的，key值不能重复，无value，并且key必须是不可变类型
  {var1, var2, var3}

Dictionary (字典): 类似map: 无序的key:value，并且key必须是不可变类型，key必须是唯一的
  {key1:var1, key2:var2, key3: var3}
  查找速度极快，dict内部存放的顺序和key放入的顺序是没有关系的
'''

"""
总结: 
1.list与tuple为一类，只是tuple为不可变
2.string 元组 列表 都属于序列，因此都可以循环
3.set与 dict key值必须是不可变对象，判断有没有都可以用 in
4.dict与list比较
  dict:查找和插入的速度极快，不会随着key的增加而增加；需要占用大量的内存，内存浪费多。
  list:查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。
  所以，dict是用空间来换取时间的一种方法
  在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
  而list是可变的，就不能作为key
5.注意：
  初始化set，要写成 set()，而不能写成{}, {}被认为是一个空的dict
"""
print('List ==================================')
list1 = ['abc', 123, 3.14, True]

# 获取长度
print(len(list1)) # 4

# 获取元素的下标
print(list1.index(3.14)) # 2

# 遍历
for l in list1:
	print(l)

# 通过下标取值
print(list1[2]) # 3.14

# 支持负数标
print(list1[-1]) # True

# 尾追加一个元素 list.append(元素)
list1.append('end') # list ['abc', 123, 3.14, True, 'end']

# 把元素插入到指定的位置 list.insert(索引, 元素)
list1.insert(2, 'insert') # list ['abc', 123, 'insert', 3.14, True, 'end']

# 要删除list末尾的元素， list.pop()
print(list1.pop()) # 返回被删除的元素  list ['abc', 123, 'insert', 3.14, True]

# 要删除指定位置的元素， list.pop(索引)
print(list1.pop(1)) # 返回 123   list ['abc', 'insert', 3.14, True]

# del 也可以删除元素
print(del list1[0]) # 删除第0个位置的元素
print(del list1[-1]) # 删除第0个位置的元素


# 某元素替换成其他元素， list[1] = 'Marry'
list1[1] = 'marry'

# 计数，返回元素在列表中出现的次数  list.count(元素)
print('sdfsd:',list1.count('s')) # 1 

# 合并两个list 用 + 号即可，太方便了
list2 = ['a', 'b', 'c']
list1 += list2

# 排序 sort、reverse
list3 = [3,1,4,0]
list3.sort()
print(list3) # [0, 1, 3, 4]

# sorted, 返回排序后的元素副本，并不修改原列表
list_y = [4,1,3,5]
list_n = sorted(list_y)
print(list_n) # [1,2,3,4]
print(list_y) # [4,1,3,5]

# 清空 list.clear()
list3.clear() # []

# list[起始下标 : 结束下标]，但不包含结束
list4 = [1, 2, 3, 4]
list4[1:3] = ['a', 'b']
print(list4) # [1, 'a', 'b', 4]

# copy() 复制一个列别
newList = copy(list4)

print('Tuple ==================================')
# 获值类方法与list一样

# 定义一个只有1个元素的tuple
t = (1)

# 也有切片功能

# 输出多次 * n，没什么用
tuple = ('abc', 123)
print(tuple * 2) # ('abc', 123, 'abc', 123)

# 也可以链接另一个元组

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 所以，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
t1 = ('a', 'b', ['A', 'B']) 
t1[2][0] = 'X' # ('a', 'b', ['X', 'B'])


print('Set ==================================')
set1 = {'Tom', 'Marry', 'Jack', 'Rose', 'Tom'} # {'Tom', 'Marry', 'Jack', 'Rose'} 重复项Tom被干掉了
set2 = set('abcde') # {'b', 'c', 'e', 'd', 'a'} 每次打印的顺序不一样
set3 = set([1, 2, 3]) # {1, 2, 3}
# 添加  s.add(key)
set3.add(4) # set {1, 2, 3, 4}
# 删除  s.remove(key)
set3.remove(2) # set {1, 3, 4}
# 某key是否在set中 in
if 'Tom' in set1:
	print('Tom 在集合中')
else:
	print('Tom 不在集合中')

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 交集
s3 = s1 & s2 # s3 {2, 3}
# 并集: 
s4 = s1 | s2  # s4 {1, 2, 3, 4])
# 差集
s5 = s1 - s2  # s5 {1}
s6 = s2 - s1  # s6 {4}
# 交集不存在的
s7 = s1 ^ s2  # s7 {1, 4}

s3 = set('abc') # {'a', 'b', 'c'}


# set的原理和dict一样，所以，


print('dict ==================================')

score = {'xfz':99,'zc':100,'rc':85}
# 取值
score['xfz'] # 99
score.get('xfz') # 99
# 添加
score['xb'] = 66
# 判断key是否存在  in 或 get 两种方式
'zc' in score # True
score.get('wb') == None # True
# 删除key
score.pop('xb') # 66
# 删除key
del score['xfz']

# 把一个list转化成dict
item = [('name','ss'),('age',24)]
d = dict(item)
print(d)  # {'name': 'ss', 'age': 24} 

# copy 与 deepCopy
# copy返回时原来字典的一个引用，而deepCopy 深度拷贝啦
from copy import deepcopy
d1 = {'xfz':99,'zc':100,'rc':85}
d2 = d1.copy()
d3 = deepCopy(d1)

# 遍历 for key in dict
my_dict = {'name':'xfz', 'age':16}
for key in my_dict:
    print(my_dict[key]) # xfz 16
# 遍历 for key, value in list.items() 同时遍历出key和value
my_dict = {'name':'xfz', 'age':16}
for key, value in my_dict.items():
    print(key, value)

# keys方法返回字典中所有的键
print(my_dict.keys())
# values方法提取所有值
print(my_dict.values())
