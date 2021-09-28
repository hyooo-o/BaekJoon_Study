# import math

a, b, v = map(int, input().split())
day = 0

day = (v-b)/(a-b)

if day % 1 != 0:
    print(int(day+1))
else:
    print(int(day))


# 라이브러리 사용
# print(math.ceil(day))