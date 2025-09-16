num_entries = int(input())
ans = 0
for i in range(0,num_entries):
    val = input()
    if "++" in val:
        ans = ans + 1
    elif "--" in val:
        ans = ans - 1
print(ans)