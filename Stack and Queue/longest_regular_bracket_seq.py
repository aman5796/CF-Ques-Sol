sequence = input().strip()
stack = [-1]
max_len = 0
count = 0

for i, ch in enumerate(sequence):
    if ch == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            curr_len = i - stack[-1]
            if curr_len > max_len:
                max_len = curr_len
                count = 1
            elif curr_len == max_len:
                count += 1

if max_len == 0:
    print("0 1")
else:
    print(max_len, count)
