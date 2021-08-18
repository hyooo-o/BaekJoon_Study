arr = []
n = 0
for i in range(3):
    arr.append(int(input()))
result = arr[0]*arr[1]*arr[2]
rel = []
while result != 0:
    rel.append(result%10)
    result //= 10
while n < 10:
    count = 0
    for j in rel:
        if j == n:
            count = count+1
    print(count)
    n += 1