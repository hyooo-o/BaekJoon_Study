n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
count = 0

for i in data:
    count += 1
    if i  <= count:
        group += 1
        count = 0

print(group)