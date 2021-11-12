x = int(input())
d = [0] * 30001

for a in range(2, x+1):
    d[a] = d[a-1] + 1
    if a % 5 == 0:
        d[a] = min(d[a], d[a//5] + 1)
    if a % 3 == 0:
        d[a] = min(d[a], d[a//3] + 1)
    if a % 2 == 0:
        d[a] = min(d[a], d[a//2] + 1)

print(d[x])