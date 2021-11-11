# 재귀함수 이용 - 스택 오버플로우 발생

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

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