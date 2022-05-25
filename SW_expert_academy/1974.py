t = int(input())

for i in range(1, 1+t):
    result = 1
    cube = [list(map(int, input().split())) for _ in range(9)]
    # 가로, 세로 확인
    for j in range(9):
        row = [0] * 10
        cal = [0] * 10
        for k in range(9):
            # 숫자가 중복되면 0 반환 후, 종료
            if row[cube[j][k]] or cal[cube[k][j]]:
                result = 0
                break
            row[cube[j][k]] = 1
            cal[cube[k][j]] = 1
            # 3X3 확인 (j, k = 0, 3, 6일 때)
            square = [0] * 10
            if j % 3 == 0 and k % 3 == 0:
                for r in range(j, j+3):
                    for m in range(k, k+3):
                        # 숫자가 중복되면 0 반환 후, 종료
                        if square[cube[r][m]]:
                            result = 0
                            break
                        square[cube[r][m]] = 1
    print("#%d" %i, result)