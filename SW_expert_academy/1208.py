for i in range(1, 11):
    t = int(input())
    li = list(map(int, input().split()))
    for j in range(t):
        a = li.index(max(li))
        b = li.index(min(li))
        li[a] -= 1
        li[b] += 1
    data = max(li) - min(li)
    print('#{} {}' .format(i, data))