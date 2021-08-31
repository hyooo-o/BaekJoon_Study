def solution(n, lost, reserve):
    result = n - len(lost)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if reserve[i] - 1 == lost[j] or reserve[i] + 1 == lost[j]:
                result += 1
                lost[j] = reserve[i]
    return result