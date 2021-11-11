# 계수정렬 이용

n = int(input())
shop = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))

arr = [0] * (max(shop)+1)

for i in shop:
    arr[i] = 1

for i in need:
    if arr[i] == 1:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')


