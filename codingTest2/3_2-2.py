n, m, k = map(int, input().split())
num = list(map(int, input().split()))
result = 0

num.sort(reverse=True)
set = num[0] * k + num[1]

result = (m // (k+1)) * set + (m % (k+1)) * num[0]

print(result)