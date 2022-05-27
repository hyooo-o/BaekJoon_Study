t = int(input())
a = []

for i in range(1, t+1):
    li, n = list(map(int, input().split()))
    for j in str(li):
        a.append(j)
    # n번 위치 교환
    for k in range(n):
        for m in range(a):
            if