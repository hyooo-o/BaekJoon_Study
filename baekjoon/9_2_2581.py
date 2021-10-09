m = int(input())
n = int(input())
dec = []

for i in range(m, n+1):
    x = 0
    if i > 2:
        for j in range(2, i):
            if i % j == 0:
                x += 1
                break
        if x == 0:
            dec.append(i)

if not dec:
    print(-1)
else:
    print(sum(dec))
    print(min(dec))