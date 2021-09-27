n = int(input())
count = 0

for i in range(n):
    b = []
    word = list(map(str, input()))
    temp = word[0]
    for j in range(len(word)):
        if temp == word[j]:
            b.append(word[j])
        else:            
            if word[j] not in b:
                temp = word[j]
                b.append(word[j])
            else:
                break
        if j == len(word)-1:
            count += 1
print(count)