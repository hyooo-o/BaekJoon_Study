for i in range(1, 11):
    n = int(input())
    li = [list(input()) for _ in range(8)]
    cnt = 0
    for j in range(8):
        for k in range(8-n+1):
            # 가로
            row = li[j][k:k+n]
            if row == row[::-1]:
                cnt += 1
            # 세로
            cal = ''
            for c in range(k, k+n):
                cal += li[c][j]
            if cal == cal[::-1]:
                cnt += 1
    print('#{} {}' .format(i, cnt))