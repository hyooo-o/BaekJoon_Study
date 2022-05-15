t = int(input())

for i in range(1, t+1):
  case = map(int, input().split())
  print("#%d" %i, max(case))