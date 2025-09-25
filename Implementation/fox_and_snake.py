nums = input()
[rows, cols] = [int(num) for num in nums.split(' ')]
first = False
last = True
for i in range(rows):
    for j in range(cols):
        if (i%2 == 0):
            print('#', end=''if j!=cols-1 else '\n')
        else:
            if first and j == 0:
                print('#',end='')
            elif last and j == cols-1:
                print('#', end='\n')
            else:
                print('.', end=''if j!=cols-1 else '\n')
            # update the flag in last
            if j == cols-1:
                first = not first
                last = not last