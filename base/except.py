# 异常与错误处理

'''
try:
  pass
except Exception as e:  相当于catch
  raise
else:  如果没有异常，则执行，通常不需要
  pass
finally:
  pass
'''

try:
  print('try...')
  r = 10 / 0
  print('result:', r)
except ZeroDivisionError as e:
  print('except:', e)
finally:
  print('finally')