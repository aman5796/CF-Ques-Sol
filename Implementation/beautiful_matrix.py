arr = []
for i in range(5):
    arr.append(input())
for i in range(1,6):
    a = arr[i-1].split(" ")
    for j in range(1,6):
        if a[j-1] == '1':
            row = i
            col = j
            break
print(abs(3-row) + abs(3-col))