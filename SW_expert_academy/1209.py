for i in range(1, 11):
    t = int(input())
    _max = 0
    li = [list(map(int, input().split())) for _ in range(100)]
    # 각 행, 열의 합 중 최댓값
    for k in range(100):
        row = 0
        cal = 0
        for m in range(100):
            row += li[k][m]
            cal += li[m][k]
        _max = max(row, cal, _max)
    # 대각선 2개의 합을 구해서 위에서 구한 최댓값 _max와 비교해 최종 최댓값 구하기
    dia1 = 0
    dia2 = 0
    for j in range(100):
        dia1 += li[j][j]
        dia2 += li[j][99-j]
    _max = max(_max, dia1, dia2)

    print('#{} {}' .format(i, _max))