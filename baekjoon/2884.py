H, M = map(int,input().split())

if H < 0 and H > 23 and M < 0 and M > 59:
    print("시간을 다시 입력하시오.")
elif M < 45:
    print(H-1, M+15)
elif M >= 45:
    print(H, M-45)
