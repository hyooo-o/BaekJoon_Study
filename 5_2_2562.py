arr = []
for i in range(9):
    arr.append(int(input()))

print(max(arr))
a = arr.index(max(arr))
print(a+1)