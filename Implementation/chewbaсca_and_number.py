number = input()
ans = ""
for indx in range(1,len(number)):
    digit = ord(number[indx])%48
    ans = ans + str(digit if(digit < 9-digit) else 9-digit)
digit = ord(number[0])%48
ans = str(digit if(digit == 9 or digit < 9-digit) else 9-digit) + ans
print(ans)