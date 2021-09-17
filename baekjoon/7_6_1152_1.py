a = input().split(' ')

if a[0] == '':
    del a[0]
if a[-1] == '':
    del a[-1]

print(len(a))