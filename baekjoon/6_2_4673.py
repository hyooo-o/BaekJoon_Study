def d(n):
    for i in str(n):
        n += int(i)
    return n

arr = set(range(1, 10000))
arr2 = []

for i in arr:
    arr2.append(d(i))

result = sorted(arr-set(arr2))

for i in result:
    print(i)