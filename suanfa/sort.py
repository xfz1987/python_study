# 快速排序
# python没有 ?: 的写法
# 为真时的结果 if 判断条件 else 为假时的结果（注意，没有冒号）

# from math import floor
x = [5,4,6,3,2] 
def quickSort(list):
    if len(list) <= 1:
        return list
    base = list.pop(0)
    # base = list.pop(floor(len(list)/2))
    left = []
    right = []
    for l in list:
        left.append(l) if l < base else right.append(l)
    return quickSort(left) + [base] + quickSort(right)

result = quickSort(x)
print(result)