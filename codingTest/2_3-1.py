# 내 풀이_sort()함수
import time

n, m = map(int, input().split())
arr = []

start = time.time()

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    arr[i].sort()

for i in range(1, n):
    max = arr[0][0]
    if arr[i][0] > max:
        max = arr[i][0]
print(max)

print(time.time() - start)