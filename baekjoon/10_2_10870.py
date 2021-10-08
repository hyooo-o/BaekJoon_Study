n = int(input())

def fibonacci(a):
    if a < 2:
        return a
    return fibonacci(a-1) + fibonacci(a-2)

print(fibonacci(n))