t = int(input())

for i in range(1, t+1):
  a, b = map(int, input().split())
  q = a // b
  r = a % b
  print(f"#{i} {q} {r}")