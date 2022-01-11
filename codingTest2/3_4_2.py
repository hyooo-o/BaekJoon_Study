n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k       # n//k 로 몫을 구하고 k를 곱해 나눌 수 있는 수를 찾음
    result += (n - target)      # k로 나눌 수 있는 값(target)이 되기 위해 n에서 -1를 몇 번 해야하는지
    n = target                  # -1 수행한 후의 n 값
    if n < k:
        break                   # n이 k로 나눠지지 않을 때 반복문 탈출
    result += 1                 # n이 k로 나눠질 때
    n //= k

result += (n-1)         # n이 1이 될 때까지 -1
print(result)