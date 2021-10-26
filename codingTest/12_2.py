s = list(input())
s.sort()
arr = []
sum = 0

for i in s:
    if i.isalpha():
        arr.append(i)
    else:
        sum += int(i)

arr.append(str(sum))
print(''.join(arr))