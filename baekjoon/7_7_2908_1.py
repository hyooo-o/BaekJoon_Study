a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

print(type(a))
if a > b:
    print(a)
else:
    print(b)