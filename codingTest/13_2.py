import time

start = time.time()
n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
  data.append(list(map(int, input().split())))

# 상하좌우
nx = [-1, 1, 0, 0]
ny = [0, 0, -1,  1]
result = 0

def virus(x, y):
  for i in range(4):
    dx = x + nx[i]
    dy = y + ny[i]

    if dx >= 0 and dx < n and dy >= 0 and dy < m:
      if temp[dx][dy] == 0:
        temp[dx][dy] = 2
        virus(dx, dy)

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

def dfs(count):
  global result
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    result = max(result, get_score())
    return

  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        count -= 1
        data[i][j] = 0
      
dfs(0)
print(result)
print(time.time() - start)