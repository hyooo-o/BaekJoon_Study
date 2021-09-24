alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
count = 0

for i in range(len(a)):
    for j in alp:
        if a[i] in j:
            count += alp.index(j) + 3

print(count)