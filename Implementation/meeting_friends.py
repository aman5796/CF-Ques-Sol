nums = input()
arr = [int(n) for n in nums.split(' ')]
arr.sort()
print((arr[1]-arr[0]) + (arr[2]-arr[1]))