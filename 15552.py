import sys

n = int(input())

for i in range(0, n):
    _input = sys.stdin.readline().split()
    a, b = map(int, _input)
    print(a + b)
