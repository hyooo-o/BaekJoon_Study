t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    # n*n 배열 초기화
    li = [[0] * n for _ in range(n)]
    # n*n 2차원 배열에 숫자 할당
    for j in range(n):
        li[j] = list(map(int, input().split()))
    # 전체 파리채 중 최대 개수인 _max 변수와 좌표 이동을 위한 x, y 변수 초기화
    _max = 0
    x, y = 0, 0
    # 파리채 이동하며 해당 영역에 존재하는 파리 개수 구하기
    for p in range(n-m+1):
        for q in range(n-m+1):
            _sum = 0
            # 죽은 파리 개수
            for k in range(m):
                for r in range(m):
                    _sum += li[x+k][y+r]
            _max = max(_sum, _max)
            y += 1
        y = 0
        x += 1
    print("#%d" %i, _max)
