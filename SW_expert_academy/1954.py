t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, t + 1):
    n = int(input())
    li = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dist = 0
    for j in range(1, n * n + 1):
        li[x][y] = j
        x += dx[dist]
        y += dy[dist] 
        # 순서대로 조건을 비교하므로 li[x][y] != 0 을 맨 앞에 두면 인덱스 범위 에러가 날 수 있음
        if  x < 0 or y < 0 or x >= n or y >= n or li[x][y] != 0:
            x -= dx[dist]
            y -= dy[dist]
            dist = (dist + 1) % 4  # 0 1 2 3, 4 5 6 7, ...
            x += dx[dist]
            y += dy[dist]
    print("#%d" %i)
    for row in li:
        print(*row)
