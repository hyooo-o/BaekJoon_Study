# 반복문 이용

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
shop = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))
shop.sort()

for i in need:
    result = binary_search(shop, i, 0, n-1)
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')