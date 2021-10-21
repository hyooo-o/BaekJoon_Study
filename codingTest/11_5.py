n, m = map(int, input().split())
weight = list(map(int, input().split()))
count = 0

array = [0] * 11
for i in weight:
    array[i] += 1

for i in array:
    if i != 0:
        n -= i
        count += i * n

print(count)