n = int(input())
arr = []

for i in range(n):
  count = 0
  sum = 0
  arr = list(input())
  for j in range(len(arr)):
    if arr[j] == 'O':
      count += 1
      sum += count
    else:
      count = 0
  print(sum)
    