for i in range(1, 11):
    t = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    for k in range(2, t-2):
        if li[k] - max(li[k+1], li[k+2], li[k-1], li[k-2]) > 0:
            cnt += li[k] - max(li[k+1], li[k+2], li[k-1], li[k-2])
    print('#{} {}' .format(i, cnt))