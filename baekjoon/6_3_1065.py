def d(n):
    count = 0
    if n >= 100:
        for m in range(100, n+1):
            i = m // 100
            j = m // 10 % 10
            k = m % 10  
            if i - j == j - k:
                count += 1
        count += 99
    else:
        count = n
    return count

n = int(input())
print(d(n))