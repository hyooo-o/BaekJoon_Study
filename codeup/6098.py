d = []
x, y = 1, 1

for i in range(10):
    d.append(list(map(int, input().split())))

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] ==2:
        d[x][y] = 9
        break

    if d[x][y+1] == 1 and d[x+1][y] == 1:
        break

    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1
        
for i in range(10):
    for j in range(10):
        print(d[i][j], end = ' ')
    print()