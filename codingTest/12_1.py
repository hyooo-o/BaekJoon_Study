n = list(map(int, input()))
 
num = len(n) // 2

a = n[:num]
b = n[num:]

if sum(a) == sum(b):
    print("LUCKY")
else:
    print("READY")