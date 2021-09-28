t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    ho = n // h
    if n % h == 0:
        print(h*100 + ho)
    else:
        print(floor*100 + (ho+1))