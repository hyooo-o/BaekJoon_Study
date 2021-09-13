n = int(input())
arr = list(map(int, input().split()))
m_arr = max(arr)
avg = 0
for i in range(n):
  avg += arr[i] / m_arr * 100
print(avg/n)