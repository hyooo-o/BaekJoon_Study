s = input()
result = int(s[0])

for i in range(1, len(s)):
    i = int(s[i])
    if result < 2 or i < 2:
        result += i
    else:
        result *= i
        
print(result)