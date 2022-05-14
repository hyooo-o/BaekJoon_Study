T = int(input())

for i in range(1, T+1):
    case = list(map(int, input().split()))
    avg = sum(case) / len(case)
    print("#%d" %i, round(avg))