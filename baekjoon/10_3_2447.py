def star(a):
    matrix = []
    for i in range(3 * len(a)):
        if i // len(a) == 1:
            matrix.append(a[i % len(a)] + " " * len(a) + a[i % len(a)])
        else:
            matrix.append(a[i % len(a)] * 3)
    return list(matrix)

n = int(input())
s = ['***', '* *', '***']
k = 0

while n != 3:
    n = n//3
    k += 1

for i in range(k):
    s = star(s)

for i in s:
    print(i)