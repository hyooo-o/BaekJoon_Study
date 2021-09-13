c = int(input())

for i in range(c):
    count = 0
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    for k in range(1, len(arr)):
        if arr[k] > avg:
            count += 1
    result = count / arr[0] * 100
    print("%.3f%%" %result)