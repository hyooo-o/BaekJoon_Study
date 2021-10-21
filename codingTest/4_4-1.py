n, m = map(int, input().split())

visit = [[0] * m for _ in range(n)]
x, y, d = map(int, input().split())
visit[x][y] = 1

arr = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, input().split())))

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if visit[nx][ny] == 0 and arr[nx][ny] == 0:     
        x = nx
        y = ny
        count += 1
        visit[x][y] = 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y = dy[d]
        if arr[nx][ny] == 1:
            break
        else:
            x = ny
            y = ny
        turn_time = 0

print(count)