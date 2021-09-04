def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n - len(lost)