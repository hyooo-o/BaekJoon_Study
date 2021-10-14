def solution(name):
    answer = 0
    next_i = 0
    min_move = len(name)
    
    for i, n in enumerate(name):
        next_i = i+1
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        min_move = min(min_move, i + i + len(name) - next_i)    # 왜 루프 안에 두냐면 어차피 오른쪽 값은 계속 +1 씩 증가함
    answer += min_move
    return answer