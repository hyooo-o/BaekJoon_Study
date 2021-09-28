# 내 풀이 - 복잡
x = int(input())
n = 1
cnt = 1

while cnt < x:
    n += 1
    cnt += n

if n % 2 == 0:
    print(x-(cnt-n), n-(x-(cnt-n))+1, sep = '/')
else:
    print(n-(x-(cnt-n))+1, x-(cnt-n), sep = '/')