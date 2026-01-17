wire_seq = input()
stack = []
for terminal in wire_seq:
    if len(stack) == 0:
        stack.append(terminal)
    else:
        if stack[-1] == terminal:
            stack.pop()
        else:
            stack.append(terminal)
print("Yes" if len(stack) == 0 else "No")