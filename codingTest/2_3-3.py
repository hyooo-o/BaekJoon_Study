# 책 풀이_2중 for문
import time

n, m = map(int, input().split())
result = 0

start = time.time()

for i in range(n):
    data = list(map(int, input().split()))
    arr_min = 10001
    for j in data:
        arr_min = min(arr_min, j)
    result = max(result, arr_min)

print(result)

print(time.time()-start)