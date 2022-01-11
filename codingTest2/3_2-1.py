n, m, k = map(int, input().split())
num = list(map(int, input().split()))
count = 0
result = 0

num.sort(reverse = True)

while True:
    for i in range(k):
        result += num[0]
        m -= 1
        if m == 0:
            break
    result += num[1]
    m -= 1
    if m == 0:
        break
        
print(result)