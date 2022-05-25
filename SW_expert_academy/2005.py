t = int(input())

for i in range(1, t+1):
    n = int(input())
    li = [[] for _ in range(n)]
    for j in range(n):
        for k in range(j+1):
            # 해당 줄의 맨 앞, 맨 뒤 숫자는 1로 고정
            if k == 0 or j == k:
                li[j].append(1)
                continue
            _sum = li[j-1][k-1] + li[j-1][k]
            li[j].append(_sum)
    # 출력
    print("#%d" %i)
    for pascal in li:
        print(*pascal, sep=' ')