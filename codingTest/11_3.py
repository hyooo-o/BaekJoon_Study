import time

s = input()
num0 = 0
num1 = 0

h = time.time()
if s[0] == '0':
    num1 += 1
else:
    num0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            num1 += 1
        else:
            num0 += 1

print(min(num0, num1))
print(time.time() - h)