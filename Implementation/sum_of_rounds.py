def composition(num):
    arr = []
    size = len(num)
    for i in range(size):
        if num[i] != '0':
            arr.append((10**(size-i-1))*int(num[i]))
    return arr

n = int(input())
num_arr = []
for i in range(n):
    num_arr.append(input())
for num in num_arr:
    compose = composition(num)
    size = len(compose)
    print(size)
    for i in range(size):
        print(compose[i],end=' ' if i<size-1 else '\n')