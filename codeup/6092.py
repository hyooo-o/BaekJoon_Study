n = int(input())
a = input().split()
for j in range(n):
    a[j] = int(a[j])
for i in range(1, 24):
    print(a.count(i), end = ' ')