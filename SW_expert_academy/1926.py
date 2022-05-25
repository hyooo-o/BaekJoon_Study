n = int(input())

for i in range(1, n+1):
    cnt = 0
    r = i % 10
    q = i // 10
    while q != 0 or r != 0:
        if r == 3 or r == 6 or r == 9:
            cnt += 1
        r = q % 10
        q //= 10
    if cnt == 0:
        print(i, end=' ')
    else:
        print("-" * cnt, end=' ')
