def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    connection = set([costs[0][0]])
    
    while len(connection) != n:
        for i, m in enumerate(costs):
            if m[0] in connection and m[1] in connection:
                continue
            if m[0] in connection or m[1] in connection:
                connection.update([m[0], m[1]])
                answer += m[2]
                costs[i] = [-1, -1, -1]
                break
    return answer