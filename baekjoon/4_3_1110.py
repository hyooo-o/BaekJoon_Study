num = int(input())
num1 = num
n = 0

while True:
    a = num1 // 10
    b = num1 % 10
    c = (a + b) % 10
    num2 = b * 10 + c
    n += 1
    if num == num2:
        print(n)
        break
    else:
        num1 = num2
