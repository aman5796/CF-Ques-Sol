import math
ip = input()
[n,l,k,c,d,p,nl,np] = [int(num) for num in ip.split(" ")]
toast = math.floor((l*k)/nl)
slices = c*d
salt = math.floor(p/np)
print(math.floor(min([toast,slices,salt])/n))