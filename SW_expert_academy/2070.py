t = int(input())

for i in range(1, t+1):
  case = list(map(int, input().split()))
  if case[0] == case[1]:
    print("#%d" %i, "=")
  elif case[0] < case[1]:
    print("#%d" %i, "<")
  else:
    print("#%d" %i, ">")