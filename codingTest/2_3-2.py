# 책 풀이_min()함수
import time

n, m = map(int, input().split())
result = 0

start =time.time()

for i in range(n):
    arr = (list(map(int, input().split())))
    arr_min = min(arr)
    result = max(result, arr_min)

print(result)

print(time.time()-start)