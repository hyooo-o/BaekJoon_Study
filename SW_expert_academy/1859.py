t = int(input())

for i in range(1, t+1):
  sum = 0
  n = int(input())
  case = list(map(int, input().split()))
  num1 = case[-1]
  for j in range(n-2, -1, -1):
    if num1 > case[j]:
      sum += num1 - case[j]
    else:
      num1 = case[j] 
  print("#%d" %i, sum)