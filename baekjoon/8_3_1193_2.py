# 다른 풀이 - 간단
n = int(input())
line = 1
while n > line:
  n -= line
  line += 1
if line % 2 == 1:
    print(str(line-n+1)+'/'+str(n))
else:
    print(str(n)+'/'+str(line-n+1))