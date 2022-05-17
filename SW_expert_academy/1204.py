t = int(input())

for i in range(1, t+1):
  num = int(input())
  case = list(map(int, input().split()))
  n = [0] * 101
  for j in case:
    n[j] += 1
    max = 0
    result = 0
  for k, v in enumerate(n):
    if max <= v:
      max = v
      result = k
  print('#{} {}' .format(i, result))