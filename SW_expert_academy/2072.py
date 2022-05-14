s = int(input())

for i in range(1, s+1):
    sum = 0
    case = map(int, input().split())
    for j in case:
        if j % 2 == 1:
            sum += j
    print("#%d" %i, sum)