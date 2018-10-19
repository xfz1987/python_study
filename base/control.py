# 条件控制语句 (没有switch-case)
'''
if 条件1:
	code-block1
elif 条件2:   (注意：是 elif 不是elseif)
	code-block2
else:
	code-block3
'''

var1 = 20
if var1:
	print('var1:',var1)

var2 = False
if var2:
	print('var2:',var2)

print('===============================')

var3 = 10
if var3 < 10:
	print('小于10')
elif var3 == 10:
	print('等于10')
else:
	print('大于10')

# if 嵌套
'''
if(){
	if(){
	
	}else{
	
	}
}
'''
if True:
	if True:
		pass
	else:
		pass
else:
	pass

age = 3
if age >= 18:
	print('your age is ', age)
	print('adult')
elif age >= 6:
	print('your age is ', age)
	print('teenager')
else:
	print('your age is ', age)
	print('kid')

'''
注意: 
	if是从上到下执行的，跟java、js不同
    如果某一个条件满足，即使也满足下面的条件，但下面的内容不会执行
    当我输入 age = 20 时，只会输出 adult，而不会输出 teenager
'''

print('循环语句===============================')

# whlie循环语句，break、continue
'''
while 条件:
	语句
'''
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
# 	sum += counter
# 	counter += 1 # python 没有++或--运算符 
# print('sum: ',sum)

# print('人机交互====================')
# while True:
# 	num = int(input('请输入一个数字:'))
# 	print(num)
# 	if num == 999:
# 		break

# else
count = 0
while count < 3:
	print('count: ', count)
	count += 1
else:
	print('else count:', count) # 3



# for循环语句，break、continue
'''
for name in names
	code-block
'''
names = ['gzf','zc','rc']
for name in names:
	print(name)  # gzf  zc  rc
else:
	print('for-end')

# enumerate(list) 循环出索引
names = ['a', 'b', 'c']
for index, name in enumerate(names):
    print(index, name)
# 0 a 1 b 2 c


for a in range(2, 5):
	print('a:', a)

# range(5) 可以生成一个从0到4整数序列 [0, 1, 2, 3, 4]
# range(2, 5) 生成序列 [2, 3, 4]
# range(1, 5, 3)   生成序列 [1, 4] 从 1-5 [1, 2, 3, 4]，然后从第2位数开始 +3

# xrange在python3已经弃用
# for x in xrange(1, 10):
# 	pass