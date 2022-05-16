n = int(input())
data = []

for i in range(1, int(n**(1/2))+1):
  if n % i == 0:
    data.append(i)
    if i != (n // i):
      data.append(n // i)

data.sort()

for i in data:
  print(i, end = ' ')