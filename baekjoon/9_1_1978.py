n = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    x = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                x += 1
                break
        if x == 0:
            count += 1
print(count)