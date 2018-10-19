# 老兔子生小兔子

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

print(fibs(5))

def fibs(num):
    # if num == 0 or num == 1:
    if num <= 1:
        return num
    else:
        return fibs(num-2) + fibs(num-1)
print(fibs(5))