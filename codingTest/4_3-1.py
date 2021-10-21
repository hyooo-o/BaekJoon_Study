n = input()
x = int(ord(n[0])) - int(ord('a')) + 1
y = int(n[1])

step = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

result = 0
for i in step:
    nx = x + i[0]
    ny = y + i[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    result += 1

print(result)