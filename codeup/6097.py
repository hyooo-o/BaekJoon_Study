h, w = map(int, input().split())
a = []
for i in range(h+1):
    a.append([])
    for j in range(w+1):
        a[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for i in range(l):
            a[x][y+i] = 1
    else:
        for i in range(l):
            a[x+i][y] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        print(a[i][j], end = ' ')
    print()